import sys
import json
from pprint import pprint

def hw():
		print 'Hello, world!'

def lines(fp):
		print str(len(fp.readlines()))

def main():
	 tweet_file = open(sys.argv[1])
	 
	 #temp_json = json.loads(tweet_file)
	 tweets_data = []
	 for line in tweet_file:
			tweets_data.append(json.loads(line))

	 

	 total_count = 0
	 for tweets in tweets_data:
			if 'text' in tweets:
				 total_count += len(tweets['text'].split())


	 sentiments_count = {}
	 for  tweets in tweets_data:
		 if 'text' in tweets:
				for word in tweets['text'].split(" "):
				 word = word.encode('utf-8').lower()
				 if  word 	 in sentiments_count.keys():
						sentiments_count[word] = sentiments_count[word] +1
				 else:
						sentiments_count[word] = 1				 
	 
	 for key, value in sentiments_count.iteritems():
			print(key + ' ' + str((float(value)/float(total_count))))
	 #pprint(tweets['text'])
	 #pprint(total_count)
	 
	 #pprint(sentiment_scores)
	 #print type(scores)
	# print scores.items() # Print every (term, score) pair in the dictio nary

if __name__ == '__main__':
		main()
