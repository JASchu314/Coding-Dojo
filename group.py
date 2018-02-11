#1
greeting = "hello"
name = "dojo"
print name , greeting

#2
list = ['wish' , 'mop' , 'bleet' , 'march' , 'jerk']
for i in range(0 , len(list)):
    print list[i]

#3
def nf(num):
    list = []
    for i in range(0,25):
        num *= 2
        list.append(num)
    print list
nf(3)

#4
def funstring(string_param):
    newstr = ''
    for i in range(len(string_param) -1, -1 , -1):
        newstr += string_param[i]
    print newstr
funstring("hello")    
    
x = 10 
x *= 7
y = 30
z = y + x
z *= 3 
z -= y
z /= 27
x = z+y
y = 3
x += y
if x % 2 == 0:
    print True
else: 
    print False

suit = ["hearts", "diamonds", "spades", "clubs"]
value = ["ace", 2, 3, 4, 5, 6 ,7 ,8 ,9 ,10, "jack", "queen", "king"]

#Deck o' Cards
class Cards(object):
    def __init__(self, suit, value):
        self.suit= suit
        self.value = value
    def __str__(self):
        return "{} of {}".format(self.value, self.suit)
class Deck(object):
    def __init__(self):
        self.card_list = []
    def __str__(self):
        for i in self.card_list:
            print i
    def addCard(self,card):
        self.card_list.append(card)
        return self
    def Deal(self, cardlist):
        print self.card_list
        return self
our_cards = Deck()
for i in range(1, 53):
    for s in suit:
        for v in value:
            i = Cards(s,v)
            our_cards.addCard(i)
print our_cards