def total_expenses(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total


def calculate_balances(members, expenses):
    if not members:
        raise ValueError("At least one flatmate is required.")

    total = total_expenses(expenses)
    share = total // len(members)
    remaining_cents = total % len(members)
    balances = []

    for index in range(len(members)):
        name = members[index]
        paid = 0
        for expense in expenses:
            if expense["person"] == name:
                paid += expense["amount"]

        # A single cent cannot be split further.
        personal_share = share
        if index < remaining_cents:
            personal_share += 1

        balances.append({
            "name": name,
            "paid": paid,
            "share": personal_share,
            "balance": paid - personal_share,
        })

    return balances


def calculate_transfers(balances):
    debtors = []
    creditors = []

    for person in balances:
        if person["balance"] < 0:
            debtors.append({"name": person["name"], "amount": -person["balance"]})
        elif person["balance"] > 0:
            creditors.append({"name": person["name"], "amount": person["balance"]})

    transfers = []
    debtor_index = 0
    creditor_index = 0

    while debtor_index < len(debtors) and creditor_index < len(creditors):
        debtor = debtors[debtor_index]
        creditor = creditors[creditor_index]
        amount = min(debtor["amount"], creditor["amount"])

        transfers.append({
            "from": debtor["name"],
            "to": creditor["name"],
            "amount": amount,
        })

        debtor["amount"] -= amount
        creditor["amount"] -= amount

        if debtor["amount"] == 0:
            debtor_index += 1
        if creditor["amount"] == 0:
            creditor_index += 1

    return transfers
