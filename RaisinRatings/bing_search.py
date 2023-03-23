import json
import requests


def read_bing_key():
    bing_api_key = None
    try:
        with open('bing.key', 'r') as f:
            bing_api_key = f.readline().strip()
    except:
        try:
            with open('../bing.key') as f:
                bing_api_key = f.readline().strip()
        except:
            raise IOError('bing.key file not found')

    if not bing_api_key:
        raise KeyError('Bing key not found')
    return bing_api_key


def run_query(search_terms):
    # Construct a request
    subscription_key = read_bing_key()
    search_url = "https://api.bing.microsoft.com/v7.0/search"
    mkt = 'en-US'
    params = {'q': search_terms, 'mkt': mkt}
    headers = {'Ocp-Apim-Subscription-Key': subscription_key}

    # Call the API
    try:
        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()
        search_results = response.json()
        results = []
        for result in search_results['webPages']['value']:
            results.append({
                'title': result['name'],
                'link': result['url'],
                'summary': result['snippet'],
            })
        return results, search_terms  # s_terms included to allow it to remain in search box after submitting form.
    except Exception as ex:
        raise ex
