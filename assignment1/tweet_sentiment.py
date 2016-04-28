import sys
import json
from pprint import pprint

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
   sent_file = open(sys.argv[1])
   tweet_file = open(sys.argv[2])

   #lines(sent_file)
   #lines(tweet_file)
 
   scores = {} # initialize an empty dictionary
   for line in sent_file:
   	#  print line
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.


   
   #temp_json = json.loads(tweet_file)
   tweets_data = []
   for line in tweet_file:
    	tweets_data.append(json.loads(line))

      #afinnfile = open("AFINN-111.txt")

      #print line

   #pprint(tweets_data)
  # hw()
   

   sentiment_score = 0
   sentiment_scores = []
   for tweets in tweets_data:
	   if 'text' in tweets:
	      #tweets = tweets_data[5]
	      for word in tweets['text'].split(" "):
	         if word.encode('utf-8').lower() in scores.keys():
	            score += scores[word.encode('utf-8').lower()]
	   pprint(score)
	   sentiment_scores.append(score)
	   score = 0
   #pprint(tweets['text'])
   #pprint(score)
   
   #pprint(sentiment_scores)
   #print type(scores)
  # print scores.items() # Print every (term, score) pair in the dictio nary

if __name__ == '__main__':
    main()
