import os
import secrets

from flask import Flask, abort, redirect, render_template, request, session, url_for

from calculations import calculate_balances, calculate_transfers, total_expenses

app = Flask(__name__, static_folder="public/static")

secret_key = os.environ.get("SECRET_KEY")
if os.environ.get("VERCEL") and not secret_key:
    raise RuntimeError("Set SECRET_KEY before deploying the app.")
app.secret_key = secret_key or secrets.token_hex(32)
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
app.config["SESSION_COOKIE_SECURE"] = bool(os.environ.get("VERCEL"))

members = ["Elon Musk", "Donald Trump", "JD Vance"]

# Amounts are stored in cents: 4200 means CHF 42.00.
sample_expenses = [
    {"id": 1, "person": "Elon Musk", "description": "Wi-Fi for Mars", "amount": 4200},
    {"id": 2, "person": "Donald Trump", "description": "Gold spray for the toaster", "amount": 3000},
    {"id": 3, "person": "Elon Musk", "description": "Backyard rocket launch", "amount": 1800},
]


def get_expenses():
    if "expenses" not in session:
        session["expenses"] = list(sample_expenses)
    return session["expenses"]


def save_expenses(expenses):
    # Leave room for the cookie name and settings within the browser's limit.
    serializer = app.session_interface.get_signing_serializer(app)
    if len(serializer.dumps({"expenses": expenses})) > 3500:
        return False
    session["expenses"] = expenses
    return True


def parse_amount(text):
    parts = text.strip().replace(",", ".").split(".")
    if len(parts) > 2 or not parts[0].isdecimal() or len(parts[0]) > 6:
        raise ValueError("Enter an amount between CHF 0.01 and CHF 999999.99.")

    cents = "00"
    if len(parts) == 2:
        if not parts[1].isdecimal() or len(parts[1]) > 2:
            raise ValueError("Use no more than two decimal places.")
        cents = parts[1].ljust(2, "0")

    amount = int(parts[0]) * 100 + int(cents)
    if amount <= 0:
        raise ValueError("The amount must be greater than zero.")
    return amount


@app.template_filter("chf")
def format_chf(cents):
    sign = "-" if cents < 0 else ""
    cents = abs(cents)
    return f"{sign}{cents // 100}.{cents % 100:02d}"


@app.route("/", methods=["GET", "POST"])
def home():
    expenses = get_expenses()
    error = None
    form = {"person": members[0], "description": "", "amount": ""}

    if request.method == "POST":
        form = {
            "person": request.form.get("person", ""),
            "description": request.form.get("description", "").strip(),
            "amount": request.form.get("amount", "").strip(),
        }

        if form["person"] not in members:
            error = "Choose one of the flatmates."
        elif not form["description"] or len(form["description"]) > 80:
            error = "Enter a description between 1 and 80 characters."
        else:
            try:
                amount = parse_amount(form["amount"])
            except ValueError as message:
                error = str(message)

        if error is None:
            next_id = 1
            if expenses:
                next_id = expenses[-1]["id"] + 1

            new_expense = {
                "id": next_id,
                "person": form["person"],
                "description": form["description"],
                "amount": amount,
            }
            if save_expenses(expenses + [new_expense]):
                return redirect(url_for("home"))
            error = "The demo is full. Remove an expense before adding another."

    return render_template(
        "index.html",
        members=members,
        expenses=expenses,
        total=total_expenses(expenses),
        form=form,
        error=error,
    ), 400 if error else 200


@app.route("/settlement")
def settlement():
    expenses = get_expenses()
    balances = calculate_balances(members, expenses)
    return render_template(
        "settlement.html",
        balances=balances,
        transfers=calculate_transfers(balances),
        total=total_expenses(expenses),
    )


@app.route("/expenses/<int:expense_id>/delete", methods=["POST"])
def delete_expense(expense_id):
    expenses = get_expenses()
    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)
            session["expenses"] = expenses
            return redirect(url_for("home"))
    abort(404)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
