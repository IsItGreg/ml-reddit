import json
from process import process
import os
import pandas as pd


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

    POSTS = "RS_2006-02"
    COMMENTS = "RC_2006-02"


    postList = []

    with open(POSTS, "r") as postFile:
        for line in postFile:
            parsedPost = json.loads(line)
            postList.append([parsedPost])

    with open(COMMENTS) as commFile:
        for comment in commFile:
            parsedComm = json.loads(comment)
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

