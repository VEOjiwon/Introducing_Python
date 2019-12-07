#Section4 연습문제

#4.1
guess_me = 7

if guess_me < 7 : print("too low")
elif guess_me > 7 : print("too high")
else : print("just right")

#4.2
guess_me = 7
start = 1

while True:
    if start < guess_me : print('too low')
    elif guess_me == start : print('found it!'); break
    elif start > guess_me : print('oops'); break
    start+=1

# 4.3

l = [x for x in range(3, -1, -1)]
for i in l:
    print(i)

# 4.4

l2 = [x for x in range(10) if x % 2 == 0]
print(l2)

# 4.5
squares = {x: x ** 2 for x in range(10)}
print(squares)

# 4.6
s = {x for x in range(10) if x % 2 == 1}
print(s)

# 4.7
for i in ('Got %s' % x for x in range(10)):
    print(i)


# 4.8
def good():
    return ['Harry', 'Ron', 'Hermione']


for i in good():
    print(i)


# 4.9
def get_odds():
    for x in range(1, 10, 2): yield x


for count, number in enumerate(get_odds(), 1):
    """
    enumerate 함수는 순서가 있는 자료형(list, set, tuple, dictionary, string)을 입력으로 받아 
    인덱스 값을 포함하는 enumerate 객체를 리턴합니다
    두번째 인자는 숫자 몇 부터 세기 시작할 것인지 셋팅합니다
    """
    if count == 3: print("The third odd number is ", number);break


# 4.10
def doc(func):
    def new_func(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result

    return new_func


@doc
def just():
    print("Hard day")


# 4.11
class OopsException(Exception):
    pass


try:
    raise OopsException()
except OopsException:
    print('Caught an oops')


#4.12
titles = ['Creature of habit','Crewel Fate']
plots = ['Anun turns into a mon ster', 'A haunted yarn shop']


#dic = {a:b for a,b in zip(titles,plots)}
dic = dict(zip(titles,plots))