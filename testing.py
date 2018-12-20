import json


data = [ {'site1':'data1'}, {'site2':'data2'}, {'site2':'data2'}, {'site2':'data2'} ]

with open('hasil.json', 'w') as fp:
    json.dump(data, fp)