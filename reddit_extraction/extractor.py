import praw
import json


# Define authentication details
CLIENT_ID = 'ZuErHiTiPHWDiQ'
CLIENT_SECRET = 'SaC0IWN8JNnuqWy-uv-h0FPytGM'
USERNAME = 'ME-64'
PASSWORD = '!NN0V4T10Nredd'
USER_AGENT= 'sub-reccomender/0.0.1 by ME-64'

# Initiate instance of reddit object
reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                    password=PASSWORD, username = USERNAME,
                    user_agent=USER_AGENT)

class Reddit(object):

    def __init__(self, client_id, client_secret, password, username, user_agent):
        self._reddit = praw.Reddit(
                client_id=client_id,
                client_secret=client_secret,
                password=password,
                username=username,
                user_agent=user_agent
                )

    def get_qa(self, subreddit, sort):

        self._subreddit = self._reddit.subreddit(subreddit)

        if sort == 'controversial':
            self._subreddit = self._subreddit.controversial(limit=1000)
        elif sort == 'top':
            self._subreddit = self._subreddit.top(limit=1000)
        elif sort == 'hot':
            self._subreddit = self._subreddit.hot(limit=1000)
        elif sort == 'rising':
            self._subreddit = self._subreddit.rising(limit=1000)

        qna = {}
        post_count = 0

        for submission in self._subreddit:
            post_count += 1
            if ((submission.title[-1] == '?') 
            & (submission.id not in qna) & 
            (submission.is_self == True)):
                submission.comment_sort = 'best'
                qna[submission.id] = {}
                qna[submission.id]['question'] = submission.title
                qna[submission.id]['score'] = submission.score
                qna[submission.id]['ups'] = submission.ups
                qna[submission.id]['downs'] = submission.downs
                qna[submission.id]['created_datetime'] = submission.created_utc
                for comment in submission.comments:
                    if len(comment.body) <= 280:
                        qna[submission.id]['answer'] = comment.body
                        break

                if len(qna[submission.id].get('answer', '')) == 0:
                    del qna[submission.id]
                else:
                    print('found new Q! - ' + submission.title)

            print('posts parsed = ' + str(post_count))
            print('Qs found = ' + str(len(qna.keys())))
            print('=====')

        return qna


def main():
    reddit = Reddit(CLIENT_ID, CLIENT_SECRET, PASSWORD, USERNAME, USER_AGENT)
    
    subreddits = ['vegan', 'askvegans', 'debateavegan']
    sorts = ['controversial', 'top', 'hot', 'rising']
    final_qna = {}
    for subreddit in subreddits:
        for sort in sorts:
            temp_dict = reddit.get_qa(subreddit, sort)

            final_qna[subreddit + '_' + sort] = temp_dict

    with open('final_answers.json', 'w') as json_file:
        json.dump(final_qna, json_file)

if __name__ == '__main__':
    main()
