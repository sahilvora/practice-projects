''' 
JSON API
https://data.cityofchicago.org/resource/7as2-ds3y.json

1) five most pothole-filled 10 block sections of road in chicago
2) worst road based on historical data involving actual number of patched potholes

'''
# itertools: 
# - http://kentsjohnson.com/blog/arch_m1_2005_12.html#e69
# - 
# pandas: http://pandas.pydata.org/pandas-docs/stable/index.html
import urllib
import sys
import json
import collections

url = 'https://data.cityofchicago.org/resource/7as2-ds3y.json'

res = urllib.urlopen(url).read()
potholes = json.loads(res)

zip_list = []

for ticket in potholes:
    if ticket['status'] == 'Open':
        try: 
            zip_list.append(ticket['zip'])
        except KeyError:
            print 'no zip here'

print collections.Counter(zip_list)



'''
d = {dictionary}
sum(d.values())
'''

'''
a = 0
for row in potholes:
    a = a+1

print a
'''

'''
# json examples - https://docs.python.org/2/library/json.html
# .loads() parses json into dictionary type
# 'results' is dictionary within 'query' dictionary
res = json.loads(res)['query']['results'] 

# .dumps() for pretty printing of dictionary input
print json.dumps(res, indent=4, sort_keys=True)
'''