import naver_api
import json
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('main.html')

@app.route('/newspage')
def newspage():
    return render_template('news.html')

@app.route('/blogpage')
def blogpage():
    return render_template('blog.html')

@app.route('/news', methods=['GET'])
def news():
    if request.method == 'GET':
        query = request.args["query"]
        print(query)
        # 검색어를 받아서 네이버 api 함수에 전달하면 좋을것 같다
        json_data = naver_api.news(query)
        dic1 = json.loads(json_data)
        j_list = dic1['items']
        # titles = ''
        # for data in j_list:
        #     titles += data['title'] + '<br>'
        # print(titles)
        return render_template('result.html', query=query, newslist=j_list, type='뉴스')

@app.route('/blog', methods=['GET'])
def blog():
    if request.method == 'GET':
        query = request.args["query"]
        print(query)
        # 검색어를 받아서 네이버 api 함수에 전달하면 좋을것 같다
        json_data = naver_api.blog(query)
        dic1 = json.loads(json_data)
        j_list = dic1['items']
        # print(j_list)
        # titles = ''
        # for data in j_list:
        #     titles += data['title'] + '<br>'
        # print(titles)
        return render_template('result.html', query=query, newslist=j_list, type='블로그')


@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        query = request.args["query"]
        print(query)
        # 검색어를 받아서 네이버 api 함수에 전달하면 좋을것 같다
        json_data = naver_api.news(query)
        dic1 = json.loads(json_data)
        j_list = dic1['items']
        titles = ''
        for data in j_list:
            titles += data['title'] + '<br>'
        # print(titles)
        return render_template('result.html')
        # return f"GET으로 전달하고 받은 데이터는? {query}"
    else:
        query = request.form["query"]
        print(query)
        return f"POST으로 전달하고 받은 데이터는? {query}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)