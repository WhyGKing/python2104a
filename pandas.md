#### swcodingschool's classroom
# Pandas 모듈 활용
### Padas 모듈의 정의
- 파이선의 대표적인 데이터 분석 라이브러리
  - 행과 열로 이루어지 ㄴ데이터 객체를 만듦
- 특히 안정적으로 대용량 데이터를 처리하는데 매우 적합(빅데이터)
  - 프로그래밍 언어 R의 DataFrame과 유사
- 빅데이터의 생성, 선택, 연산, 병합, 그룹화, 변형, 그래프 등 엑셀과 유사한 기능을 손쉽게 구현할 수 있음

### Pandas 모듈 설치
```python
pip install pandas
import pandas as pd
```

### Pandas 모듈의 활용
- pandas 모듈이 제공하는 기본적인 자료구조
  - Series
  - DataFrame

#### Series
- 인덱스를 가진 1차원 배열과 같은 자료형
- 기본 인덱스는 정수로 따로 지정할 수 있으며, 파이썬 사전 자료형과 호환 가능


```python
# 실습
import pandas as pd
s = pd.Series([1, 9, -3, 4])
print(s)

print(s.values) #값 확인
print(s.index) # 인덱스 확인
print(s.dtypes) # 자료형 확인
```

    0    1
    1    9
    2   -3
    3    4
    dtype: int64
    [ 1  9 -3  4]
    RangeIndex(start=0, stop=4, step=1)
    int64
    


```python
# 인덱스 지정
s = pd.Series([1, 9, -3, 4], index=['a', 'b', 'c', 'd'])
print(s)
```

    a    1
    b    9
    c   -3
    d    4
    dtype: int64
    


```python
# 사전과 호환
dic = {'A':3000, 'B':6000, 'C':2000, 'D':4000}
s = pd.Series(dic)
print(s)
```

    A    3000
    B    6000
    C    2000
    D    4000
    dtype: int64
    

### DataFrame
- 행과 열을 가진 자료구조로 직접 행과 열에 데이터를 입력하거나, 파이썬의 사전 자료형이나 numpy 모듈의 array로 정의함



```python
df = pd.DataFrame({'A':1., 
                  'B':'2021-05-06',
                   'C':[1,2,3,4],
                   'D':(5,6,7,8),
                   'E':0,
                   'F':'Web'
                  })
print(df)
```

         A           B  C  D  E    F
    0  1.0  2021-05-06  1  5  0  Web
    1  1.0  2021-05-06  2  6  0  Web
    2  1.0  2021-05-06  3  7  0  Web
    3  1.0  2021-05-06  4  8  0  Web
    


```python
# 행
print(df.index)
# 열
print(df.columns)
```

    RangeIndex(start=0, stop=4, step=1)
    Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')
    


```python
data = {'name':['A', 'B', 'C', 'D', 'E'],
       'year':[2017, 2018, 2019, 2020, 2021],
       'points':[3.5, 4.2, 2.6, 7.4, 1.9]}
df = pd.DataFrame(data)
print(df)
```

      name  year  points
    0    A  2017     3.5
    1    B  2018     4.2
    2    C  2019     2.6
    3    D  2020     7.4
    4    E  2021     1.9
    


```python
# 인덱싱[열] 열을 기준으로 데이터 추가 삭제 및 변경 가능
print(df[['year']])
```

       year
    0  2017
    1  2018
    2  2019
    3  2020
    4  2021
    


```python
print(df[['year', 'points']])
```

       year  points
    0  2017     3.5
    1  2018     4.2
    2  2019     2.6
    3  2020     7.4
    4  2021     1.9
    


```python
# 새로운 열 추가
df['new'] = [1,2,3,4,5]
print(df)
```

      name  year  points  new
    0    A  2017     3.5    1
    1    B  2018     4.2    2
    2    C  2019     2.6    3
    3    D  2020     7.4    4
    4    E  2021     1.9    5
    


```python
# 조건을 사용하여 새로운 열 추가
df['past'] = df['year'] < 2020
print(df)
```

      name  year  points  new   past
    0    A  2017     3.5    1   True
    1    B  2018     4.2    2   True
    2    C  2019     2.6    3   True
    3    D  2020     7.4    4  False
    4    E  2021     1.9    5  False
    


```python
# 삭제
del df['past']
print(df)
```

      name  year  points  new
    0    A  2017     3.5    1
    1    B  2018     4.2    2
    2    C  2019     2.6    3
    3    D  2020     7.4    4
    4    E  2021     1.9    5
    


```python
# 인덱싱[행] 행을 기준으로 데이터 추가 및 삭제
data = {'name':['A', 'B', 'C', 'D', 'E'],
       'year':[2017, 2018, 2019, 2020, 2021],
       'points':[3.5, 4.2, 2.6, 7.4, 1.9]}
df = pd.DataFrame(data)
print(df)
```

      name  year  points
    0    A  2017     3.5
    1    B  2018     4.2
    2    C  2019     2.6
    3    D  2020     7.4
    4    E  2021     1.9
    


```python
# 새로운 행 추가
df.loc[5, :] = ['F', 2022, 4.0]
print(df)
```

      name    year  points
    0    A  2017.0     3.5
    1    B  2018.0     4.2
    2    C  2019.0     2.6
    3    D  2020.0     7.4
    4    E  2021.0     1.9
    5    F  2022.0     4.0
    


```python
# 범위 선택
print(df[0:3])
```

      name    year  points
    0    A  2017.0     3.5
    1    B  2018.0     4.2
    2    C  2019.0     2.6
    


```python
#범위 선택, 특정 열
print(df.loc[1:3, 'name'])
```

    1    B
    2    C
    3    D
    Name: name, dtype: object
    


```python
# DataFrame 데이터 분석 : 데이터 분석과 관련 다양한, 함수 제공
# sum: 행 또는 열의 합
# min, max
# mean
# median
# std, var : 표준편차, 분산
# count
# srot_values : 정렬
# corr, cov : 상관계수, 공분산
data = {'name':['A', 'B', 'C', 'D', 'E'],
       'year':[2017, 2018, 2019, 2020, 2021],
       'points':[3.5, 4.2, 2.6, 7.4, 1.9]}
df = pd.DataFrame(data)

# 각 행의 합
print(df.sum(axis=1))

# 각 열의 합
print(df.sum(axis=0))
```

    0    2020.5
    1    2022.2
    2    2021.6
    3    2027.4
    4    2022.9
    dtype: float64
    name      ABCDE
    year      10095
    points     19.6
    dtype: object
    
