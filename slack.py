#!/usr/bin/python

import time
import daemon
from slackclient import SlackClient

def marcopolo_bot():
    token = 'xoxb-55268990450-WzfkM0A5ufihTTElZ8k6sC33'
    sc = SlackClient(token)
    if sc.rtm_connect():
        while True:
            rtm_responses = sc.rtm_read()
            for rtm_response in rtm_responses:
                if 'text' in rtm_response:
                    if rtm_response['text'] == 'marco':
                        sc.api_call(
                            "chat.postMessage", channel="marco-polo", text="polo",
                            username='pybot', icon_emoji=':robot_face:'
                        )

            time.sleep(1)

    else:
        quit()

with daemon.DaemonContext():
    marcopolo_bot()

