import sys
import json
import string

from collections import defaultdict

def data_clean(word):
    exclude = set(string.punctuation)
    word = ''.join(ch for ch in word.lower() if ch not in exclude)
    return word

def inc_count(dct,tweet):
	for word in tweet.split():
		if word in dct:
			dct[word] += 1
		else:
			dct[word] = 1


def main():
	dct = defaultdict()
	tweet_file = open(sys.argv[1])
	for line in tweet_file:
		d = json.loads(line.encode('utf8'))
		if 'text' in d.keys():
			inc_count(dct,data_clean(d['text'].encode('utf8')))

	all_occ = sum(dct.values())
	for word in dct.keys():
	    try:
                word.decode('utf-8')
                if (all_occ != 0):
		    print word,dct[word]/float(all_occ)
            
            except UnicodeError:
	        n = 2


if __name__ == '__main__':
    main()
    
    