#### ▣ swcodingschool's classroom
# Web Crawling


# 1. requests 모듈
파이썬으로 HTTP 호출하는 프로그램을 작성할 때 가장 많이 사용

Requests document : https://docs.python-requests.org/en/master/

#### 사용전 설치 먼저...
```python
# requests 패키지 설치하고 import하기
!pip install --upgrade pip
!pip install requests
```

### API
requests 라이브러리는 매우 직관적인 API를 제공한다. 어떤 방식(method)의 HTTP 요청을 하느냐에 따라서 해당하는 이름의 함수를 사용하면 된다.

- GET 방식: requests.get()
- POST 방식: requests.post()
- PUT 방식: requests.put()
- DELETE 방식: requests.delete()

### 응답상태
온라인 서비스를 HTTP로 호출하면 상태 코드를 응답받는다. 일반적으로 이 상태 코드를 보고 요청이 잘 처리되었는지 문제가 있는지 알 수 있다.

상태 코드는 응답 객체의 status_code 속성을 통해 간단하게 얻을 수 있다.

### 응답전문(response body/payload)
요청이 정상적으로 처리된 경우, 응답전문에 요청한 데이터가 담겨져 온다. 응답전문은 크게 3가지 방식으로 읽어올 수 있다.

첫번째, content 속성을 통해 바이너리 원문을 얻을 수 있다.
두번째, text속성을 통해 UTF-8로 인코딩된 문자열을 얻을 수 있다.
마지막으로, 응답 데이터가 JSON 포맷이라면 json() 함수를 통해 사전dictionary 객체를 얻을 수 있다.
```python
response = request.get("URL")
response.content
response.text
response.json()
```

### 응답헤더
응답에 대한 메타 데이터를 담고 있는 응답 헤더는 headers 속성을 통해 딕셔너리 형태로 얻을 수 있다.
```python
response.headers
response.headers['Content-Type']
```

### 요청 쿼리
GET방식으로 HTTP요청을 ㅡ할 때는 쿼리 스트링(query string)을 이용, 응답받을 데이터를 필터링하는 경우가 많다.   
params  옵션을 사용하면 쿼리스트링을 딕셔너리 형태로 넘길 수 있다.
```python
>>> response = requests.get("https://jsonplaceholder.typicode.com/posts", params={"userId": "1"})
>>> [post["id"] for post in response.json()]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```


```python
# 네이버에 GET 요청하기
import requests
url = 'http://www.naver.com'
response = requests.get(url)
print("status code : ", response.status_code)
# 응답코드로 200을 리턴. 정상적으로 값을 받았음을 확인.
# 아래 명령어를 추가로 실행해서 응답받은 페이지 내용을 출력해 볼 수 있음
# print(response.text)
```


```python
# POST 메소드를 사용하는 방법
import requests
url = 'http://www.naver.com'
response = requests.post(url)
print("status code : ", response.status_code)
```


```python
# 데이터 전송방법. 전달하기
# 방법 1. 직접 파라미터를 넣어서 보내기 
# 방법 2. dictionary 이용, params 를 사용 파라미터를 넣어서 보낼수 있다.
# 방법 3. POST로 보내기
# 방법 4. SSL 인증서를 사용하는 경우
# 방법 5. 인증이 필요한 경우
```


```python
# 방법 1로 보내기 :
import requests
url = 'http://www.naver.com?a=bbb&b=123'

print("status code : ", response.status_code)
```


```python
# 방법 2로 보내기
import requests
paramDict = {"a":"bbb", "b":123}
url = "http://www.naver.com"
response = requests.get(url, params=paramDict)
print("staus code :", response.status_code)
# parameter 형태
# 자료형 이름 = {"param1":value1, "param2":value2, ...}
```


```python
# 방법 3 post로 데이터 보내기
# post로 보낼 때는 url주소에 파라미터를 넣지 않기 때문에 방법2와 같이 처리
# 단, 다른 점은 get 메소드에서는 params 인자 사용. post 메소드에서는 data 인자 사용
import requests
paramDict = {"a":"bbb", "b":123}
url = "http://www.naver.com"
response = requests.post(url, data=paramDict)
print("staus code :", response.status_code)
```


