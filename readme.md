# Data product developed to help reduce food waste in Nantes metropole's Canteens

The dashboard was made using boostrap, plotly and flask. The predictive tool is made using lightGBM library from Microsoft.

## Architecture

The web app is made of :
- a dashboard displaying useful informations for canteen staff,
- a predictive tool to make predictions about the attendance of the canteens in 2/3 week and beyond,
- a contact page to give feedback about the app.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required libraries.

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

Open a terminal, and go into the app root directory.

```bash
python wsgy.py
```

### Test the app

```bash
source venv/bin/activate
cd tests/
pytest
```

## Config

- For dev and test config : using a local database and gmail SMTP server for contact form 
- For prod config : using an azure database, twilio sendgrid SMTP server and app insights for logging

Set environment variables accordingly.

## License
[MIT](https://choosealicense.com/licenses/mit/)
