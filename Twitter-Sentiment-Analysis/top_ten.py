import sys
import json
import operator
import collections

def main():
    all_hash = collections.defaultdict(float)
    tf = open(sys.argv[1])
    for line in tf:
        tweet = json.loads(line, 'utf=8')
        if 'entities' in tweet.keys():
            hashtags = tweet['entities']['hashtags']
            for hash in hashtags:
                all_hash[unicode(hash['text'])] += 1.0
    sorted_hash = sorted(all_hash.iteritems(), key=operator.itemgetter(1),reverse=True)
    for key,value in sorted_hash[0:10]:
        print key, value

if __name__ == '__main__':
    main()