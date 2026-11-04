from flask import Flask, abort, redirect, render_template, request, url_for

from calculations import calculate_balances, calculate_transfers, total_expenses

app = Flask(__name__)

members = ["Elon Musk", "Donald Trump", "JD Vance"]

# Amounts are stored in cents: 4200 means CHF 42.00.
expenses = [
    {"id": 1, "person": "Elon Musk", "description": "Wi-Fi for Mars", "amount": 4200},
    {"id": 2, "person": "Donald Trump", "description": "Gold spray for the toaster", "amount": 3000},
    {"id": 3, "person": "Elon Musk", "description": "Backyard rocket launch", "amount": 1800},
]


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

            expenses.append({
                "id": next_id,
                "person": form["person"],
                "description": form["description"],
                "amount": amount,
            })
            return redirect(url_for("home"))

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
    balances = calculate_balances(members, expenses)
    return render_template(
        "settlement.html",
        balances=balances,
        transfers=calculate_transfers(balances),
        total=total_expenses(expenses),
    )


@app.route("/expenses/<int:expense_id>/delete", methods=["POST"])
def delete_expense(expense_id):
    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)
            return redirect(url_for("home"))
    abort(404)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
