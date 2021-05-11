```python
#
# 파이썬 웹 크롤링을 이용하여, 데이터를 수집하고 분석하는 방법을 알아본다.
#
# 필요로 하는 패키지, 모듈, 클래스 등을 import
#
#
import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# 분석 대상 데이터를 가져올 소스 사이트
# http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun=

# requests.get() 이용, 소스 사이트를 가져온다.
source = requests.get('http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun=')
# BeautifulSoup(소스.content, 파서) 이용, htmp.parser
soup = BeautifulSoup(source.content, 'html.parser')

# 시도별 발생현황, 데이터를 가진 테이블을 찾는다.
# 검사 결과, <table class="num, midsize">
table = soup.find('table', {'class':'midsize'})
table = soup.find('tbody')

data = []

for tr in table.find_all('tr'):
    tds = list(tr.find_all('td'))
    rowdata = []
    for td in tds:
        rowdata.append(td.text.replace(',',''))
    # 한 행 구성
    #print(rowdata)
    data.append(rowdata)

# print(data)
# data를 dataframe으로 변환
column_name = ['합계','국내발생','해외유입','확진환자','격리중','격리해제','사망자','발생률']
index_name = ['합계','서울','부산','대구','인천','광주','대전','울산','세종','경기','강원','충북','충남','전북','전남','경북','경남','제주','검역']
df = DataFrame(data,columns=column_name, index=index_name)
print(df)
```

         합계 국내발생 해외유입    확진환자   격리중    격리해제   사망자     발생률
    합계  511  483   28  128283  7687  118717  1879  247.42
    서울  163  163    0   39895  2692   36739   464  409.87
    부산   14   13    1    5286   284    4880   122  154.93
    대구    8    8    0    9448   111    9116   221  387.77
    인천   21   20    1    5839   185    5594    60  197.52
    광주   24   23    1    2518   107    2389    22  172.86
    대전    7    7    0    1835   130    1685    20  124.48
    울산   19   19    0    2247   386    1823    38  195.90
    세종    0    0    0     386    27     358     1  112.76
    경기  138  127   11   35852  2019   33225   608  270.57
    강원   12   12    0    2843   184    2609    50  184.55
    충북    4    4    0    2708   112    2531    65  169.31
    충남   18   18    0    3175   181    2958    36  149.59
    전북   12   12    0    2033   115    1860    58  111.87
    전남   10   10    0    1178   141    1026    11   63.17
    경북   15   15    0    4352   294    3979    79  163.45
    경남   10    9    1    4268   367    3882    19  126.97
    제주   24   23    1     816   110     705     1  121.66
    검역   12    0   12    3604   242    3358     4       -
    
