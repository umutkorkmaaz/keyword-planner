# Keyword Planner
This tool makes suggestions based on the keyword provided, using the Google Keyword Planner API.

This tool allows you to save keywords as CSV and also contains search volumes for keywords.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
usage: index.py [-h] --customer-id CUSTOMER_ID [--keyword KEYWORD [KEYWORD ...]] [--output OUTPUT] [--quiet]

Google Ads API keyword suggestion tool

options:
  -h, --help            show this help message and exit
  --customer-id CUSTOMER_ID, -c CUSTOMER_ID
                        Google Ads customer ID
  --keyword KEYWORD [KEYWORD ...], -w KEYWORD [KEYWORD ...]
                        Keyword to get suggestions for
  --output OUTPUT, -o OUTPUT
                        Output file name for the keyword suggestions
  --quiet, -q           Suppress output to console
```

## Example

```bash
python index.py -q -c [CUSTOMER_ID] -w [KEYWORD] --output example
```
