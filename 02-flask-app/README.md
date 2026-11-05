# Flat Force One

Flat Force One splits shared expenses between Elon Musk, Donald Trump and JD Vance. It calculates each person's share and who needs to pay whom.

[Live demo](https://flat-force-one-isd.vercel.app)

## Run the app

You need Python 3.9 or later and pip. Open a terminal in `02-flask-app`. On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

On Windows, create the environment with `py -m venv .venv` and activate it in PowerShell with `.venv\Scripts\Activate.ps1`. Then use the same `python` commands.

Open [http://127.0.0.1:5001](http://127.0.0.1:5001). Press `Ctrl+C` in the terminal to stop the server. `debug=True` is intended for local development.

## Features

- Add and remove shared expenses.
- Show the total and the amount paid by each flatmate.
- Split costs equally between the three flatmates.
- Calculate balances and suggested payments.
- Reject missing or invalid form values with an error message.

Every expense is shared by all three people. The selected person is the one who paid the bill upfront. The app suggests payments; it does not transfer money or record completed settlement payments.

## Example

| Flatmate | Paid | Share | Balance |
| --- | ---: | ---: | ---: |
| Elon Musk | CHF 60.00 | CHF 30.00 | CHF 30.00 |
| Donald Trump | CHF 30.00 | CHF 30.00 | CHF 0.00 |
| JD Vance | CHF 0.00 | CHF 30.00 | CHF -30.00 |

JD should pay Elon CHF 30.00.

Amounts are stored as whole cents, where 100 cents equal CHF 1.00. If a total cannot be divided evenly, leftover cents are assigned in the order of the members list. The shares therefore add up to the exact total.

## Files

```text
02-flask-app/
  app.py                  Flask routes, form handling and sample data
  calculations.py         Totals, balances and suggested payments
  requirements.txt        Flask dependency
  vercel.json             Hosting configuration
  DEMO.md                 Live demonstration outline
  templates/
    base.html             Shared page layout
    index.html            Expense list and form
    settlement.html       Balances and suggested payments
  public/static/
    style.css             Styling
    flat-kitchen.png      Caricature of the flatmates
```

Each browser has its own copy of the expenses in a signed Flask session cookie. Changes survive page reloads and do not affect other visitors. Clearing the site's cookies starts a fresh demo. There is no database or shared account. Session cookies are signed but not encrypted.

Locally, the app generates a signing key at startup. Restarting it resets existing sessions unless you set a stable `SECRET_KEY` environment variable. The app rejects new entries if they would exceed its cookie storage limit.

## Deploy on Vercel

Import this repository and set **Root Directory** to `02-flask-app` and **Framework Preset** to `Flask`. Add a random `SECRET_KEY` as a production environment variable in Vercel, then deploy. Keep the key out of the repository. Vercel starts the Flask application directly, without the local debug server.

The files in `public/static/` serve at `/static/` both locally and online.

## Manual checks

1. Start the app. The expense page shows CHF 90.00 and three expenses.
2. Open **Settlement**: JD pays Elon CHF 30.00.
3. Add an expense paid by JD Vance, with description `Dishwashing gloves` and amount `30.00`.
4. The total is now CHF 120.00. Donald and JD each pay Elon CHF 10.00.
5. Remove the gloves entry. The original settlement returns.
6. Try adding an expense with amount `0`. An error appears and the expense list stays unchanged.

## Documentation

Routes, forms and templates are described in the [Flask Quickstart](https://flask.palletsprojects.com/en/stable/quickstart/).
