tradeking
=========

TradeKing API

A Python wrapper for <a href="https://www.tradeking.com/">TradeKing</a> API

## Author

<a href="http://www.nicholaskuechler.com/">Nicholas Kuechler</a>

## Requirements

* oauth2
* argparse (for the demo quotes example)

You can install them with pip:

    pip install oauth2
    pip install argparse

## Demo

Edit demo_quotes.py and input your TradeKing API credentials.

Run the demo:

    python demo_quotes.py QQQ

## Use TradeKing API in your application

    from tradeking import tradeking
    
    CONSUMER_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    CONSUMER_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    OAUTH_TOKEN_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    OAUTH_TOKEN_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    
    tk = tradeking.TradeKing(CONSUMER_KEY,
                             CONSUMER_SECRET,
                             OAUTH_TOKEN_KEY,
                             OAUTH_TOKEN_SECRET)
