import json
import requests

v1 = input ('Enter a food: ')
v2 = input ('Enter an ABV: ')

url = 'https://api.punkapi.com/v2/beers?food='+v1+'&abv='+v2+'' 

r = requests.get(url)

data = json.loads(r.text)

beer_list =[]

for item in data:
    name = item['name'] #the terms here can be found in the json data 
    tagline = item['tagline']
    abv = item['abv']
    
    #creating a dictionary of key and value pairs for each beer
    
    beer_details = {'name':name, 'tagline':tagline, 'abv':abv}
    beer_list.append(beer_details) 
    
print(beer_list)

import tabulate
header = beer_list[0].keys()
rows = [x.values() for x in beer_list]
print(tabulate.tabulate(rows, header))