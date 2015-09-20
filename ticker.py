'''
goal: take stock ticker symbols from user & return last price
adapted from https://github.com/dotslash/Projects/blob/master/solutions/quotes.py

1. ask user for ticker symbol input (quotes)
2. clean quotes by removing trailing whitespace
3. convert quotes into format to put into SQL IN()
4. pass quotes into YQL query to get finance data from yahoo.finance.quotes
5. url-encode YQL query
6. pass query YQL query into url
7. open url query to get JSON results (res)
8. parse JSON into dictionary type using json.loads()
9. select relevant parts of result set using dictionary index
10. print formatted result using json.dumps() 
'''

import urllib   # https://docs.python.org/2/library/urllib.html
import sys      # https://docs.python.org/2/library/sys.html
import json     # https://docs.python.org/2/library/json.html

url = 'http://query.yahooapis.com/v1/public/yql?{0}&format=json'
query = '''select LastTradePriceOnly,symbol,Name
           from yahoo.finance.quotes
           where symbol in ({0})'''

#pass arguments through command line in quotation marks
#quotes = sys.argv[1]

## user input:
quotes = raw_input("what ticker symbols are you interested in?")

# 
# '   a   '.strip() results in 'a' -- removes characters from before/after (can specify which character)
# '-'.join("a","b") results in 'a-b'
# 'a,b'.split(',') results in ['a','b'] -- delimiter

# original approach:
# quotes = ','.join(('"' + q.strip() + '"' for q in quotes.split(',')))

quotes = quotes.split(',')	# split input into list based on comma delimiter

quotes_clean = []
for q in quotes:
	q = q.strip()		# remove whitespace
	q = '"'+q+'"'		# add quotation marks
	quotes_clean.append(q)			# add cleaned symbols to list
quotes = ','.join(quotes_clean)	# combine list items with comma

# https://pyformat.info/
# 'hello {1}'.format('joe','bob') = 'hello bob'
# same as: 'hello %s' %('bob')

query = query.format(quotes)    # pass quotes string into query

# url escaping resources - http://archive.oreilly.com/pub/h/476
# yql guide - https://developer.yahoo.com/yql/guide/two-minute-tutorial.html

query = urllib.urlencode({'q': query, 'env': 'http://datatables.org/alltables.env'}) # url escaping query and datatables.org

url = url.format(query) # pass query into url

res = urllib.urlopen(url).read() # open url for reading to get JSON string

# json examples - https://docs.python.org/2/library/json.html
# .loads() parses json into dictionary type
# 'results' is dictionary within 'query' dictionary
res = json.loads(res)['query']['results'] 


# .dumps() for pretty printing of dictionary input
print json.dumps(res, indent=4, sort_keys=True)