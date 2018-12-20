data = [ {'site1':'data1'}, {'site2':'data2'} ]

with open ('list1.csv', 'w') as f:
    for dict in data:
        for key, value in dict.items():
            text = key+','+value+'\n'
            f.writelines(text)