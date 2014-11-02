import oauth2 as oauth
import json

# Need to register with Twitter to get consumer and access keys
CONSUMER_KEY = 'need'
CONSUMER_SECRET = 'need'

SEARCH_URL = "https://api.twitter.com/1.1/search/tweets.json"
GEOCODE_URL = "https://api.twitter.com/1.1/geo/search.json"

ACCESS_KEY = 'need'
ACCESS_SECRET = 'need'

def oauth_req(url, key, secret, http_method="GET", post_body=None, http_headers=None):
    
    consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth.Token(key=key, secret=secret)
    client = oauth.Client(consumer, token)
    #print url

    resp, content = client.request(
        url,
        method=http_method,
        body=post_body,
        headers=http_headers,
        force_auth_header=True
    )
    return content

def oauth_get_req_with_params(url,key,secret,params):

    url_with_params = url + "?"
    for params_key in params.keys():
        url_with_params += params_key + "=" + str(params[params_key]) + "&"
    # Remove extraneous '?' or '&'
    url_with_params = url_with_params[:-1]
    return oauth_req(url_with_params,key,secret)

## Search Tweets near NC State Univeristy

def getLatitudeFromTweetParameters(tweet_search_params):
    geocode_string = tweet_search_params["geocode"]
    geocode_components = geocode_string.split(',')
    return float(geocode_components[0])

def setLatitudeForTweetParameters(tweet_search_params, latitude):
    geocode_string = tweet_search_params["geocode"]
    geocode_components = geocode_string.split(',')
    geocode_components[0] = str(latitude)
    tweet_search_params["geocode"] = ','.join(geocode_components)

def getLongitudeFromTweetParameters(tweet_search_params):
    geocode_string = tweet_search_params["geocode"]
    geocode_components = geocode_string.split(',')
    return float(geocode_components[1])

def setLongitudeForTweetParameters(tweet_search_params, longitude):
    geocode_string = tweet_search_params["geocode"]
    geocode_components = geocode_string.split(',')
    geocode_components[1] = str(longitude)
    tweet_search_params["geocode"] = ','.join(geocode_components)

tweets_search_params = {
    'q' : "%20", # bit if a hack to search all tweets (that contain a space), might need to adjust this if we the rate max
    'geocode' : "35.784663,-78.682095,5km", # within 5km of NC State center point
    'result_type' : 'recent'
}

# Get JSON response
tweets_search_results_json_str = oauth_get_req_with_params(
    SEARCH_URL,ACCESS_KEY,ACCESS_SECRET,tweets_search_params
)
