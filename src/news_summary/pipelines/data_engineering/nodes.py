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

def request_data(api_key: str, max_result: int=10):
    """Request news articles about movies and music in
    Australia, France, UK and USA in entertainement on
    newsdata.io

    Args:
        api_key (str): Api_key used to request
        max_result (int): Max number of articles to request
    Returns:
        response
    """
    api = NewsDataApiClient(apikey=api_key)
    response = api.news_api(
        q='movies,music',
        country="au,fr,gb,us",
        category="entertainment",
        language="en",
        max_result=max_result,
    )
    return response
