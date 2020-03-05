import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Crypto Tweet Spam</h1><p>More stuff soon</p>"

@app.route('/coin/<coin>')
def show_user_profile(coin):
    # show the user profile for that user
    return 'Get coin stuff for %s' % flask.escape(coin)

app.run()