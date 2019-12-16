'''
drinks = {
        'martini' : {'vodka','vermouth'},
        'black russian' : {'vodka', 'kahlua'},
        'white russian' : {'cream', 'kahlua', 'vodka'},
        'manhattan' : {'rye', 'vermouth', 'bitters'},
        'screwdriver' : {'orange juice', 'vodka'}
}

for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)

print("------------------------------------")

for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
        print(name)

for name, contents in drinks.items():
    if 'vodka' in contents and not contents & ('vermouth','cream'):
        print(name)

'''



# generater

def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step


ranger = my_range  # function

rnager = my_range()  # genrater


############################################################################

# decorater   // example, using for function debugging

# 데커레이터 함수 선언
def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result', result)
        return result

    return new_function


# 데커레이터를 이용할 함수 선언
def add_ints(a, b):
    return a + b


# 데커레이터를 수동으로 할당
cooler_add_ints = document_it(add_ints)

# 더커레이터가 포함된 함수 실행
cooler_add_ints(3, 5)


# 데커레이터 사용법

@document_it  # 사용하고 싶은 함수에 @(데커레이터 이름)을 추가만 해주면 끝...
def add_ints(a, b):
    return (a + b)


add_ints(1, 5)  # 결과 확인 가능

# 데커레이터는 여러개 가질 수 있다... 함수 위에 @ 두개 적어주면 됨
# 이 떄 순서는 함수와 가까운 데커레이터 부터 실해 (함수 바로 위 데커레이터)

############################################################################

# Handle the exception

short_list = [1, 2, 3]
while True:
    value = input('Position [q to quit]? ')
    if value == 'q':
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print('Bad index:', position)
    except Exception as other:
        print('Something else broke', other)


##########################################################################

# use the deque from import // from collections import deque


def palindrome(word):
    """
    determine whether palindrome word or not
    :param word: 
    :return:
    """
    from collections import deque
    dq = deque(word)
    while len(dq) > 1 :
        if dq.popleft() !=dq.pop():
            return False
    return True

print(palindrome('rasr'))

############################################################################

# 상속 예제
class Car():
    def exclaim(self):
        print("I'm a Car!")


class Yugo(Car):
    pass


give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_yugo.exclaim()


# 오버라이드 예제
class Car():
    def exclaim(self):
        print("I'm a Car!")


class Yugo(Car):
    def exclaim(self):
        print("I'm a yugo")

    def need_a_push(self):
        print("A little help here?")


give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()
give_me_a_yugo.need_a_push()


# super 예제
class Person():
    def __init__(self, name):
        self.name = name


class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email


hunter = EmailPerson('Elmer Fudd', 'EF@naver.com')


# getter, setter
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name

    def get_name(self):
        print('inside the getter')
        return self.hidden_name

    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

    name = property(get_name, set_name)


# getter, setter using decerater

class Circle():
    def __init__(self, radius):
        self.radius = radius

    @property  # 외부에서 diameter를 수정 못하게 만듬
    def diameter(self):
        return 2 * self.radius


# private and mangling

class Duck():
    def __init__(self, input_name):
        self.__name = input_name

    @property
    def name(self):
        print('inside the getter')
        return self.__name

    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name


# class method

class A():
    count = 0

    def __init__(self):
        A.count += 1

    def exclaim(self):
        print("I'm an A!")

    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.")


# duck typing

class BabblingBrook():
    def who(self):
        return 'Brook'

    def says(self):
        return 'Babble'


def who_says(obj):
    print(obj.who(), 'says', obj.says())


hunter = BabblingBrook()
who_says(hunter)

#named tuple

from collections import namedtuple
Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')


##############################################################################################

#section 7

#unicode things

import unicodedata

def unicode_test(value):
    #import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s",name="%s",value2="%s"' %(value, name, value2))

#unicode_test('A')
#unicode_test('$')
#unicode_test('\u00a2')
#unicode_test('\u20ac')
#unicode_test('\u2603')
#unicode_test('\u00e9')

print(unicodedata.name('\u00e9'))
print(unicodedata.lookup('LATIN SMALL LETTER E WITH ACUTE'))

place = 'caf\u00e9'

place2 = 'caf\N{LATIN SMALL LETTER E WITH ACUTE}'

#encoding
snowman = '\u2603'
print(len(snowman))
print(snowman)
ds = snowman.encode('utf-8')
print(len(ds))
print(ds)
#ds2 = snowman.encode('ascii') -> error!!
ds2 = snowman.encode('ascii','ignore')#replace, bakslashreplace, xmlcharrefreplace 등의 옵션 존재

#decoding

place = 'caf\u00e9'
print(type(place))

place_bytes = place.encode('utf-8')
print(type(place_bytes))

place_bytes.decode('utf-8')

#인코딩과 디코딩 타입은 같아야 한다... 가급적이면 utf-8타입을 사용하자


#formating

#old version
print("my height is %d and my age is %d"%(180,23))

#new version
n=42
f=7.03
s='string cheese'
print('{} {} {}'.format(n,f,s))

#순서지정
print('{1} {2} {0}'.format(n,f,s))


#딕셔너리 인자
print('{n} {f} {s}'.format(n=42,f=8.2,s='string'))

