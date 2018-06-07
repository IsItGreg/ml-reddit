import json

def main():

    testComment = '{"created_utc":1138752114,"author_flair_css_class":null,"score":0,"ups":0,"subreddit":"reddit.com","stickied":false,"link_id":"t3_15xh","subreddit_id":"t5_6","body":"THAN the title suggests.  Whoops.","controversiality":1,"retrieved_on":1473820870,"distinguished":null,"gilded":0,"id":"c166b","edited":false,"parent_id":"t3_15xh","author":"gmcg","author_flair_text":null}'
    testPost = '{"media_embed":{},"selftext":"","stickied":false,"id":"5y9qm","subreddit":"reddit.com","author_flair_text":null,"is_self":false,"author":"moe","from":null,"created":1140998384,"over_18":false,"from_kind":null,"link_flair_text":null,"score":21,"quarantine":false,"media":null,"hide_score":false,"link_flair_css_class":null,"ups":21,"subreddit_id":"t5_6","archived":true,"author_flair_css_class":null,"distinguished":null,"url":"http://www.webdevout.net/firefox_myths.php","gilded":0,"from_id":null,"downs":0,"retrieved_on":1443014580,"title":"Firefox Myths","domain":"webdevout.net","thumbnail":"default","permalink":"/r/reddit.com/comments/5y9qm/firefox_myths/","edited":false,"secure_media_embed":{},"secure_media":null,"num_comments":5,"created_utc":"1140998384","saved":false,"name":"t3_5y9qm"}'


    parsedPost = json.loads(testPost)
    print parsedPost["name"]

    0

    return


if __name__ == "__main__":
    main()

