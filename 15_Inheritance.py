class Card(object):
    """Represents a standart playing card."""

    suit_names = ['Clubs', 'Hearts', 'Diamonds', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank


    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])


    # def __cmp__(self, other):
    #     # suits
    #     if self.suit > other.suit: return 1
    #     if self.suit < other.suit: return -1
    #
    #     # if suits are the same..check ranks
    #     if self.rank > other.rank: return 1
    #     if self.rank < other.rank: return -1
    #
    #     # if ranks are the same..it's a tie
    #     return 0


    def __cmp__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return cmp(t1, t2)


queen_of_diamonds = Card(1, 12)

card1 = Card(2, 11)
print card1
