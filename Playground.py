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