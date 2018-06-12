import json
from process import process
import os
import pandas as pd
import bz2

def createDir(dir):
    try:
        os.mkdir(dir)
        return True
    except:
        return False

def main():

    dir = "redditFiles"
    createDir(dir)
    data = []

    POSTS = "RS_2006-02.bz2"
    COMMENTS = "RC_2006-02.bz2"
    posts = bz2.BZ2File(POSTS).readlines()
    comments = bz2.BZ2File(COMMENTS).readlines()

    postList = []

    for line in posts:
        parsedPost = json.loads(line.decode('utf-8'))
        postList.append([parsedPost])

    for comment in comments:
        parsedComm = json.loads(comment.decode('utf-8'))
        for list in postList:
            if parsedComm["link_id"] == list[0]["name"]:
                list.append(parsedComm)
                break

    count = 0
    for list in postList:
        processed = process(list, count, dir)
        if processed[0] != 0:
            count += processed[0]
            data.extend(processed[1])


    df = pd.DataFrame(data, columns=["Post Title", "Username A", "Username B", "Post URL", "Comments in Chain"])
    df.to_csv(os.path.join(dir, "reddit_metadata.csv"), sep='\t', encoding=('utf-8'))

    return


if __name__ == "__main__":
    main()

