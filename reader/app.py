import flask
from reader import get_tweets

app = flask.Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "<h1>Crypto Tweet Spam</h1><p>More stuff soon</p>"


@app.route("/coin/<coin>")
def get_coin_tweets(coin):
    print(f"Getting coin tweets for {coin}")
    return flask.jsonify(get_tweets(flask.escape(coin)))


app.run(debug=True, host="0.0.0.0")
