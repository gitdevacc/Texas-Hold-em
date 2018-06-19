import card
class Table(): 
    def __init__(self):
        self.deck=Deck()
        self.deck.shuffle()
        self.middle=[self.deck.pop(),self.deck.pop(),self.deck.pop()]
    def deal_hand(self):
        if len(d)!=0:
            return [self.deck.pop(),self.deck.pop()]
        else:
            self.deck=Deck()
    def table_middle(self):
        print('Current cards in middle:', self.middle)
        print('Please place your bets.')
        if len(self.middle)<=5:
            self.middle.append(self.deck.pop())
            print('Shared card has been dealt has been dealt. Current cards in middle:', self.middle)
            return self.middle
        else:
            raise Exception("Middle of table can only have five cards")
    def return_cards(self, hand):
        self.deck.extend(hand)
        if len(self.deck)==52:
            self.deck.shuffle()
        else:
            pass
    #def evaluate_hand(self, hand): #under progress DO NOT TOUCH 
class Hand():
    def __init__(self):
        t=Table()
        self.hand=[t.deal_hand()]
        self.current_bet=0
    def __getitem__(self, index):
        return self.hand[index]
    def __str__(self):
        return [str(card) for card in self.hand]
    def check_double(self):
        if self.hand[0]==self.hand[1]:
            return True
    def card_total(self):
        a=[card.points() for card in self.hand]
        return sum(a)
    def fold(self):
        print('Fold. Waiting for next game...')
        t.return_cards(self.hand)
        self.hand=[]
    def update_betamount(self, higherbet):
        if higherbet<=self.current_bet: 
            return False
        elif isinstance(higherbet, int)==False: 
            raise Exception("Bet must be an integer.")
        else:
            self.current_bet=higherbet
class Player(Hand):
    def __init__(self):
        h=Hand()
    def place_bet(self, amount):
        self.bet_amount=amount
        print("Bet", amount)
    def check(self):
        
class AIPlayer(Player):
    def initial_bet_strategy(self):
        self.bet_amount=5
        if h.check_double()==True:
            self.bet_amount*2
        else: 
            pass
    def fold_strategy(self):
        if 
    

    

        
        

    
    