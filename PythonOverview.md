[previous: 강의개요 ◀◀](./README.md) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;@ here...  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [▶▶next: 파이썬 1시간에 끝내기 ](./PythonInOneHour.md)

###### ▣ swcodingschool's Coding Class
# Python Overview

> ***PYTHON IS BOOMING!  IT IS THE TOP LANGUAGE BEING TAUGHT IN UNIVERSITIES.***
>
> *Python developers are  among the  highest paid. With  the  boom  in  datascience, Python is  quickly becoming one  of  the  most desired  skills foranalytics. Operations are  also  adopting Python to  manage their backendsystems. They are  discovering what web  developers using Python haveknown for a long time; namely, that Python will make you productive.*
>
> ***파이썬 붐입니다. 대학에서 가르치는 가장 인기있는 언어가 되었어요.*** 
>
> *Python 개발자는 가장 높은 급여를 받고 있고, 데이터사이언스 붐과 함께 Python은 분석에 가장 원하는 기술 중 하나가 되었다. 많은 개발자들이 백엔드 시스템을 관리하기 위해 Python을 채택하고 있다. 파이썬이 제공하는 생산성을 활용하기 위하여 웹개발자들도 오랫동안 작업했던 많은 것들을 파이썬으로 대체하고 있다.* 
>
> *from <llustrated Guide to PYTHON 3> by Matt harrison 2017.* 



#### 왜 Python을 배워야 하는가?

Python은 배우기 쉽다. 초보 프로그래머에게 Python은 훌륭한 출발선이 될 수 있으며, 프로그래밍 경험이 있다면 며칠 안에 파이썬의 기초를 배울 수 있다.   간단한 프로그램을 작성하는 방법을 배우는 것은 매우 쉬울 뿐 아니라 복잡한 "엔터프라이즈" 시스템으로 확장할 수도 있다. 아울러 Python은 생산성을 향상시킬 수 있다. @editing

#### Python의 어떤 Version을 배워야 하는가?

수업은 Python 3.x버전을 중심으로 진행한다. 

#### Python 다운로드와 설치

