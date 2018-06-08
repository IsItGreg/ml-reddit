from alphabet_detector import AlphabetDetector
import os

def fixLine(str):
    newstr = ""
    quote = False
    for line in str.splitlines(True):
        if line[:4] != '&gt;':
            if quote == True:
                newstr = newstr.rstrip() + '">>'
            newstr += line
            quote = False
        else:
            if quote == False:
                newstr += '<<You said "'
            newstr += line[4:]
            quote = True
    return ' '.join(newstr.split())+"\n"

def findNext(text_file,author, notbody, parent, left):
    for comment in left:
        if comment["parent_id"][3:] == parent["id"] and comment["author"] == author and fixLine(comment["body"]) != notbody:
            with open(text_file, "a") as file:
                file.write(comment["author"]+ ": " +fixLine(comment["body"]))
            return  findNext(text_file, parent["author"], fixLine(parent["body"]), comment, left) + 1
    return 0

def process(list, number, dir):
    ad = AlphabetDetector()
    nullreturn = (0, [])
    post = list[0]
    comments = list[1:]
    count = 0
    data = []
    if not ad.only_alphabet_chars(post["title"], "LATIN"):
        print(post["title"])
        return nullreturn

    if len(comments) < 2:
        return nullreturn

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
    if len(level2) < 1:
        return nullreturn

    for comment in level2:
        for parent in level1:
            if comment["parent_id"][3:] == parent["id"]:
                break
        if comment["parent_id"][3:] == parent["id"] and comment["body"] != "[deleted]":
            print ("Creating file: reddit" + "{:0>4d}".format(number+count)+".txt")
            with open(os.path.join(dir, "reddit" + "{:0>4d}".format(number+count)+".txt"), "w") as file:
                file.write(post["title"].replace('\n', ' ').replace('\r', ' ')+"\n")
                file.write(post["url"]+"\n")
                file.write(parent["author"]+": "+fixLine(parent["body"]))
                file.write(comment["author"]+": "+fixLine(comment["body"]))
            numcomments = findNext(os.path.join(dir, "reddit" + "{:0>4d}".format(number+count)+".txt"), parent["author"], fixLine(parent["body"]), comment, notlevel2) + 2
            data.append([post["title"].replace(",", ""), parent["author"], comment["author"], "https://www.reddit.com" + post["permalink"], numcomments])
            count += 1
    return (count, data)
