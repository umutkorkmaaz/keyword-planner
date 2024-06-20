# Keyword Planner
[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/umutkorkmaz)

This tool makes suggestions based on the keyword provided, using the Google Keyword Planner API.

This tool allows you to save keywords as CSV and also contains search volumes for keywords.

## Installation

```bash
pip install -r requirements.txt
```

or 

```bash
chmod +x scripts/install.sh
./scripts/install.sh [customer_id] [developer_token] [client_id] [client_secret] [refresh_token]
```


## Usage

```bash
usage: kwplanner [-h] --customer-id CUSTOMER_ID [--keyword KEYWORD [KEYWORD ...]] [--output OUTPUT] [--quiet]

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

## Examples

Rename output csv file
```bash
kwplanner -q -c [CUSTOMER_ID] -w [KEYWORD] --output example
```
Reorder the output csv file
```bash
kwplanner -q -w keyword | sort -k3,3n -t',' keyword.csv
```