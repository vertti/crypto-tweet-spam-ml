token=$1

parse () {
   jq -c '.statuses[] | { text: .full_text, meta: { retweets: .retweet_count, favorites: .favorite_count, user_id: .user.id_str, followers: .user.followers_count }}'
}

fetch () {
   twurl --bearer -c $2 "/1.1/search/tweets.json?q=\$${1}&tweet_mode=extended&result_type=recent&count=100&until=2020-01-29" > ${1}tweets.json
}

declare -a arr=("eth" "btc" "bnb" "etc" "vet" "neo" "ada" "xrp")

rm alltweets.jsonl

## now loop through the above array
for i in "${arr[@]}"
do
   echo "Fetching tweets about $i"
   fetch $i $token
   echo "Parsing tweets about $i"
   cat ${i}tweets.json | parse >> alltweets.jsonl
done

