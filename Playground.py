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

#연습문제 3.8

#3.1
year_list = [i for i in range(1980,1986)]
#print(year_list)

#3.2
print(year_list[3])

#3.3
print(year_list[-1])

#3.4
things = ["mozzarella", "cinderella", "salmonella"]
print(things)

#3.5
print(things[1].capitalize())
print(things)

#3.6
print(things[0].capitalize())

#3.7
things.remove('salmonella')
print(things)

#3.8
suprise = ["Groucho","Chico","Harpo"]

#3.9
suprise[2] = suprise[2].lower()
suprise[-1] = suprise[-1][::-1]
suprise[-1] = suprise[-1].capitalize()
print(suprise)

#3.10
e2f = {'dog' : 'chien','cat':'chat','walrus':'morse'}
print(e2f)

#3.11
print(e2f['walrus'])

#3.12
f2e={}
for k,v in e2f.items():
    f2e[v]=k
print(f2e)

#3.13
print(f2e['chien'])

#3.14
print(list(e2f.keys()))

#3.15
life ={'animals':{'cats':['Henri','Grumpy','Lucy'],'octopi':{},'emus':{}},'plants':{},'other':{}}
print(life)

#3.16
print(list(life.keys()))

#3.17
print(list(life['animals'].keys()))

#3.18
print(life['animals']['cats'])