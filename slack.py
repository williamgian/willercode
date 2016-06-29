#!/usr/bin/python

# Load libraries 
# Load wrapper from Slack API to translate 
import time
import daemon
from slackclient import SlackClient


def marcopolo_bot():
    # Insert API token from Slack
    # My token was disabled as soon as I uploaded it to Git, another token must be generated 
    token = 'xoxb-55268990450-WzfkM0A5ufihTTElZ8k6sC33'
    # Creating the slackclient object/instance 
    sc = SlackClient(token)
    # Connect to Slack
    if sc.rtm_connect():
        
        while True:
            # Read latest messages as long as connected to Slack
            rtm_responses = sc.rtm_read()
            # Check every instance of potential response and check for text response 
            for rtm_response in rtm_responses:
                if 'text' in rtm_response:
                    # If response is found as 'marco', call API function to respond with 'polo'
                    if rtm_response['text'] == 'marco':
                        sc.api_call(
                            "chat.postMessage", channel="marco-polo", text="polo",
                            username='pybot', icon_emoji=':robot_face:'
                        )
            
            time.sleep(1)

    else:
        quit()

# Run as daemon
with daemon.DaemonContext():
    marcopolo_bot()