```python
# 방법 4. SSL 인증서를 사용하는 경우
# 보안 때문에 http보다 https를 많이 사용. 간혹 ssl때문에 오류가 발생. verify 옵션 추가
import requests
url = "https://www.naver.com"
response = requests.post(url, verify=False)  # False의 경우 warning 발생. default값은 True.
print("status code : ", response.status_code)
```


```python
# 방법 5. 인증이 필요한 경우
# API를 사용할 때 KEY 토큰을 할당받아서 사용하기도 하지만, 
# id와 password를 이용해 인증하는 경우도 있음
# 이때는 auth 옵션 사용
import requests
url = "https://www.naver.com"
response=requests.post(url, auth=("id", "pass"))
print("status code : ", response.status_code)                     
```


```python
# 실습 따라하기
# google 에 검색어 'python' 던지기
import requests
URL = 'https://www.google.com/search'

#response = requests.get(URL)

# get요청시 parameter 전달하기
# params = {'param1': 'value1', 'param2': 'value'}
# res = requests.get(URL, params=params)
params = {'q' : 'python'}
response = requests.get(URL, params=params)

print(response.status_code)
print(response.text)

# 추가학습
"""
1. POST요청할 때 data 전달하기 : params대신 data라는 이름으로 준다.
data = {'param1':'value1', 'param1':value2}
res = requests.post(URL, data=data)

2. 헤더추가, 쿠키 추가
별도의 헤더 옵션을 추가하고자 할 때는 headers 옵션을, 
쿠키를 심어서 요청을 보내고 싶으면 cookies 옵션을 사용하면 된다

headers = {'Content-Type': 'application/json; charset=utf-8'}
cookies = {'session_id': 'sorryidontcare'}
res = requests.get(URL, headers=headers, cookies=cookies)

3. 응답객체(Reaponse)
요청(request)을 보내면 응답(response)을 받는다. 
당연히 이 응답은 python 객체로 받는다. 
그리고 이 응답 객체는 많은 정보와 기능을 가지고 있다. 
ipython이나 jupyter notebook에서 <탭> 기능을 이용해서 직접 체험해보면 
금방 파악이 가능하다.
"""
```


```python
# 실습 따라하기
print(response.request) # request객체에 접근 가능
print(response.status_code) # 응답코드
print(response.raise_for_status()) # 200 OK 코드가 아닌 경우 에러 발동
#response.json()  # json response일 경우 딕셔너리 타입으로 바로 변환
```


```python
# 실습 따라하기 : 서울시 코로나 확진자 발생현황 스크래핑
import requests
URL = 'https://www.seoul.go.kr/coronaV/coronaStatus.do'
response = requests.get(URL)
html_data = response.text
print(html_data)
```


```python
# 실습 따라하기 : 네이버 증권 
import requests 
URL = 'https://finance.naver.com'
#response = requests.get(URL)
# 크롤러를 차단하였을 때, 브라우저를 이용한 직접 검색처럼 꾸미기
header = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'}
response = requests.get(URL, headers=header)

html_data = response.text
print(html_data)
```


```python
## requests 모듈 활용 샘플 코드 
## 실제 사용시, 조건문을 이용 응답 코드에 따라 다른 로직으로 처리하도록 구성
## 정상적으로 응답을 받을 경우와 잘못된 url 사용으로 4xx 코드 받을 경우
import requests

url = "https://www.naver.com"   # 정상적 url 요청
#url = "https://www.test.com"   # 비정상적 url 요청
rs = requests.post(url)

rs_code = rs.status_code

if int(rs_code) == 200:
    print("페이지 데이터 정상 수신")
    page_data = rs.text
    print(page_data)
else:
    print(rs_code,"페이지 데이터 수신 실패")   
```

# 2. urllib 모듈

### urllib 모듈이란?
- 파이썬의 표준 모듈로써 URL을 다루기 위한 모듈 패키지
- 설치가 필요하지 않고, import urllib로 활용
- requests 모듈과 마찬가지로 URL과 관련된 여러가지 기능들을 제공
- https://docs.python.org/3/urllib.html

