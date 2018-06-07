import json
from anytree import Node, RenderTree

def chains(list, parent):

    lists = []
    replies = []
    for comment in list:
        if comment["parent_id"] == parent:
            replies.append(comment)



    return lists

def process(list, number):

    post = list[0]
    comments = list[1:]

    cChains  = chains(comments, post["name"])

    preplies = []
    for comment in comments:
        if comment["parent_id"] == post["name"]:
            preplies.append(comment)

    rpreplies = []
    for comment in comments:
        if comment["parent_id"] ==


    return