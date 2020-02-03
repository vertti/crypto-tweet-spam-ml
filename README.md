# crypto-tweet-spam-ml

## Fetching data

Install `twurl` and `jq`. Authenticate with Twitter using:

```
twurl authorize --bearer --consumer-key your-consumer-key --consumer-secret your-consumer-secret
```

then fetch tweets about different crypto currencies ($ETH, $NEO, $VET etc.) by running:

```
./load-tweet-set.sh
```

This will do multiple Twitter search queries and convert the results to JSONL files where each line contains one tweet and it's metadata (like the retweet count of that tweet).

## Training with Prodigy

Install Prodigy.

Install SpaCy language model with:

```
python -m spacy download en_core_web_sm
```

and start training with seed words defined in `spam-seeds.jsonl` with:

```
prodigy textcat.teach twitter_spam en_core_web_sm ./alltweets.jsonl --label SPAM --patterns ./spam-seeds.jsonl
```

When you've done enough teaching, quit Prodigy and run training:

```
prodigy textcat.batch-train twitter_spam en_core_web_sm --output twitter-spam-model --eval-split 0.2
```

This will create training and evaluation sets and SpaCy model in `twitter-spam-model` folder.