### 4가지의 하위 모듈 
- request : url을 열고 읽기 위한 모듈(http요청).  https://docs.python.org/ko/3.10/library/urllib.request.html
- parse : url구문 분석을 위한 모듈(url 해석 및 조작)  https://docs.python.org/ko/3.10/library/urllib.parse.html
- error : request 모듈에서 발생하는 예외들을 포함하는 모듈 https://docs.python.org/ko/3.10/library/urllib.error.html
- robotparser : robots.txt 파일을 파싱하는 모듈 https://docs.python.org/ko/3.10/library/urllib.robotparser.html


```python
# urllib.request : Request()
# urllib.request는 URL(Uniform Resource Locator)을 가져오기 위한 파이썬 모듈

import urllib
URL = 'https://introsjlee.pythonanywhere.com'
request = urllib.request.Request(URL)
print(request)
print(request.full_url)
print(request.type)
print(request.host)
```


```python
# urllib.request : urlopen() 
# urlopen 함수의 형태로, 매우 간단한 인터페이스를 제공
# 해당 url 열기, 응답데이터는 바이트 형식의 HTTPResponse 객체
# request 객체 또는 URL을 직접 넣어도 가능
import urllib
URL = 'https://introsjlee.pythonanywhere.com'
request = urllib.request.Request(URL)

response1 = urllib.request.urlopen(request)
response2 = urllib.request.urlopen(URL)
print(response1)
print(response2)
print(response1.geturl())
print(response1.getheaders())
```


```python
# 응용하여 사용해보기
# rullib.request를 사용하는 가장 간단한 방법

import urllib.request
url = 'https://introsjlee.pythonanywhere.com'
with urllib.request.urlopen(url) as response:
    html = response.read()
print(html)
```


```python
# 응용하여 사용해보기 2
# URL을 통해 리소스를 가져와서 임시 위치에 저장하려면, shutil.copyfileobj()와 tempfile.NamedTemporaryFile() 함수를 통해 수행
import shutil
import tempfile
import urllib.request

with urllib.request.urlopen('https://introsjlee.pythonanywhere.com') as response:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        shutil.copyfileobj(response, tmp_file)

with open(tmp_file.name) as html:
    pass

print(html)
```


```python
# urllib.request.urlopen()
# urllib.request에 포함되어 있으며, python3에서는 request까지 모두 import해야 에러가 발생하지 않는다.
# 해당 url을 열고 데이터를 얻을 수 있는 함수와 클래스를 제공하며, http를 통해 웹 서버에 데이터를 얻는 데 많이 사용한다.
# urlopen(url[,data [,timeout]])
# url : 열고자 하는 url문자열, request클래스의 인스턴스가 포함된다.
# data는 post방식으로 전송시에 서버로 업로드할 폼 데이터, url 인코딩 되어 있는 문자열
# timeout : 내부에서 사용하는 모든 블로킹 연산에 사용할 타임아웃 시간
#
#
# urlopen에서는 몇가지 메서드를 지원한다. 몇가지 정리하면...
# urlopen().read([nbytes]) : nbyte의 데이터를 바이트 문자열로 읽음
# urlopen().readline() : 한 줄의 텍스트를 바이트 문자열로 읽음
# urlopen().info() : URL에 연관된 메타 정보를 담은 매핑 객체를 반환
# urlopen().getcode() : HTTP 응답 코드를 정수로 반환( 200, 404 )
# urlopen().close() : 연결을 닫는다
#
# urlopen().read() :
# urlopen으로 연 객체를 읽고, 인자로 전달하는 숫자만큼 데이터를 읽음. 바이트 형식의 데이터
# read([nbytes]) : nbyte의 데이터를 바이트 문자열로 읽음
# readline() : 한 줄의 텍스트를 바이트 문자열로 읽어 리스트에 반환
import urllib
url = 'https://introsjlee.pythonanywhere.com'
response = urllib.request.urlopen(url)
byte_data = response.read() # 해당 url에 있는 html데이터를 바이트 문자열로 반환
#byte_data = response.readline()
print(byte_data)
# info() 메서드를 쓰면 해당 URL의 메타 정보를 담은 매핑 객체를 반환
print(response.info())
```


```python
# with 구문 활용, 이렇게도 표현 가능
import urllib.request

URL = 'https://introsjlee.pythonanywhere.com'
req = urllib.request.Request(URL)
with urllib.request.urlopen(req) as response:
    byte_data = response.read()
print(byte_data)
```


