import json

def findNext(text_file,author, parent, left):
    for comment in left:
        if comment["parent_id"][3:] == parent["id"] and comment["author"] == author:
            with open(text_file, "a") as file:
                file.write(comment["author"] + ": " + str(comment["body"]).replace('\n', '').replace('\r', ' ') + "\n")
            findNext(text_file, parent["author"], comment, left)
            break

def process(list, number):
    print len(list)
    post = list[0]
    comments = list[1:]
    print post["id"]
    count = 0

    commentids = []
    for comment in comments:
        commentids.append(comment["id"])
    print commentids

    level1 = []
    level2 = []
    notlevel1 = []
    notlevel2 = []

    for comment in comments:
        if comment["parent_id"][3:] not in commentids:
            level1.append(comment)
        else:
            notlevel1.append(comment)
    for comment in level1:
        commentids.append(comment["id"])
    for comment in notlevel1:
        if comment["parent_id"][3:] not in commentids:
            notlevel2.append(comment)
        else:
            level2.append(comment)

    for comment in level2:
        b = comment["author"]
        a = "none"
        for parent in level1:
            if comment["parent_id"][3:] == parent["id"]:
                a = parent["author"]
                break

        print "Creating file: " + "reddit" + "{:0>4d}".format(number+count)+".txt"
        with open("reddit" + "{:0>4d}".format(number+count)+".txt", "w") as file:
            file.write(post["title"].replace('\n', ' ')+"\n")
            file.write(post["url"]+"\n")
            file.write(parent["author"]+": "+str(parent["body"]).replace('\n', '').replace('\r', ' ')+"\n")
            file.write(comment["author"]+": "+str(comment["body"]).replace('\n', '').replace('\r', ' ')+"\n")
        findNext("reddit" + "{:0>4d}".format(number+count)+".txt", parent["author"], comment, notlevel2)

        count += 1









    return