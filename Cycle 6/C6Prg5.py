f = open('D:\\20mca030\\csvfile.csv','a')
import json

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
result = json.dumps(thisdict)
f.write(result)
f.close()
f = open('D:\\20mca030\\csvfile.csv','r')
print(f.read())