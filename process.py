import json
from langdetect import detect

def findNext(text_file,author, parent, left):
    for comment in left:
        if comment["parent_id"][3:] == parent["id"] and comment["author"] == author:
            with open(text_file, "a") as file:
                file.write(comment["author"].encode('utf-8') + ": " + str(comment["body"].encode('utf-8')).replace('\n', '').replace('\r', ' ') + "\n")
            findNext(text_file, parent["author"], comment, left)
            break

def process(list, number):
    #print len(list)
    post = list[0]
    comments = list[1:]
    #print post["id"]
    count = 0
    if detect(post["title"]) != "en":
        0#print post["title"]
        #return 0

    if len(comments) < 3:
        return 0

    commentids = []
    for comment in comments:
        commentids.append(comment["id"])

    level1 = []
    level2 = []
    notlevel1 = []
    notlevel2 = []

    for comment in comments:
        if comment["parent_id"][3:] not in commentids:
            level1.append(comment)
        else:
            notlevel1.append(comment)

    commentids = []
    for comment in level1:
        commentids.append(comment["id"])

    for comment in notlevel1:
        if comment["parent_id"][3:] not in commentids:
            notlevel2.append(comment)
        else:
            level2.append(comment)

    for comment in level2:
        for parent in level1:
            if comment["parent_id"][3:] == parent["id"]:
                break
        if comment["parent_id"][3:] == parent["id"]:
            print "Creating file: " + "reddit" + "{:0>4d}".format(number+count)+".txt"
            with open("reddit" + "{:0>4d}".format(number+count)+".txt", "w") as file:
                file.write(post["title"].encode('utf-8').replace('\n', ' ').replace('\r', ' ')+"\n")
                file.write(post["url"]+"\n")
                file.write(parent["author"].encode('utf-8')+": "+str(parent["body"].encode('utf-8')).replace('\n', '').replace('\r', ' ')+"\n")
                file.write(comment["author"].encode('utf-8')+": "+str(comment["body"].encode('utf-8')).replace('\n', '').replace('\r', ' ')+"\n")
            findNext("reddit" + "{:0>4d}".format(number+count)+".txt", parent["author"], comment, notlevel2)
            count += 1

    return count