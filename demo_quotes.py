import argparse

from tradeking import tradeking

CONSUMER_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
CONSUMER_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
OAUTH_TOKEN_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
OAUTH_TOKEN_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'


def main(symbol, verbose):
    tk = tradeking.TradeKing(CONSUMER_KEY,
                             CONSUMER_SECRET,
                             OAUTH_TOKEN_KEY,
                             OAUTH_TOKEN_SECRET)

    symbol = symbol.upper()
    quote = tk.quote(symbol)

    if not verbose:
        print "%s price: %s" % (symbol, quote["last"])
    else:
        print "%s quote: %s" % (symbol, quote)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("symbol", type=str,
                        help="display stock quote for a symbol")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="increase output verbosity")
    args = parser.parse_args()
    main(args.symbol, args.verbose)