```python
# urllib.request : decode()
# 분석을 위해서 바이트 형식의 데이터를 원하는 형식으로 변환
# 기본값으로 utf-8 사용
import urllib
URL = 'https://introsjlee.pythonanywhere.com'
response = urllib.request.urlopen(URL)
byte_data = response.read()
text_data = byte_data.decode()
print(text_data)
```


```python
# urlretrieve() 
# 웹상의이미지를 다운로드
# 이미지 url 주소를 입력 후, 해당 주소 이미지를 다운로드해 저장
import urllib.request
img_src = 'https://img1.daumcdn.net/relay/cafe/original/?fname=http%3A%2F%2Fcfs8.blog.daum.net%2Fimage%2F33%2Fblog%2F2008%2F08%2F28%2F07%2F02%2F48b5cecb1de78%26filename%3D4%25EC%2595%2584%25EB%25A6%2584%25EB%258B%25A4%25EC%259A%25B4%25ED%2592%258D%25EA%25B2%25BD.jpg'
save_name = 'test.png'
urllib.request.urlretrieve(img_src, save_name)
print("저장되었습니다.")
```


```python
###
# urllib.parse : urlparse()
# url을 파싱하여 분석하기 위한 모듈
# http뿐만 아니라 ftp, ssh, imap 등도 포함
# url 형식 : 프로토콜://아이디:비밀번호@호스트:포트/하위경로?파라미터#색인
# url을 6개로분리하여 반환
import urllib
parse = urllib.parse.urlparse('https://introsjlee.pythonanywhere.com/friends/detail/1')
print(parse)
print(parse[0])
print(parse[1])
print(parse[2])

# urlsplit()
# url을 5개로 분리하여 반환
parse2 = urllib.parse.urlsplit('https://introsjlee.pythonanywhere.com/bookmark/detail/1')
print(parse2)
print(parse2[0])
print(parse2[1])
print(parse2[2])
```


```python
# urllib.parse : urlunparse(), urlunsplit()
# 분리된 url을 다시 합침
# 튜플(변경 불가능)로 반환되기 때문에 리스트(변경가능)로 변경하여 활용
parse = list(parse)
parse[1] = 'blog.daum.net'

unparse = urllib.parse.urlunparse(parse)
print(unparse)
```


```python
# parse_qs(), parse_qsl()
# 쿼리를 파싱해서 각각 사전(qs) 및 리스트(qs1)로 반환
# 쿼리를 변경하여 요청할 때 활용
import urllib
parse = urllib.parse.urlparse('https://www.naver.com?a=1&b=2&c=3&d=4')
print(parse)
print(parse.query)
print(type(parse.query))
#
# 
qs = urllib.parse.parse_qs(parse.query)
print(qs)
print(type(qs))
#
#
qs1 = urllib.parse.parse_qsl(parse.query)
print(qs1)
print(type(qs1))
```


```python
# urljoin(a,b)
# a와 b url을 합쳐주는 기능
# /에 따라 url주소가 달라지는 것 주의
import urllib.parse
url = 'https://naver.com/a/b'
print(urllib.parse.urljoin(url, 'c'))
print(urllib.parse.urljoin(url, '/c'))

##
url = 'https://naver.com/a/b/'
print(urllib.parse.urljoin(url, 'c'))
print(urllib.parse.urljoin(url, '/c'))
```


```python
# quote(), unquote()
# 아스키 코드가 아닌 문자들을 퍼센트 인코딩을 변환
# URL에 한글이 섞여 있을 때 발생하는 오류 해결을 위해 사용함
import urllib
url = 'https://search.naver.com/search.naver?query=파이썬'
response = urllib.request.urlopen(url)  # UnicodeEncodeError 발생함
#encoded = urllib.parse.quote('파이썬')
#url = 'https://search.naver.com/search.naver?query=' + urllib.parse.quote('파이썬')
response = urllib.request.urlopen(url)  # UnicodeEncodeError 발생함
byte_data = response.read()
text_data = byte_data.decode()
print(text_data)  
#print(urllib.parse.quote('파이썬'))
```


```python

```


```python
# urllib 활용
# 1. 홈페이지를 로컬에 파일로 저장
# 파일 입출력 함수 활용(open, write, close )
```


