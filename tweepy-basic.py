import tweepy

# Authenticate to Twitter

CONSUMER_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
CONSUMER_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_TOKEN_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("//////////////////////////Authentication OK \n")
except:
    print("Error during authentication")

U_NAME="alferdez"
user = api.get_user(U_NAME)

print("\n //////////////////////////User details:")
print(user.name)
print(user.description,)
print(user.location)

print("\n //////////////////////////Last 3 Followers:")
for follower in user.followers(count=3):
    print(follower.name)
	

print("\n //////////////////////////Last 3 Tweets:")
stuff = api.user_timeline(screen_name = U_NAME, count = 3, include_rts = True)

for status in stuff:
    print (status.text)
