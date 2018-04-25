from pybacklog import BacklogClient
import re
import os
import json

client = BacklogClient(os.environ['ID'], os.environ['API_KEY'])

def comments(result):
    comment = ''
    comment += "''ID:'' {}\n".format(result['commits'][0]['id'])
    comment += "''Date:'' {}\n".format(result['commits'][0]['timestamp'])
    comment += "''URL:'' {}\n".format(result['commits'][0]['url'])
    comment += "''Author:'' {}\n".format(result['commits'][0]['author']['name'])
    comment += "{code}\n"
    comment += "{}\n".format(result['commits'][0]['message'])
    comment += "{/code}\n"
    return comment

def ticket_number(result):
    m = re.match(r"(#)((.*?)-[0-9]{1,})", result['commits'][0]['message'])
    if m != None:
        return m.group(2)
    else:
        print("not match")

# add comment
def lambda_handler(event, context):
    try:
        print(event)
        return client.add_issue_comment(ticket_number(event), comments(event))
    except Exception as e:
        print(e)
        raise e