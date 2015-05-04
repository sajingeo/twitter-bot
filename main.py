from twitter import *
token = ''
token_key = ''
con_secret = ''
con_secret_key = ''
t = Twitter(auth=OAuth(token, token_key, con_secret, con_secret_key))

## this is the users time line -everything he follows
## time_line = t.statuses.home_timeline()

## this is personal tweets time line
## time_line = t.statuses.user_timeline(screen_name="sajingeo")

## this is to search for hash tag
time_line = t.search.tweets(q="#pycon")

print time_line['statuses'][0]['text']
# Search for the latest tweets about #pycon
#t.search.tweets(q="#pycon")
