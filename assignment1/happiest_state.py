import sys
import json
from pprint import pprint
import operator

def hw():
		print 'Hello, world!'

def lines(fp):
		print str(len(fp.readlines()))

def main():
	 sent_file = open(sys.argv[1])
	 tweet_file = open(sys.argv[2])
	 states = {
				'AK': 'Alaska',
				'AL': 'Alabama',
				'AR': 'Arkansas',
				'AS': 'American Samoa',
				'AZ': 'Arizona',
				'CA': 'California',
				'CO': 'Colorado',
				'CT': 'Connecticut',
				'DC': 'District of Columbia',
				'DE': 'Delaware',
				'FL': 'Florida',
				'GA': 'Georgia',
				'GU': 'Guam',
				'HI': 'Hawaii',
				'IA': 'Iowa',
				'ID': 'Idaho',
				'IL': 'Illinois',
				'IN': 'Indiana',
				'KS': 'Kansas',
				'KY': 'Kentucky',
				'LA': 'Louisiana',
				'MA': 'Massachusetts',
				'MD': 'Maryland',
				'ME': 'Maine',
				'MI': 'Michigan',
				'MN': 'Minnesota',
				'MO': 'Missouri',
				'MP': 'Northern Mariana Islands',
				'MS': 'Mississippi',
				'MT': 'Montana',
				'NA': 'National',
				'NC': 'North Carolina',
				'ND': 'North Dakota',
				'NE': 'Nebraska',
				'NH': 'New Hampshire',
				'NJ': 'New Jersey',
				'NM': 'New Mexico',
				'NV': 'Nevada',
				'NY': 'New York',
				'OH': 'Ohio',
				'OK': 'Oklahoma',
				'OR': 'Oregon',
				'PA': 'Pennsylvania',
				'PR': 'Puerto Rico',
				'RI': 'Rhode Island',
				'SC': 'South Carolina',
				'SD': 'South Dakota',
				'TN': 'Tennessee',
				'TX': 'Texas',
				'UT': 'Utah',
				'VA': 'Virginia',
				'VI': 'Virgin Islands',
				'VT': 'Vermont',
				'WA': 'Washington',
				'WI': 'Wisconsin',
				'WV': 'West Virginia',
				'WY': 'Wyoming'
	 }
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
	 states_data = {}
	 for tweets in tweets_data:
			if 'text' in tweets:
				 #tweets = tweets_data[5]
				 for word in tweets['text'].split(" "):
						if word.encode('utf-8').lower() in scores.keys():
							 score += scores[word.encode('utf-8').lower()]
			
				 if 'user' in tweets:
						#pprint(tweets['user']['location'])
						if tweets['user']['location'].rsplit(' ', 1)[-1].encode('utf-8').lower().strip() in states_data.keys():
							 states_data[tweets['user']['location'].rsplit(' ', 1)[-1].encode('utf-8').lower().strip()] += score
						else:
							 states_data[tweets['user']['location'].rsplit(' ', 1)[-1].encode('utf-8').lower().strip()] = score
			sentiment_scores.append(score)
			#pprint(score)
			score = 0

		#pprint(tweets['text'])
	 short_listed_countries = {}

	 for key,value in states_data.iteritems():
			if key.upper() in states:
				 short_listed_countries [key] = value
				 

	 #pprint(sorted(short_listed_countries.iteritems(), key=lambda item: -item[1])[:1])
	 	print(max(short_listed_countries.iteritems(), key=operator.itemgetter(1))[0].strip('"\''))
	# pprint(states_data)
	 
	 #pprint(sentiment_scores)
	 #print type(scores)
	# print scores.items() # Print every (term, score) pair in the dictio nary

if __name__ == '__main__':
		main()
