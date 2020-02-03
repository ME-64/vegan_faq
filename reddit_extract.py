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

# Select required subreddit
askvegan = reddit.subreddit('askvegans')

# Empty dict for question / answer pairs
qaa = {}

sub_count = 0
del_count = 0

for submission in askvegan.top():
    sub_count += 1
    # Checking to see if there is a clear question
    if (submission.title[-1] == '?') & (submission.title not in qaa):
        # Retrive the best comment and append to the dictionary
        submission.comment_sort = 'best'
        qaa[submission.title] = {}
        qaa[submission.title]['score'] = submission.score
        qaa[submission.title]['ups'] = submission.ups
        qaa[submission.title]['downs'] = submission.downs
        qaa[submission.title]['created_datetime'] = submission.created_utc
        for comment in submission.comments:
            if len(comment.body) <= 280:
                qaa[submission.title]['answer'] = comment.body
                break
        # delete the title / submission if no valid response is found in comments
        if len(qaa[submission.title].get('answer', '')) == 0:
            del qaa[submission.title]
            del_count = del_count + 1 

    print('sub count = ' + str(sub_count))
    print('del count = ' + str(del_count))
    print('Q count = ' + str(len(qaa.keys())))

with open('answers.json', 'w') as json_file:
    json.dump(qaa, json_file)



