# from django.test import TestCase

# Create your tests here.

# import requests
# d = {
#     'title' : 'new',
#     'content' : 'newnew',
#     'is_complete' : 0
# }

# import requests
# d = {
#     'title' : 'new',
#     'content' : 'newnew',
#     'is_complete' : 0
# }
# data = requests.post('http://127.0.0.1:8000/todo_list/create/', data = d)
# data = requests.put('http://127.0.0.1:8000/todo_list/1/update/', data = d)
# data = requests.delete('http://127.0.0.1:8000/todo_list/3/delete/')

# print(data)






rest_key = '5b11c1507025858e59f3381bdad95f45'

import requests
import json
import pandas as pd

headers = {
    "Authorization": "KakaoAK {}".format(rest_key)
}
url = 'https://dapi.kakao.com/v2/search/web?query={}&size=50'.format("저녁밥")

t = requests.get(url, headers = headers)
raw = json.loads(t.text)
signs = []
signs.extend(raw['documents'])
for k in range(0, 50):
    data = requests.post('http://127.0.0.1:8000/apis/apic/', signs[k])
    print(data)