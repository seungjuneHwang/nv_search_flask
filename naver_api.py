# 네이버 검색 API 예제 - 블로그 검색
import os
import sys
import urllib.request
client_id = "Lv7zIt6YhMNE9AZTyuQp"
client_secret = "JT4HDalhh5"

# 여기서 부터 함수를 만들어 보자
def news(query):
    encText = urllib.parse.quote(query)
    url = "https://openapi.naver.com/v1/search/news?query=" + encText # JSON 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        # print(response_body.decode('utf-8'))
        return response_body.decode('utf-8')
    else:
        print("Error Code:" + rescode)

def blog(query):
    encText = urllib.parse.quote(query)
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        # print(response_body.decode('utf-8'))
        return response_body.decode('utf-8')
    else:
        print("Error Code:" + rescode)
# import json        
# json_data = news('가을')
# dic1 = json.loads(json_data)
# print(type(dic1))
# # print(dic1['items'])
# j_list = dic1['items']
# # 리스트를 출력 해보자
# titles = ''
# for data in j_list:
#     titles += data['title'] + '<br>'
#     # print(data['title'])
# print(titles)
