# Information Systems Development homework

Two independent assignments from Session 3.

| Assignment | Folder | Contents |
| --- | --- | --- |
| 1. Kadane's algorithm | [01-kadane](01-kadane/README.md) | Maximum subarray indices, maximum sum and a stock-profit example |
| 2. Personal Flask app | [02-flask-app](02-flask-app/README.md) | Flat Force One, a shared-expense splitter |

## Assignment 1: Kadane

Requires Python 3.9 or later. From the repository root:

```bash
python3 01-kadane/kadane.py
```

The notebook example returns start index `3`, end index `6` and maximum sum `9`.
No Flask installation is needed.

## Assignment 2: Flask app

Flat Force One is a fictional flat shared by Elon Musk, Donald Trump and JD Vance. The app records shared expenses and suggests who pays whom. All characters' purchases are invented for the story.

[Open the live demo](https://flat-force-one-isd.vercel.app). Each browser has its own demo expenses.

On macOS or Linux, from the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r 02-flask-app/requirements.txt
python 02-flask-app/app.py
```

On Windows, create the environment with `py -m venv .venv` and activate it with `.venv\Scripts\Activate.ps1` in PowerShell. Then use the same `python` commands.

Open [http://127.0.0.1:5001](http://127.0.0.1:5001). Stop the server with `Ctrl+C`.

See the [app README](02-flask-app/README.md) for features and limitations, and the [live demonstration outline](02-flask-app/DEMO.md) for the presentation.

The two assignments do not import or call each other.
