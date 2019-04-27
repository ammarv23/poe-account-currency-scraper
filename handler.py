"""
Given an account name and a shard_id, make a request to the bulk stash tab API of Path of Exile

http://api.pathofexile.com/public-stash-tabs

If the account is not found in the payload, update the scheduler with the next invocation and shardId and return,
if it is, then update the account in the database and return


"""

import requests
import json

POE_URL = "http://api.pathofexile.com/public-stash-tabs"


def hello(event, context):
    r = requests.get(url=POE_URL)
    body = json.loads(r.text)

    matches = filter(lambda x: x["accountName"] == event["account"], body["stashes"])

    count = sum(1 for _ in matches)

    return "Found " + str(count) + " matches for account name " + event["account"]
