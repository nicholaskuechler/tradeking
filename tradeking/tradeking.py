import oauth2 as oauth
import json


class TradeKing(object):

    TRADEKING_API_URL = "https://api.tradeking.com/v1"

    def __init__(self,
                 consumer_key,
                 consumer_secret,
                 oauth_token_key,
                 oauth_token_secret):

        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.oauth_token_key = oauth_token_key
        self.oauth_token_secret = oauth_token_secret

        self.consumer = oauth.Consumer(key=consumer_key,
                                       secret=consumer_secret)
        self.token = oauth.Token(key=oauth_token_key,
                                 secret=oauth_token_secret)
        self.client = oauth.Client(self.consumer,
                                   token=self.token)

    def quote(self, symbol):
        url = "%s/market/ext/quotes.json?" \
              "symbols=%s" % (self.TRADEKING_API_URL, symbol)
        resp, content = self.client.request(url, "GET")
        data = json.loads(content)
        quote = data["response"]["quotes"]["quote"]
        return quote
