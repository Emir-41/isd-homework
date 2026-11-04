# Presenting Flat Force One

## Opening

“Imagine Elon Musk, Donald Trump and JD Vance sharing a flat. The Wi-Fi supposedly reaches Mars. The toaster has been painted gold. Nobody has done the dishes. And now someone has to split the bills.”

The flat and all expenses are fictional. This is the satirical setup for the demonstration.

## The first bill

- Elon pays CHF 42 for Wi-Fi for Mars.
- Donald pays CHF 30 for gold spray for the toaster.
- Elon pays another CHF 18 for a backyard rocket launch.
- JD has not paid for anything yet.

Total: CHF 90. Each flatmate owes a share of CHF 30. Elon has paid CHF 60, so he should receive CHF 30 back. Donald is even. JD should pay Elon CHF 30.

“Apparently, even a rocket launch gets split three ways in this flat.”

## Live demonstration

1. Open **Expenses** and briefly show the three entries.
2. Open **Settle up**: JD pays Elon CHF 30.
3. Return to **Expenses**. Select JD Vance, enter `Dishwashing gloves` and `30.00`, then click **Add expense**.
4. “JD has finally bought something. Unfortunately, that does not quite clear his debt.”
5. The total is now CHF 120. Each person owes a share of CHF 40. Donald and JD each pay Elon CHF 10.
6. Remove the gloves entry. The original settlement returns.

## Move to the Python code

“The characters provide the joke. The data structure is the same as the product catalogue in our notebook: a list of dictionaries.”

Show the expenses in `app.py`, then `total_expenses()` and `calculate_balances()` in `calculations.py`. Explain the formula `paid − share`. Next, show how `render_template()` sends the data to the HTML page.

The caricature is an image in `public/static/`. It has no effect on the calculation. Each browser has its own demo expenses in a signed cookie. Clearing the site's cookies restores the sample data.