```python
# 2. 헤더를 추가해서 모바일 페이지로 저장
# request 함수에 헤더 인자에 값을 전달
import urllib
header = {'User-Agent' : 'Mozilla/5.0 (iPhone)'}
request = urllib.request.Request("http://www.naver.com", headers=header)
data = urllib.request.urlopen(request).read()
f = open("mobile.html", "wb")
f.write(data)
f.close()
```


```python
# 파라미터를 변경해 여러 정보 가져오기
# 파이썬 문법을 활용해 연관검색어 리스트 출력
# 여러가지 검색어의 Naver 검색 결과 출력
import urllib
query_list = ['파이썬', '웹 크롤링', '빅데이터', 'python']
url = 'https://search.naver.com/search.naver?query='
for i in query_list:
    new_url = url + urllib.parse.quote(i)
    response = urllib.request.urlopen(new_url)
    byte_data = response.read()
    text_data = byte_data.decode()
    print(text_data)
```


```python
import urllib
URL = 'https://search.yahoo.com/search?p='
URL = URL + urllib.parse.quote('파이썬')
response_urllib = urllib.request.urlopen(URL)
byte_data = response_urllib.read()
text_data = byte_data.decode()
print(text_data)
```


```python
# https://www.youtube.com/results?search_query=

import urllib
URL = 'https://www.youtube.com/results?search_query='
URL = URL + urllib.parse.quote('파이썬')
response_urllib = urllib.request.urlopen(URL)
byte_data = response_urllib.read()
text_data = byte_data.decode()
print(text_data)
```

# 3. BeautifulSoup 모듈
- 홈페이지 내 데이터를 쉽게 추출할 수 있도록 도와주는 파이썬 외부 라이브러리
- 웹 문서 내 수많은 HTML 태그들을 parser를 활용해 사용하기 편한 파이썬 객체로 만들어 제공
- 웹 문서 구조를 알고 있다면, 아주 편하게 원하는 데이터를 뽑아 활용할 수 있음


```python
# 설치하기
# !pip install bs4
# 또는 
# !pip install beautifulsoup4
```


```python
from bs4 import BeautifulSoup
import urllib

URL = 'http://www.naver.com'
response_urllib = urllib.request.urlopen(URL)
byte_data = response_urllib.read()
text_data = byte_data.decode()

soup = BeautifulSoup(text_data, 'html.parser')
print(soup.prettify())
```

### BeautifulSoup 모듈 정의 : 기존 방식과의 차이점
- 기존 방식 : 정규 표현식, 문자열 함수 등을 활용하여 홈페이지 텍스트 내 패턴을 분석하여 하나식 원한느 데이터를 찾아가는 형식
- BeuatifulSoup 방식 : html문서를 태그를 기반으로 구조화하여 태그로 원하는 데이터를 찾아가는 방식


```python
import requests
from bs4 import BeautifulSoup

req = requests.get('https://naver.com')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

result = soup.find_all('a', 'thumb', limit=5)
news_list = []
for i in result:
    news_list.append(i.find("img")["alt"])
print(news_list)

print(soup.title)
print(soup.title.name)
print(soup.title.string)

print(soup.img)
```


```python

```


```python
# 네이버 영화 랭킹 가져오기
# 1. 홈페이지 텍스트 가져오기
# https://movie.naver.com/movie/sdb/rank/rmovie.nhn
# 2. BeautifulSoup으로 파싱하기
import requests
from bs4 import BeautifulSoup
URL = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
req = requests.get(URL)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
print(soup)
```


```python
# 텍스트에서 영화 랭킹 가져오기 Step 2.
# 1. 텍스트에서 영화 랭킹 찾기
# 2. 영화랭킹에 해당하는 부분의 태그 찾기
movie_ranking_list = soup.find_all('div', 'tit3')
for i in range(len(movie_ranking_list)):
    print("{:2}위:{}".format(i+1, movie_ranking_list[i].get_text().strip()))
```


```python
# BeautifulSoup 모듈을 활용하여 네이버 뉴스 페이지의 헤드라인 뉴스를 가져오는 
# 코드를 작성하세요.
import requests
from bs4 import BeautifulSoup
URL = "http://news.naver.com"
req = requests.get(URL)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
print(soup)

```


