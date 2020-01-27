print '\n Exercise 1 \n'

class Clock(object):
    
    cities = ['New York', 'London', 'Dubai', 'Tokyo']
    timezones = ['UTC']

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        
    
    # def time_to_int(self):
    #     minutes = self.hour * 60 + self.minute
    #     seconds = minutes * 60 + self.second
    #     return seconds
    #     print seconds
    
    # def __cmp__(self, other):
    #     # check hours 
    #     # if self.hour > other.hour: return 1 
    #     if self.hour > other.hour: print 'hour' 
    #     if self.hour < other.hour: return -1
    #     # if hours are tied - check minutes 
    #     if self.minute > other.minute: print 'minutes' 
    #     if self.minute < other.minute: return -1
    #     # if minutes are tied - check seconds 
    #     if self.second > other.second: return 1 
    #     if self.second < other.second: return -1 
    #     # exact same time
    #     return 0

    def print_time(self):
        print '{:02d}:{:02d}:{:02d}'.format(self.hour, self.minute, self.second)

    def __cmp__(self, other):
        t1 = self.hour, self.minute, self.second
        t2 = other.hour, other.minute, other.second
        return cmp(t1, t2)

t1 = Clock(11,4,2)
t2 = Clock(11,2,2)
t1.print_time()
t2.print_time()
   
print t1 > t2 

print '\n Exercise 2 \n'

import random 


class Card(object):
    """Represents a standart playing card."""

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        # default card is 2 of Clubs 
        self.suit = suit
        self.rank = rank


    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __cmp__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return cmp(t1, t2)


class Deck(object):
    

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(14):
                card = Card(suit, rank)
                self.cards.append(card)


    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)


    def pop_card(self):
        return self.cards.pop()


    def add_card(self, card):
        self.cards.append(card)

   
    def shuffle(self):
        random.shuffle(self.cards)


    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def sort_cards(self):
        self.cards.sort()
        

deck = Deck()
deck.shuffle()
print deck
deck.sort_cards()
print 'sorting....'
print deck

print '\n Exercise 3 \n'

import random

class Deck(object):


    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(14):
                card = Card(suit, rank)
                self.cards.append(card)


    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)


    def pop_card(self):
        return self.cards.pop()


    def add_card(self, card):
        self.cards.append(card)


    def shuffle(self):
        random.shuffle(self.cards)


    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())


    def deal_hands(self, hands_num, cards_num):
        hands = []
        for elmt in range(hands_num):
            elmt = Hand('some hand')
            print elmt.label
            hands.append(elmt)
        for item in hands:
            for i in range(cards_num):
                hand.add_card(self.pop_card())
        return hands   
         
deck = Deck()
import itertools

class Hand(Deck):
    """Represents a hand of playing cards."""
    # newid = itertools.count().next
    # class_counter = 0
    def __init__(self, label=""):
        # self.id = Hand().newid
        self.cards = []
        self.label = label
        # self.id = Hand.class_counter
        # Hand.class_counter += 1 

hand = Hand('new_hand')
print hand.cards
print hand.label

card = deck.pop_card()
hand.add_card(card)
print hand

hands = deck.deal_hands(4, 5)
print hands


print '\n Exercise 3 \n'


print '\n Exercise 4 \n'

