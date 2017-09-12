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

queen_of_diamonds = Card(1, 12)

card1 = Card(2, 11)
print card1