```python
head_news_list = []
result_bit = soup.find_all('p', "hdline_fick_kit")
for i in result_big:
    head_news_list.append(i.get_text())
result_small = soup.find_all('div', "hdline_article_tit")
for i in result_small:
    head_news_list.append(i.get_text().strip())
print(head_news_list)
```

# 4. Selenium 모듈
- python으로 크롤링할 때 크롤링 대상인 웹 페이지에 동적인 동작과 함께 크롤링 하기 위해 필요한 라이브러리 모듈.
- 웹 어플리케이션 테스트를 위한 프레임워크(제작한 홈페이지를 테스트하기 위해 사용)
- 다양한 언어에서 지원하며(C++, JAVA, Python 등) 사용자가 아닌 프로그램이 웹 브라우저를 제어할 수 있도록 지원
- 웹 브라우저마다 클라이언트 프로그램(Web Driver)이 별도로 필요(웹브라우저 - 프로그램간 통신 목적)
- 크롤링보다는 웹을 제어하는 목적이 더 큼

### selenium의 장점
- 웹 드라이버를 사용해서 웹 페이지를 동적으로 크롤링할 수 있다. 크롤링 결과 특정 html 엘리먼트에 마우스 클릭을 발생시키거나, input 엘리먼트에 텍스트를 채워넣기 등이 가능하다.


## Selenium 설치(Windows 10기준)

### Selenium 설치 명령어 
```python
pip install selenium  # pip로 설치하는 방법
!pip install selenium  # jupyter notebook cell 상태에서 설치하기
```
### Chrom Web Driver 설치
브라우저 주소창에 https://chromedriver.chromium.org/downloads 를 입력하고 다운로드 페이지를 연다.  
플랫폼과 크롬 버전에 맞는 버전을 선택하여 다운로드 한다. 윈도우즈 버전의 경우 win32만 있으나 64머신에서도 아무 문제 없이 잘 동작한다.  
크롬 버전은 크롬 브라우저의 도움말 > Chrome정보를 통해 확인할 수 있다.  


## Selenium 모듈 활용
### HTML로 접근하기
- BeautifulSoup 모듈과 비슷하게 HTML문서의 구조에 따라 접근할 수 있음
- BeautifulSoupㅇ서 원하는 태그, 속성 등을 가져오기 위해 단일 객체는 find(), 복수 객체는 find_all()함수로 접근햇다면, selenium에서는 태그 종류에 따라 각각 함수가 있음
- 단일객체 
  - find_element_by_id()
  - find_element_by_css_selector()
  - find_element_y_class_name()
  - ...
- 복수객체(리스트 형태)
  - find_elements_by_class_name()
  - find_elements_by_xpath()
  - find_elements_by_tag_name()
  - ...

- 원하는 데이터의 태그를 쉽게 검색하려면 브라우저에서 마우스 우클릭 > 검사 선택 > 원하는 데이터로 마우스 이동

  


```python
#
#  셀레니움 web driver 설치가 완료되었다면 간단한 selenium 크롤링 코드를 작성해보자.
# 
import selenium
from selenium import webdriver
# selenium에서 사용할 웹 드라이버의 절대 경로
path = "C:/Users/dears/chromedriver/chromedriver.exe"

# selennium의 webdriver에 앞서 설치한 crhonedriver를 연동한다.
driver = webdriver.Chrome(path)

# driver로 특정 페이지를 크롤링한다.
driver.get('https://www.naver.com')

print("="*100)
print(driver.title)   # 크롤링한 페이지의 title 정보
print(driver.current_url)  # 현재 크롤링된 페이지의 url
print("네이버 홈페이지 크롤링")
print("위의 특정 페이지가 크롬의 별도 탭에서 열리고, 'Chrome이 자동화된 테스트 소프트웨어에 의해 제어되고 있습니다' 메시지 출력...")
print("="*100)
```


```python
#HTML로 접근하기 : find_element_by_id()  : 원격으로 브라우저를 열고 해당 id의 정보를 가져온다.
element = driver.find_element_by_id("account")
print(element)
print(element.tag_name)
print(element.text)
```


```python
#HTML로 접근하기 : find_element_by_class_name()  : 원격으로 브라우저를 열고 해당 class의 정보를 가져온다.
element = driver.find_element_by_class_name("eg-flick-panel") # 날씨 플리커 찾아서 내용 출력하기
print(element)
print(element.tag_name)
print(element.text)
```