[Python 공식 사이트 다운로드 페이지](https://www.python.org/downloads/)를 통하여 소스코드 및 설치 프로그램을 모든 버전에 대해서 다운로드하여 설치할 수 있다.  2020년 10월 5일부터 3.9 버전을 배포하고 있으며 이 버전에 대한 지원은 2025년 10월까지 예정되어 있다. 파이썬 배포와 관련된 상세한 정보는 [Python 개발자 가이드](https://devguide.python.org/#status-of-python-branches)를 참조할 수 있다.  

Windows 사용자의 경우 https://www.python.org/ftp/python/3.9.2/python-3.9.2-amd64.exe 링크를 이용하여 다운로드 후 설치할 수 있으며, 설치 과정 중 path 정보에 설치하는 경로를 추가하는 선택 옵션을 체크 후 진행하도록 한다.

#### 코드편집기는 어떤 것이 좋을까?

Python을 설치하는 것 외에도 코드 작성을 위한 텍스트 편집기가 필요하다. 편집기는 코드 작성을위한 도구로써 편집기의 기능을 사용하여 코드 작성과 실행 작업의 효율성을 높일 수 있다. 많은 편집기들이 Python을 지원하고 있으니, 프로그램에 대한 경험이 많은 사람들은 적당한 것을 선택하여 사용하면 된다. Python을 막 시작하고 실제 텍스트 편집기에 대한 경험이 많지 않은 초보자라면 Python 설치시 함께 포함된 Python 편집 기능이있는 IDLE를 사용할 수 있다. IDLE 개발 환경은 Windows, Mac 및 Linux에서도 실행된다. 

Python 지원을 제공하는 인기있는 편집기에는 [Emacs](http://ftp.gnu.org/pub/gnu/emacs/windows/), [Atom[](https://atom.io/), [Visual Studio Code[](https://code.visualstudio.com/) 및 [Sublime Text](https://www.sublimetext.com/)가 있으며, 리팩토링 도구와 코드 자동 완성을 지원하는 편집 도구로는 [PyCharm](https://www.jetbrains.com/pycharm/download)과 [Wing Python IDE](https://wingware.com/)도 많이 사용한다. 통합개발환경은 마음대로 선택할 수 있으며, 다음의 사항을 고려하여 선택하도록 한다.

- 파이썬 코드의 구문 강조 기능이 있는가?
- REPL에서 파이썬 코드를 실행하는가?
- 파이썬 코드를 단계별로 실행할 수 있는 디버거를 제공하고 있는가?

#### IDE와 Git/Github 연동

*※ 통합개발환경과 Git/GitHub의 연동을 통한 버전관리 및 공유작업 관리는 수업 시간 중 실습을 통해 정리해 드립니다.*



## □ Software

### Jupyter Notebook

Jupyter Notebook은 라이브 코드, 수식, 시각화 및 설명 텍스트를 포함한 문서를 만들고 공유할 수있는 오픈소스 웹애플리케이션이다. Jupyter Notebook을 사용하여 데이터정리(data cleaning) 및 변환(transformation), 수치 시뮬레이션(numerical simulation), 통계 모델링(statistical modeling), 데이터 시각화(data visualization), 기계 학습(machine learning) 등을 수행할 수 있다.

#### 주요특성

##### 다양한 언어 지원

Jupyter Notebook은 Python, R, Julia, Scala 등을 포함하여 40개 이상의 프로그래밍 언어를 지원한다.

##### notebooks 공유

Notebook은 이메일, Dropbox, GitHub, Jupyter Notebok Viewer를  이용하여 다른 사람들과 편리하게 공유할 수 있다.

##### Interactive Ouput

HTML, 이미지, 비디오, LaTeX 및 사용자 지정 MIME 유형과 같은 풍부한 대화형 출력물을 생성할 수 있다.

##### Big Data Integration

Python, R 및 Scala의 Apache Spark와 같은 빅 데이터 도구를 활용할 수 있다. Pandas, scikit-learn, ggplot2, TensorFlow로 탐색적 데이터분석을 실시할 수 있다. 

#### Jupyter Notebook 설치와 실행

##### conda

```
conda install -c conda-forge notebook
```

##### pip

```
pip install notebook
```

##### Run Jupyter Notebook

```
jupyter notebook
```



### JupyterLab : Jupyter's Next-Generation Notebook Interface

JupyterLab은 Jupyter 노트북, 코드 및 데이터를위한 웹 기반 대화형 개발환경이다. JupyterLab은 데이터과학(data science), 과학컴퓨팅(sicence computing), 기계학습(machine learning)의 광범위한 워크플로우를 지원하는 사용자 인터페이스를 구성하여 제공한다. JupyterLab은 확장 가능하고 새 구성 요소를 추가하고 기존 구성 요소와 통합하는 플러그인을 작성하는 모듈을 지원한다.

#### JupyterLab의 설치와 실행

##### conda

```
conda install -c conda-formge jupyterlab
```

##### pip

```
pip install jupyterlab
```

##### Run JupyterLab

```
jupyter-lab
```



### Anaconda

아나콘다Anaconda는 패키지 관리와 배포를 단순하게 할 목적으로 과학계산(데이터과학, 기계학습 애플리케이션, 대규모 데이터 처리, 예측분석 등)을 위해 파이썬과 R프로그래밍 언어의 free-open source 패포판이다. 패키지 버전들은 패키지 관리시스템 conda를 이용해 관리한다. 아나콘다 배포판은 우니도우, 리눅스, macOS 에 적합한 1,400개 이상의 데이터 과학 패키지를 포함한다.

#### [아나콘다 공식사이트](https://www.anaconda.com/)



### PyPy

PyPy는 CPython을 대체하기 위하여 RPython 언어를 사용하여 만들어진 언어이다.  CPython 대신 사용하는 주된 이유는 속도때문이며  일반적으로 더 빠르게 실행된다.

#### 주요특성

##### 속도

주요 실행 파일은 Just-in-Time 컴파일러와 함께 제공된다. 10-Liners 뿐만 아니라 매우 크고 복잡한 Python 애플리케이션을 포함하여 대부분의 벤치 마크를 실행하는 데 빠른 속도를 보인다.

##### 메모리 사용

수백 MB 이상의 메모리를 많이 사용하는 Python 프로그램은 CPython에서보다 공간을 덜 차지할 수 있다. 그러나 많은 세부 사항에 따라 다르기 때문에 항상 그런 것은 아니다. 또한 기준선이 CPython보다 높다는 것을 주의하자.

##### Stackless

Stackless 및 greenlet에 대한 지원이 PyPy에 통합되었다. 더 자세한 정보는 [링크](http://doc.pypy.org/en/latest/stackless.html)를 통하여 확인할 수 있다.

#### [PyPy 다운로드](https://www.pypy.org/download.html)

#### [PyPy 관련문서](https://doc.pypy.org/en/latest/)

---
[previous: 강의개요 ◀◀](./README.md) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;@ here...  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [▶▶next: 파이썬 1시간에 끝내기 ](./PythonInOneHour.md)
