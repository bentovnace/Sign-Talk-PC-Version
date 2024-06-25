import requests
while True:
    r = requests.get('http://192.168.1.9:5000/get_data_stream_v1').text
    print(r)