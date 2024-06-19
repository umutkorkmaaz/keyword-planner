from math import e
from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException
import pandas as pd
from slugify import slugify
import argparse

customer_id = ""
keyword_text = ""
fileName = ""
output = False

parser = argparse.ArgumentParser(description="Google Ads API keyword suggestion tool")

parser.add_argument(
    "--customer-id",
    "-c",
    type=str,
    help="Google Ads customer ID",
    required=True,
)
parser.add_argument(
    "--keyword", "-w", type=str, nargs="+", help="Keyword to get suggestions for"
)
parser.add_argument(
    "--output",
    "-o",
    type=str,
    help="Output file name for the keyword suggestions",
    default="",
    required=False,
)
parser.add_argument(
    "--quiet",
    "-q",
    help="Suppress output to console",
    action="store_true",
)

args = parser.parse_args()


def quiet_print(text):
    if args.quiet is False:
        print(text)


if args.keyword:
    keyword_text = " ".join(args.keyword)
    quiet_print(f"Looking for provided keyword: {keyword_text}")
else:
    quiet_print("Usage: python index.py --keyword [keyword]")
    exit(1)

if args.output is None:
    output = False
else:
    output = True

if output is True:
    if args.output == "":
        fileName = slugify(keyword_text) + ".csv"
    else:
        fileName = args.output + ".csv"


if args.customer_id:
    customer_id = args.customer_id
    if args.quiet is False:
        quiet_print(f"Using provided customer ID: {customer_id}")
else:
    if args.quiet is False:
        quiet_print("Usage: python index.py --customer-id [customer_id]")

    exit(1)


google_ads_client = GoogleAdsClient.load_from_storage(path="google-ads.yaml")
keywordList = pd.DataFrame(columns=["Keyword", "Avg. Monthly Searches"])


def get_keyword_suggestions(client, customer_id, keyword_text):
    keyword_plan_idea_service = client.get_service(
        "KeywordPlanIdeaService", version="v17"
    )

    request = client.get_type("GenerateKeywordIdeasRequest", version="v17")
    request.customer_id = customer_id
    request.language = client.get_service(
        "GoogleAdsService", version="v17"
    ).language_constant_path("1037")
    request.geo_target_constants.append(
        client.get_service("GoogleAdsService", version="v17").geo_target_constant_path(
            "21069",
        )
    )

    keyword_seed = client.get_type("KeywordSeed", version="v17")
    keyword_seed.keywords.append(keyword_text)
    request.keyword_seed = keyword_seed

    try:
        response = keyword_plan_idea_service.generate_keyword_ideas(request=request)
        for idea in response.results:
            keywordList.loc[len(keywordList)] = [
                idea.text,
                idea.keyword_idea_metrics.avg_monthly_searches,
            ]
    except GoogleAdsException as ex:
        quiet_print(
            f"Request failed with status: {ex.error.code().name}, and includes the following errors:"
        )
        for error in ex.failure.errors:
            quiet_print(f"\tError with message: {error.message}")


get_keyword_suggestions(google_ads_client, customer_id, keyword_text)

if keywordList.empty:
    quiet_print("No keyword suggestions found")
    exit(1)

if output is True:
    keywordList.to_csv(fileName)
    quiet_print("File saved as " + fileName)

quiet_print(keywordList)
