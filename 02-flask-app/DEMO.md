# Flat Force One demo

## Opening

Elon, Donald and JD share a flat. Elon has paid for Wi-Fi and a rocket launch, Donald has bought gold spray for the toaster, and JD has paid nothing yet. The app calculates how they should split the costs.

## The first bill

- Elon pays CHF 42 for Wi-Fi for Mars.
- Donald pays CHF 30 for gold spray for the toaster.
- Elon pays another CHF 18 for a backyard rocket launch.
- JD has not paid for anything yet.

Total: CHF 90. Each flatmate owes a share of CHF 30. Elon has paid CHF 60, so he should receive CHF 30 back. Donald is even. JD should pay Elon CHF 30.

## Live demonstration

1. Open **Expenses** and briefly show the three entries.
2. Open **Settlement**: JD pays Elon CHF 30.
3. Return to **Expenses**. Select JD Vance, enter `Dishwashing gloves` and `30.00`, then click **Add expense**.
4. Open **Settlement** again. The total is now CHF 120. Each person owes a share of CHF 40. Donald and JD each pay Elon CHF 10.
5. Remove the gloves entry. The original settlement returns.

## Move to the Python code

Show `sample_expenses` in `app.py` as an example of a list of dictionaries. Then open `total_expenses()` and `calculate_balances()` in `calculations.py` and explain `paid - share`. Finally, show how `render_template()` passes the results to the HTML page.

The caricature is an image in `public/static/`. It has no effect on the calculation. Each browser has its own demo expenses in a signed cookie. Clearing the site's cookies restores the sample data.
