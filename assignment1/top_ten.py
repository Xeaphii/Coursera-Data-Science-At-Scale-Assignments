import sys
import json
from pprint import pprint
import operator

def hw():
		print 'Hello, world!'

def lines(fp):
		print str(len(fp.readlines()))

def main():
	# sent_file = open(sys.argv[1])
	 tweet_file = open(sys.argv[1])

	 
	 #temp_json = json.loads(tweet_file)
	 tweets_data = []
	 for line in tweet_file:
			tweets_data.append(json.loads(line))

			#afinnfile = open("AFINN-111.txt")

			#print line

	 #pprint(tweets_data)
	# hw()
	 

	 hash_tags = {}
	 for tweets in tweets_data:
		if 'entities' in tweets and 'hashtags' in tweets['entities']:
		   for hashtag in tweets['entities']['hashtags']:
			  if hashtag['text'].encode('utf-8').lower().strip() in hash_tags:
				 hash_tags[hashtag['text'].encode('utf-8').lower().strip()] +=1
			  else :
				 hash_tags[hashtag['text'].encode('utf-8').lower().strip()] =1
				 
				 

	 #pprint(sorted(short_listed_countries.iteritems(), key=lambda item: -item[1])[:1])
	#print(max(short_listed_countries.iteritems(), key=operator.itemgetter(1))[0].strip('"\''))
	 hash_tags = sorted(hash_tags.iteritems(), key=lambda item: -item[1])[:30]
	 for id,val in hash_tags:
	 	print (id + ' ' + str(val))
	 #pprint()
	# pprint(states_data)
	 
	 #pprint(sentiment_scores)
	 #print type(scores)
	# print scores.items() # Print every (term, score) pair in the dictio nary

if __name__ == '__main__':
		main()
