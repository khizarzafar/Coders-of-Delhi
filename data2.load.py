import json





data = json.load(open("data2_load.py"))
data = cleanData(data)
json.dump(data, open("cleaned_data2.json","w"),indent=4)
print("Data has been successfully cleaned.")