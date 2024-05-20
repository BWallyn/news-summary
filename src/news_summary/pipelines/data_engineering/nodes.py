"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.19.5
"""
# =================
# ==== IMPORTS ====
# =================

from newsdataapi import NewsDataAPIClient

# ===================
# ==== FUNCTIONS ====
# ===================

def request_data(api_key: str):
    """Request news articles about movies and music in
    Australia, France, UK and USA in entertainement on
    newsdata.io

    Args:
        api_key (str): Api_key used to request
    """
    api = NewsDataApiClient(apikey=api_key)
    response = api.news_api(
        q='movies,music',
        country="au,fr,gb,us",
        category="entertainment",
        language="en",
    )
    return response