#타입 지정자
print('{0:d} {1:f} {2:s}'.format(n,f,s))

##더 자세한 것들은 책 p210쪽 을 참고하시길


# 정규표현식
import re

# 1 match사용법
result = re.match('You', 'Young Frankenstein')

# 2 compile해서 match
youpattern = re.compile('You')
result2 = youpattern.match('Young Frankenstein')

# 3 match한 후 매칭 되면 문자열로 출력하기
source = 'Young Frankenstein'
m = re.match('You', source)
if m:
    print(m.group())

m = re.match('Frank', source)  # match는 패턴이 소스의 처음에 있을 때만 반환
if m:
    print(m.group())

# 4 search와 와일드 카드 .* 사용
m = re.search('Frank', source)  # search는 패턴이 어디있든 매칭가능
if m:
    print(m.group())

m = re.match('.*Frank', source)  # 1. .은 한 문자 2. *은 이전 패턴이 여러개 올 수 있음 3. Frank가 포함되어있어야 함
if m:  # .* \n을 제외한 모든 문자가 여러개 올 수 있음
    print(m.group())

m = re.search('Frank', source)
if m:
    print(m.group())

# 5 findall
m = re.findall('n', source)
print(m)
m = re.findall('n.', source)
print(m)
m = re.findall('n.?', source)  # ?는 0또는 1회를 의미 .. 마지막패턴도 찾을 수 있게 된다
print(m)

# 6 split
m = re.split('n', source)
print(m)

# 7 sub
m = re.sub('n', '?', source)
print(m)

# 8 패턴 지정자
source = '''I wish I may, I wish I might Have a dish of fish tonight.'''
print(re.findall('wish', source))

print(re.findall('wish|fish', source))

print(re.findall('^wish', source))

print(re.findall('^I wish', source))

print(re.findall('fish$', source))

print(re.findall('fish tonight.$', source))

print(re.findall('fish tonight\.$', source))

print(re.findall('[wf]ish', source))

print(re.findall('[wsh]+', source))

print(re.findall('I (?=wish)', source))

print(re.findall('(?<=I) wish', source))

print(re.findall(r'\bfish', source))  # 정규식 시작시에는 항상 문자 r(raw string)을 사용해서 이스케이프 문자 충돌 피해야함

# 9 패턴 결과 매칭하기
m = re.search(r'(. dish\b).*(\bfish)', source)
print(m.group())
print(m.groups())

m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)
print(m.group())
print(m.groups())
print(m.group('DISH'))
print(m.group('FISH'))


##########################################################################################3

# section 8

# file i.o.
poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''

fout = open('relativity', 'wt')
# fout.write(poem)
# print(poem, file=fout)
size = len(poem)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(poem[offset:offset + chunk])
    offset += chunk

fout.close()

fin = open('relativity', 'rt')
poem = fin.read()
fin.close()
print(len(poem))

fin = open('relativity', 'rt')
lines = fin.readlines()

for line in fin:
    poem += line
fin.close()
print(len(poem))

# binary handle
bdata = bytes(range(0, 256))
fout = open('bfile', 'wb')
fout.write(bdata)
fout.close()

# 자동으로 파일 닫기
with open('relativity', 'wt') as fout:
    fout.write(poem)

# 파일위치 찾기
fin = open('bfile', 'rb')
print(fin.tell())
print(fin.seek(250))
bdata = fin.read()

# CSV - JSON
menu = \
    {
        "breakfast": {
            "hours": "7-11",
            "items": {
                "breakfast burritos": "$6.00",
                "pancakes": "$4.00"
            }
        },
        "lunch": {
            "hours": "11-3",
            "items": {
                "humburger": "$5.00"
            }
        },
        "dinner": {
            "hours": "3-10",
            "itmes": {
                "spaghetti": "$8.00"
            }
        }
    }

import json

menu_json = json.dumps(menu)
# print(menu_json)

menu2 = json.loads(menu_json)
# print(menu2)

import datetime

now = datetime.datetime.utcnow()
# print(now)
# json.dumps(now) /json값이 이해할 수 없는 타입이다 json 모듈에서는 날짜 또는 시간 타입을 정의하지 않았음

now_str = str(now)
json.dumps(now_str)

from time import mktime

now_epoch = int(mktime(now.timetuple()))
print(json.dumps(now_epoch))


####################################################################


#DB - SQLITE3
import sqlite3
conn = sqlite3.connect('enterprise.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE zoo
            (critter VARCHAR(20) PRIMARY KEY,
            count INT,
            damages FLOAT)''')


curs.execute('INSERT INTO zoo Values("duck",5,0.0)')
curs.execute('INSERT INTO zoo Values("bear",2,1000.0)')

ins = 'INSERT INTO zoo (critter, count, damages) VALUES(?, ?, ?)'
curs.execute(ins, ('weasel',1,2000.0))

curs.execute('SELECT * FROM zoo')
rows = curs.fetchall()
print(rows)

curs.execute('SELECT * from zoo ORDER BY count DESC')
curs.fetchall()

#한 마리당 비용이 가장 많이 드는 동물
curs.execute('''SELECT * FROM zoo WHERE
DAMAGES = (SELECT MAX (damages) FROM zoo)''')
curs.fetchall()

curs.close()
conn.close()