### 이벤트로 제어하기
selenium은 브라우저를 직접 제어하기 때문에 마치 사람이 직접 컨트롤하듯이 마우스 클릭, 키보드 입력, 자바 스크립트 등 이벤트 처리를 할 수 있다.
- 마우스 클릭 : click()
- 키보드 입력 : send_keys()
- 자바스크립트 삽입: execute_script()
- 입력 양식 전송 : submit()
- 스크린샷 : screenshot(파일이름)
- 글자 지움 : clear()
- 뒤로 가기 : back()
- 앞으로 가기 : forwar()


```python
# 날씨 플리커를 찾아서 클릭해보자.
element = driver.find_element_by_class_name("eg-flick-panel") # 날씨 플리커 클릭해보기
print(element)
element.click()
```


```python
# 네이버의 검색창 id는 query
# 검색창을 찾아 검색어로 웹크롤링 입력
element = driver.find_element_by_id("query")
print(element)
print(element.tag_name)
element.send_keys("웹크롤링")
# element.send_keys(Keys.ENTER) # 특수 키 입력 가능..
# 특수키를 입력하려면 
# from selenium.webdriver.common.keys import Keys
# 를 먼저 import 해야 한다.
# 보통은 특수키보다는 클릭 버튼을 찾아서 클릭이벤트로 처리함.
```


```python
#셀레니움 모듈을 활용하여 네이버 메인 페이지에서 사전 바로가기 링크를 클릭한 뒤, 
# 사전 페이지에서 파이썬 검색어를 입력 및 검색한 결과를 브라우저로 띄우는 코드를 작성하세요.
import selenium
from selenium import webdriver

path = "C:/Users/dears/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get('https://www.naver.com')

#id, 또는 클래스이름으로 검색이 어려운 엘리먼트는 xpath로 요소를 지정할 수 있다.
# 개발자 도구 화면에서 요소 선택 버튼을 누른 후, 버튼 요소를 선택한다. 
# 버튼의 요소를 찾았으면, 요소 선택 후 마우스 우클리갛여 복사할 방법을 선택하는데 
# 복사 옵션을 xpath로 선택한다.
# 이때 주의할 점은 큰따옴표를 작은 따옴표로 바꾸고 사용토록 한다.
#element = driver.find_element_by_class_name("mn_dic")
element = driver.find_element_by_xpath("//*[@id='NM_FAVORITE']/div[1]/ul[2]/li[1]/a")  # xpath로 복사한 것


print(element)

element.click()
element = driver.find_element_by_id("ac_input")
element.send_keys("python")
element = driver.find_element_by_class_name("btn_search")
element.click()

```


```python
# BeautifuSoup 모듈 응용
# html의 DOM의 정의
# 노드를 활용한 검색
# BeautifulSoup 모듈의함수를 활용하여 노드를 기준으로 원하는 데이터 추출
import requests
from bs4 import BeautifulSoup
URL = "http://www.naver.com"
req = requests.get(URL)
html = req.text

soup = BeautifulSoup(html, 'html.parser')
contents = soup.find('body')
for child in contents.children:
    print(child)
```


```python
img_tag = contents.find('img')
print(img_tag)
print(img_tag.parent) # 바로 위 부모 노드를 출력함...
print("=")
print(img_tag.find_parent('div')) # 특정 부모 노드까지 검색해서 올라감
```


```python
# 연습용 페이지 구조를 전제로 함....
#find_next_sibling() 바로 다음 형제 노드를 검색
#find_next_siblings() 모든 형제노드를 검색
#find_previous_sibling()
#find_previous_siblings()
from bs4 import BeautifulSoup as bs
URL = "http://www.naver.com"
req = requests.get(URL)
html = req.text

soup = BeautifulSoup(html, 'html.parser')
contetns = soup.find('body')

p_tag = bs.find("p", class_ ="b")
print(p_tag)

print(p_tag.find_next_sibling())
print(p_tag.find_next_siblings())
```


