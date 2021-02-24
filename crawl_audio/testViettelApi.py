import requests

url = "https://viettelgroup.ai/voice/api/asr/v1/rest/decode_file"
headers = {
    'token': '',
    'sample_rate': '16000',
    'format':'S16LE',
    'num_of_channels':'1',
    'asr_model': 'model code'
}
s = requests.Session()
files = {'file': open('mp3_folder/mp3_cut_15s.mp3','rb')}
response = requests.post(url,files=files, headers=headers)

print(response.text)