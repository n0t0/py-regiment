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

    # def __cmp__(self, other):
    #         # check the suits
    #     if self.suit > other.suit: return 1
    #     if self.suit < other.suit: return -1

    #     # suits are the same... check ranks
    #     if self.rank > other.rank: return 1
    #     if self.rank < other.rank: return -1

    #     # ranks are the same... it's a tie
    #     return 0    


    def __cmp__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return cmp(t1, t2)


queen_of_diamonds = Card(1, 12) # creates a card 
print queen_of_diamonds

card1 = Card(2, 11)
print card1


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

    # NOTE: import random module
    def shuffle(self):
        random.shuffle(self.cards)


    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())


    def deal_hands(self, hand_num):
        hands = []
        for elmt in range(hand_num):
            elmt = Hand('some hand')
            print elmt.label
            hands.append(elmt)
        for item in hands:
            hand.add_card(self.pop_card())
        return hands   
         
            

deck = Deck()
# print deck

# Inheritance

class Hand(Deck):
    """Represents a hand of playing cards."""

    # NOTE: Defining init in a child class overides the parent's -
    def __init__(self, label=""):
        self.cards = []
        self.label = label

hand = Hand('new_hand')
print hand.cards
print hand.label

card = deck.pop_card()
hand.add_card(card)
print hand

hands = deck.deal_hands(4)
print hands

