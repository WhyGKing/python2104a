#  뷰 : 기능을 담당(페이지 단위)
# 화면이 나타나는 뷰(템플릿이 있음), 화면이 없는 뷰(템플릿이 있을수도 없을수도): 처리 중심
# 화면이 있건 없건 주소 URL은 있어야 한다

# 뷰 내용(함수, 클랫,), URL이 있으면 동작한다.

# 뷰의 코드 형식 : 함수형, 클래스형
# 함수형 : request를 매개변수로 받고(추가 매개 변수 가능), 모양은 함수
#          내가 원하는대로 동작들을 설계하고 만들고 싶을 때

# 클래스형 : CRUD 기존에 많이 사용하는 기능을 미리 클래스로 만들어 두고 상속받아서 사용
# 장고의 제네릭 뷰를 많이 사용


# 함수형 뷰를 먼저 만들어 봄.
from django.http import HttpResponse
from django.shortcuts import render   # 템플릿을 다루기 위한 것
def index(request):
    # 계산 또는 데이터베이스 조회, 수정, 등록
    # 응답 메시지를 만들어서 반환
    # html변수를 대신해서 템플릿
    html = "<html><body>Hello</body></html>"
    return HttpResponse(html)

# 연습문제 : 다음 뷰를 만들고 실행해 보자.
# 뷰의 이름은 welcome
# 뷰의 접속주소 welcome/
# 내용은 welcome to django
def welcome(request):
    return HttpResponse("<html><body>Wecome to Django...")

# 템플릿을 다루는 뷰를 추가해보자... render imort를 먼저해라.
def template_test(request):
    # 기본 템플릿 폴더
    # 1. admin 앱
    # 2. 각 앱의 폴더에 있는 templates 폴더
    # 3. 설정 폴더
    #    templates 폴더 생성하고, settting.py파일에서 templates 벼눗의 DIR 리스트에 등록함.

    return render(request, 'test.html')
# 뷰를 만들었으면 url 추가하고....


# 함수형 뷰 만들기, 템플릿 만들기, URL연결하기, 브라우저로 접속해보기 연습을 반복해보자.
#