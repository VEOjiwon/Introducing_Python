# 1
class Thing():
    pass


print(Thing)
example = Thing()
print(example)


# 2
class Thing2():
    letters = 'abc'


print(Thing2.letters)


# 3
class Thing3():
    def __init__(self):
        self.letters = 'xyz'


print(Thing3().letters)


# 4 + #6 + #7 +#8
class Element():
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    # def dump(self):
    # print(self.name,self.symbol,self.number)
    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number

    # def __str__(self):
    # return self.name +' '+self.symbol +' ' + self.number


hydrogen = Element('Hydrogen', 'H', '1')
print(hydrogen)

# 5
el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': '1'}
hydrogen = Element(el_dict['name'], el_dict['symbol'], el_dict['name'])
hydrogen2 = Element(**el_dict)


# 9
class Bear():
    def eats(self):
        return 'barries'


class Rabbit():
    def eats(self):
        return 'clover'


class Octothrope():
    def eats(self):
        return 'campers'


b = Bear()
r = Rabbit()
o = Octothrope()
print(b.eats(), r.eats(), o.eats())


# 10
class Laser():
    def does(self):
        return 'disintegrate'


class Claw():
    def does(self):
        return 'crush'


class Smartphone():
    def does(self):
        return 'ring'


class Robot():
    def __init__(self):
        self.l = Laser()
        self.c = Claw()
        self.s = Smartphone()

    def does(self):
        print(self.l.does(), self.c.does(), self.s.does())


r = Robot()
r.does()