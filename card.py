"""A playing card deck for Texas Hold'em."""
import random
class Card(): 
    def __init__(self, rank, suit):
        self.rank=rank
        self.suit=suit 
    def __str__(self):
        return "{0} of {1}".format(self.rank, self.suit)
class Suit(): 
    def __init__(self, suitname):
        self.suitname=suitname
    def __str__(self):
        return str(self.suitname)
class Deck():
    def __str__(self):
        return [str(card) for card in self.deck]
    def pop(self):
        return self.deck.pop()
    def shuffle(self):
        return self.deck.shuffle()
    def __init__(self):
        self.deck=[Card(rank, suit) for rank in range(14) for suit in [Diamonds, Spades, Hearts, Clubs]   
Diamonds=Suit('Diamonds')
Spades=Suit('Spades')
Hearts=Suit('Hearts')
Clubs=Suit('Clubs')
d=Deck()
print(d)
