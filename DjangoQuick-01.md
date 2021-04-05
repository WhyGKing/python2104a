[previous: Dajngo 개요 ◀◀](./DjangoQuick-00.md) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;@ here...  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [▶▶next: Django Project 생성](./DjangoQuick-02.md)

###### ▣ swcodingschool's Coding Class

# Django Tutorial Class

> ### 교육기관 : 한국아이티 전문학원

> ### 교육기간 : (총 3시간)

# Django Quick Install

Django를 사용하기 위해서는 먼저 설치를 해야한다. 설치과정과 관련한 세부 사항은 설치 가이드(https://docs.djangoproject.com/en/3.1/topics/install/)를 참고할 수 있다.

### 파이썬 설치하기

Django는 파이썬 웹 프레임워크이므로 파이썬이 필요하다. 이미 Python이 설치되어 있다면 이 과정은 생략할 수 있다.

-  Python 최신버전 [다운로드](https://www.python.org/downloads/)

- Python 설치 : 설치시 설치경로를 반드시 Path에  추가 체크할 것!!

- Python 설치 버전 확인 : 윈도우즈 환경의 경우 프롬프트상에서 python -V 또는 python --version 으로 설치된 Python 버전을 확인할 수 있다.



### 데이터베이스 설정하기

이 단계는 PostgreSQL, MariaDB, MySQL, Oracle 과 같은 규모의 데이터베이스 엔진을 사용하여 작업할 때만 필요하다. 이러한 데이터베이스를 설치하려면  [데이터베이스 설치가이드](https://docs.djangoproject.com/en/3.1/topics/install/#database-installation)를 참고할 수 있다. Python에 기본적으로 내장된 SQLite를 사용한다면 별도의 데이터베이스 설정은 필요없다.



### Django 설치하기

```python
python -m pip install Django
```



### 설치 확인하기

```python
import django
print(django.get_version())
```





