import urllib
import sys # https://docs.python.org/2/library/sys.html
import json

url = 'http://query.yahooapis.com/v1/public/yql?{0}&format=json'
query = '''select LastTradePriceOnly,symbol,Name
           from yahoo.finance.quotes
           where symbol in ({0})'''

#pass arguments through command line in quotation marks
quotes = sys.argv[1]

## alternate input:
# quotes = raw_input("what ticker symbols are you interested in?")

# 
# '-'.join("a","b") results in 'a-b'
# 'a,b'.split(',') results in ['a','b'] -- delimiter
# '   a   '.strip() results in 'a' -- removes characters from before/after (can specify which character)

'''
quotes = ','.join(('"' + q.strip() + '"' for q in quotes.split(',')))
'''

quotes = quotes.split(',')	# split input into list based on comma delimiter
print quotes

a = []
for q in quotes:
	q = q.strip()		# remove whitespace
	q = '"'+q+'"'		# add quotation marks
	a.append(q)			# add cleaned symbols to list
quotes = ','.join(a)	# combine list items with comma
print quotes


'''
query = query.format(quotes)
query = urllib.urlencode(
    {'q': query, 'env': 'http://datatables.org/alltables.env'})
url = url.format(query)

res = urllib.urlopen(url).read()
print url
res = json.loads(res)['query']['results']

print json.dumps(res, indent=4, sort_keys=True)
'''
