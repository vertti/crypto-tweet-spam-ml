#!/usr/bin/env python3

from aws_cdk import core

from infra.crypto_tweet_spam_ml_stack import CryptoTweetSpamMlStack


app = core.App()
CryptoTweetSpamMlStack(app, "crypto-tweet-spam-ml")

app.synth()
