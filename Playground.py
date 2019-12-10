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