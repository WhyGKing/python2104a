###### [ previous : Python Overview ◀◀](./PythonOverview.md) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;@ here... &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;▶▶ next :  수업을 통한 상세 설명과 실습을 통해 확인하세요.
---
###### ▣ swcodingschool's Coding Class
# Python in 1Hour

*1시간 안에 Python을 날로 먹어보는 따라해보기 실습. Python 프로그래밍 기초 및 응용과정의 수업 내용을 일부 발췌하여 구성하였습니다.*



#### Strings

작은 따옴표(') 또는 큰 따옴표(")를 사용하여 문자열을 표현할 수 있다.

```python
# string 
# single and double qoutes are same in python
a = "I ♥ swcodingschool"
b = '소프트웨에코딩스쿨 ♥'
print(a, b)
```



#### Triple Quotes for Multi-Line String

여러 행에 걸치 문자열을 표현하기 위해서는 큰 따옴표(")를 3개 연속하여 사용한다.

```python
# triple qoutes for multi-line string
a = """I ♥ swcodingschool. 
소프트웨에코딩스쿨 
사랑해요 ♥"""
print(a)
```



#### subtring, length

문자열의 부분 추출은 str [begin_index : end_index]와 같이 대괄호를 사용한다. 인덱스는 0부터 시작하며, 글자의 위치를 표현하고, 음수로 표현할 경우에는 문자열의 끝부터 세는 것이다.

```python
# substring, index사용
a = "0123456789"
print(a[1:4]) # 123
# 스트링의 길이는 len()함수 사용
print(len(a)) # 10
# 문자열은 + 기호를 사용하여 결합join
print("문자열" + "결합") #문자열의결합
# 문자열은 * 기호를 사용하여 반복repeat
print("문자열"*3) #문자열문자열문자열
```

*※ String을 다루는 더 많은 내용은 수업시간을 통해 정리해 드립니다.*



#### Artihmetic

파이썬을 사용하여 기본적인 산술연산을 수행하고 즉시 결과를 확인할 수 있다.

```python
print(3 + 4) # 7
print(3 - 4) # -1
print(3 + - 4)   # -1
print(3 * 4) # 12

print(2 ** 3) # 8 power

print(11 / 5) # 2.2  (in python 2, this would be 2)
print(11 // 5)    # 2 (quotient)
print(11 % 5) # 1 remainder (modulo)

print(divmod(11, 5))  # (2, 1) quotient and remainder
```



#### Convert to int, float, string

파이썬은 int, float, string 타입간의 자동 변환을 제공하지 않는다.

```python
print(int(3.2)) #Convert to int: int(3.2)
print(float(3)) #Convert to float: float(3)
```

*※ String의 format과 관련한 더 많은 내용은 수업시간을 통해 정리해 드립니다.*



#### Assignment Operators 대입연산자

```python
# add and assign
c = 0
c += 1
print(c)    # 1

# substract and assign
c = 0
c -= 2
print(c)    # -2

# multiply and assign
c = 2
c *= 3
print(c)    # 6

# exponent and assign
c = 3
c **= 2
print(c)    # 9

# divide and assign
c = 7
c /= 2
print(c)    # 3.5

# modulus (remainder) and assign
c = 13
c %= 5
print(c)    # 3

# quotient and assign
c = 13
c //= 5
print(c)    # 2
```

파이썬은 증감연산자 ++, --를 제공하지 않는다. 

*※ Python의 Operator연산자와 관련한 더 많은 내용은 수업시간을 통해 정리해 드립니다.*



#### True and False

False, 0, 빈 문자열, 빈 배열,…과 같은 것들은 모두 False로 평가된다. 다음은 False로 평가된다.

- `False`. A builtin Boolean type.
- `None`. A builtin type.
- `0`. Zero.
- `0.0`. Zero, float.
- `""`. Empty string.
- `[]`. Empty list.
- `()`. Empty tuple.
- `{}`. Empty dictionary.
- `set([])`. Empty set.
- `frozenset([])`. Empty frozen set.

```python
my_thing = []

if my_thing:
    print("yes")
else:
    print("no")
```



#### Conditional: if then else

```python
x = -1
if x<0:
    print('neg')
elif x==0:
    print('zero')
elif x==1:
    print('one')
else:
    print('other')

# elif은 필요에 따라 생략할 수 있다.
```



#### Loop, Iteration

```python
a = list(range(1,5)) # creates a list from 1 to 4. (does NOT include the end)

for x in a:
    if x == 3:
        print(x)

# prints 3
```

`range(m, n)` 함수는 m 부터  n-1까지의 연속된 숫자를 생성한다.

Python은 루프를 벗어나기 위한  `break` 와 루프의 반복을 위한 `continue` 를 제공한다.

- `break` → exit loop.
- `continue` → skip code and start the next iteration.

```python
for x in range(1,9):
    print(x)
    if x == 4:
        break

# 1
# 2
# 3
# 4
```

while 루프의 예

```python
x = 1
while x <= 5:
    print(x)
    x += 1
```



#### List

리스트를 생성하기 위해서는

```python
a = [0, 1, 2, "more", 4, 5, 6]
print(a)
```

카운트의 요소를 세기 위해서는

```python
a = ["more", 4, 6]
print(len(a)) # prints 3
```

리스트 내의 특정 요소에 접근하기 위해서는 list[인덱스] 구문을 사용한다. 인덱스는 0부터 시작하고, 음수를 사용하면 뒤에서 부터 카운트할 수 있으며 가장 끝의 요소는 인덱스 -1이다.

```python
a = ["more", 4, 6]
print(a[1]) # prints 4
```

리스트내 연속된 요소를 추출(보통 슬라이스라고 함)하려면  리스트명[시작인덱스:마지막인덱스:인덱스증감값]구문을 사용한다. 이 때 마지막인덱스 요소는 포함하지 않는다. 예를 들면 mylist[2:4]는 3개가 아닌 두 개 요소를 반환한다.

```python
a = ["zero", "one", "two", "three", "four", "five", "six"]
print(a[2:4])   # prints ["two", "three"]
```

리스트의 특정 요소를 수정하리 위해서는 list[인덱스] = 새로운값 과 같이 사용한다.

```python
xx = ["a", "b", "c"]
xx[2] = "two"
print(xx) # → ['a', 'b', 'two']
```

리스트 슬라이스(연속 시퀀스)는 목록에 직접 할당하여 변경할 수 있다. 슬라이스의 길이가 새 목록의 길이와 반드시 일치할 필요는 없다.

```python
xx = [ "b0", "b1", "b2", "b3", "b4", "b5", "b6"]
xx[0:6] = ["two", "three"]
print(xx)   # ['two', 'three', 'b6']
```

중첩된 리스트. 리스트는 임의로 중첩될 수 있다. 중첩된 목록의 요소를 가져오려면 대괄호를 추가로 사용한다.

```python
a = [3, 4, [7, 8]]
print(a[2][1])    # returns 8
```

리스트 결합. 리스트는 플러스 기호(+)를 이용하여 결합할 수 있다.

```python
b = ["a", "b"] + [7, 6]
print(b)    # prints ['a', 'b', 7, 6]
```

*※ List와 관련한 더 많은 내용은 수업시간을 통해 정리해 드립니다.*



#### Tuple

파이썬에는 리스트와 비슷한 튜플 타입이 있다. 리스트와 달리 새로운 요소를 추가하거나 기존 요소를 삭제하는 것을 제외하고는 리스트와 아주 유사하다. 리스트는 대괄호를 사용하여 정의하는데 비하여  tuple은 둥근 괄호(  )를 사용하여 정의할 수 있다.

```python
# tuple
t1 = (3, 4 , 5) # a tuple of 3 elements. paren optional when not ambiguous
print(t1) # (3, 4 , 5)
print(t1[0])    # 3
```

```python
# nested tuple
t2 = ((3,8), (4,9), ("a", 5, 5))
print(t2[0])   # (3,8)
print(t2[0][0])    # 3
```

```python
# a list of tuples
t3 = [(3,8), (4,9), (2,1)]
print(t3[0])   # (3,8)
print(t3[0][0])    # 3
```

*※ Tuple과 관련한 더 많은 내용은 수업시간을 통해 정리해 드립니다.*



#### Python Sequence Types 연속타입

Python은 string, list, tuple과 같은 데이터형을  "시퀀스 타입"이라 한다. 모두 같은 메서드를 가지고 있으며, 다음은 시퀀스 타입에 사용할 수있는 연산의 예이다.

```python
# operations on sequence types

# a list
ss = [0, 1, 2, 3]

# length
print(len(ss)) # 4

# ith item
print(ss[0]) # 0

# slice of items
print(ss[0:3])    # [0, 1, 2]

# slice of items with jump step
print(ss[0:10:2]) # [0, 2]

# check if a element exist
print(3 in ss)    # True. (or False)

# check if a element does NOT exist
print(3 not in ss) # False

# concatenation
print(ss + ss)   # [0, 1, 2, 3, 0, 1, 2, 3]

# repeat
print(ss * 2)    # [0, 1, 2, 3, 0, 1, 2, 3]

# smallest item
print(min(ss))    # 0

# largest item
print(max(ss))    # 3

# index of the first occurrence
print(ss.index(3))   # 3

# total number of occurrences
print(ss.count(3))   # 1
```



#### Dictionary : 키와 값의 쌍

Python의 키순 목록을 Dictionary라 한다 (다른 언어에서는 해시 테이블 또는 연관 목록이라고 함). 순서가 지정되지 않은 쌍 목록이며 각 쌍은 키와 값으로 구성한다.

```python
# define a keyed list
aa = {"john":3, "mary":4, "joe":5, "vicky":7}

# getting value from a key
print(aa["mary"])
# 4

# add a entry
aa["pretty"] = 99

# delete a entry
del aa["vicky"]

print(aa)
# {'john': 3, 'mary': 4, 'joe': 5, 'pretty': 99}

# get keys
print(list(aa.keys()))
# ['john', 'mary', 'joe', 'pretty']

# get values
print(list(aa.values()))
# [3, 4, 5, 99]

# check if a key exists
print("is mary there:", "mary" in aa)
# is mary there: True
```



#### List를 사용한 반복 Loop

다음 예제는 요소별로 목록 전체를 탐색하는 것이다. 

```python
myList = ['one', 'two', 'three', '∞']

for x in myList:
     print(x)
```

리스트를 반복하며, 요소의 인덱스와 값 모두를 출력할 수도 있다.

```python
myList = ['one', 'two', 'three', '∞']
for i, v in enumerate(myList):
     print(i, v)

# 0 one
# 1 two
# 2 three
# 3 ∞
```



#### Dictionary를 사용한 반복 Loop

```python
myDict = {"john":3, 'mary':4, 'joe':5, 'vicky':7}

for k, v in list(myDict.items()):
     print(k, v)

# output

# joe 5
# john 3
# mary 4
# vicky 7
```

*※  List, Dictionalry와 관련한 더 많은 내용은 수업시간을 통해 정리해 드립니다.*



#### Module

python의 라이브러리를 모듈이라 한다.

```python
# import the standard module named os
import os

# example of using a function
print('current dir is:', os.getcwd())
```

*※  List 모듈, Search Path, 기본 모듈과 관련한 더 많은 내용은 수업시간을 통해 정리해 드립니다.*



#### Functions

다음은 함수 정의 및 사용 예제이다.

```python
def myFun(x,y):
     """myFun returns x+y."""
     result = x+y
     return result

print(myFun(3,4)) # prints 7
```

*※  함수와 관련한 더 많은 내용은 수업시간을 통해 정리해 드립니다.*

#### Class, Object

```python
# example of a class, and create a instance of it

# define a class
class X1:
    "A class example"

    ii = 1  # a class variable

    # This method defines 1 parameter, the x.
    def gg(self, x):
        return x + 1

# create a object of the class X1
# This is called “instantiating a class”.
xx = X1()

# Data or functions defined in a class are called the class's attributes or methods.
# To access them, append a dot and their name after the object's name.

# access a class variable
print(xx.ii)
# 1

# call a method
print(xx.gg(4))
# 5
```

*※  파이썬 객체지향 프로그래밍과 관련한 더 많은 내용은 수업시간을 통해 정리해 드립니다.*

#### Wrting a Module 모듈 작성

다음 코드는 기본적인 예제이다. 다음의 코드를 작성하고 파일명을 mymodule.py로 하여 저장한다.

```python
def f1(n):
    return n+1
```

다른 파일에서 다음과 같이 코드를 작성한다. 다른 모듈을  로드하려면 import import module_name을 사용하고 다른 파일에서 정의된 함수를 호출하려면 module_name.function_name을 사용한다.

```python
import mymodule # import the module

print(mymodule.f1(5)) # calling its function. prints 6
print(mymodule.__name__)   # list its functions and variables
```
*※  모듈과 패키지 활용과 관련한 더 많은 내용은 수업시간을 통해 정리해 드립니다.*

---

###### [ previous : Python Overview ◀◀](./PythonOverview.md) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;@ here...  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;▶▶ next :  수업을 통한 상세 설명과 실습을 통해 확인하세요.