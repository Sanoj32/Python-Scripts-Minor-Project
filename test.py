
import  json
data = {
    'yo': "hello yo"
}
with open('test.json','w') as outfile:
    json.dump(data,outfile)