```python
# selenium 모듈 응용
# 폼양식 전송 실습
# selenium + web driver를 활용하여 버튼을 클릭하거나 자바스크립트 삽입 등 특정 조건이 충족되어야만 접근 가능한 대이터를
# 모듈을 활용하여 가져올 수 있음
# 활용예제 : 폼 양식을 이용해 naver 로그인하기 실습
import selenium
import time
from selenium import webdriver

path = "C:/Users/dears/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get('https://www.naver.com')

element = driver.find_element_by_class_name("link_login")
element.click()
# 로그인 페이지가 뜨면 로그인 정보 입력
id = 'yourid'
#pw = 'password'
pw = 'yourpassword'
element=driver.find_element_by_id('id')
element.send_keys(id)
time.sleep(1)
element=driver.find_element_by_id('pw')
element.send_keys(pw)
time.sleep(1)
logbtn = driver.find_element_by_id("log.login")
logbtn.click()
# 자동 로그인 방지를 위한 capchar 적용
# 자동화된 크롤러 구성에 불편함
```


```python
# 자동 로그인 방지를 위한 capchar 적용
# 자동화된 크롤러 구성에 불편함
# 회피방법 : 
# 자바스크립트로 데이터 입력하기
# 로그인폼의 id와 pwd요소에 직접 데이터 전달(send_keys보다 훨씬 안정적)

import selenium
import time
from selenium import webdriver

path = "C:/Users/dears/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get('https://www.naver.com')

element = driver.find_element_by_class_name("link_login")
element.click()
# 로그인 페이지가 뜨면 로그인 정보 입력
id = 'yourid'
#pw = 'password'
pw = 'yourpassword'

#*******************************
driver.execute_script("document.getElementById('id').value=\'" + id +"\'")
time.sleep(1)
driver.execute_script("document.getElementById('pw').value=\'" + pw +"\'")
time.sleep(1)
#*******************************
logbtn = driver.find_element_by_id("log.login")
logbtn.click()
```


```python
# BeautifulSoup + Selenium 모듈 응용
# 메일 목록 가져오기 실습
# BeautifulSoup 모듈 : 로그인이 필요하거나 어떠한 버튼 등을 클릭한 뒤 나오는 페이지의 정보들을 가져오기 어려움
# selenium모듈 : 수많은 데이터들을 손쉽게 가져오기 어려움
# ====> 두 모듈 함께 활용 : bs로 접근하기 어려운 페이지를 s으로 접속하여 bs로 분석

# 실습
# s을 활용한 네이버 로그인 및 메일 탭 클릭
from bs4 import BeautifulSoup
import selenium
import time
from selenium import webdriver

path = "C:/Users/dears/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get('https://mail.naver.com')

# 메일 페이지로 직접 연결하면 아래 생략
#element = driver.find_element_by_class_name("link_login")
#element.click()
# 로그인 페이지가 뜨면 로그인 정보 입력
id = 'yourid'
pw = 'yourpassword'


#*******************************
driver.execute_script("document.getElementById('id').value=\'" + id +"\'")
time.sleep(1)
driver.execute_script("document.getElementById('pw').value=\'" + pw +"\'")
time.sleep(1)
#*******************************
logbtn = driver.find_element_by_id("log.login")
logbtn.click()


# element = driver.find_element_by_class_name('btn_global')# 클래스네임 미확인
# element.click()
# time.sleep(1)
# 새로운 기기 로그인....
# 등록 버튼 클릭하고 가기
# element = driver.find_element_by_xpath("//*[@id='new.save']")
# element.click()
# time.sleep(1)


# 로그인 최종 성공 후 페이지에서 메일링크 찾아서 클릭하기 
#element = driver.find_element_by_class_name('tab MY_TAB_MAIL')
# element = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[1]/div/div[2]/a[1]")
# element.click()

# 버튼 찾기가 안되어서... ㅋㅋㅋ
# 메일 페이지로 직접 연결 
#driver.get('https://mail.naver.com')

## 메일함 소스 가져오기
page_source = driver.page_source
soup = BeautifulSoup(page_source, "html.parser")    # 셀레니움과 BS 의 연결
# print(soup)
mail_list = soup.select("div.subject")
cnt = 1
for i in mail_list:
    print(cnt)
    print('메일제목 :', i.select_one('a').text)
    print('메일내용 :', str(i.select_one('strong').text).split(':')[1])
    print()
    cnt +=1

```
