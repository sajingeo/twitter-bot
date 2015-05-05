from twitter import *
import subprocess
import time
import re

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
old_id = 0
cmd_line_sound = ['mplayer','-ao','-really-quite','-noconsolecontrols']
cmd_line_motor = ['python','motor.py']
while (True):
	time_line = t.search.tweets(q='#pycon')
	tweet_id = time_line['statuses'][0]['id']
	if (old_id != tweet_id):
		old_id = tweet_id
		text = time_line['statuses'][0]['text']
		text = text.encode("ascii","ignore").rstrip()
		text = text.replace ("#", " hash tag ")
		text = text = re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)
		text = text.replace(" ", "+")
		text = text.replace("\n","")
		encoded_url = 'http://tts-api.com/tts.mp3?q=' + text
		cmd_line.append(encoded_url)
		#debug
		print cmd_line
		## motor = subprocess.Popen(cmd_line_motor)
		## sound = subprocess.Popen(cmd_line)
		## sound.wait()
		## motor.kill()
		time.sleep(60)
# Search for the latest tweets about #pycon
#t.search.tweets(q="#pycon")
