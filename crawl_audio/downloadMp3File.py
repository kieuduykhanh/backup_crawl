import requests
import json

with open('data.json') as f:
    data = json.load(f)

for i in range(len(data)):
    for j in range(len(data[i]['links'])):
        try:
            url = data[i]['links'][j]
            r = requests.get(url, allow_redirects=True)
            file_name = data[i]['name'] + str(j) + '.mp3'
            open('mp3_folder/'+file_name, 'wb').write(r.content)

            print('done: ', i, j)
        except:
            print('error: ', i, j)