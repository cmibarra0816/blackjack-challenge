#Blackjack Program - Extra Credit
#Blackjack Outline
    #Deck: Shuffle(), Draw (); Card Class: Suit, Value; Player: Hand, Add_Card, Score, Hit, Hold, Play; Dealer: Inherits from Player


#Import - use for shuffling cards
import random

#Boolean type to know whether play is in hand
playing=False

#Amount for buy-in
chip_pool=100
#Raw Input ("Enter the amount for buy-in:")
print "Your buy-in amount is:", chip_pool

bet=1

restart_phrase: "Press d to deal the cards again, or press q to quit."

#Hearts, Diamonds, Clubs, Spades
suits=("H", "D", "S", "C")
#Possible card ranks
ranking=("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
#Point value dict (duality values defined later)
card_value=("A":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10)
#Card Class
card_class:
    def __init__(self, suit, rank):
        self.suit=suit
        self.rank=rank
    def __str__(self):
        return self.suit+self.rank
    def grab_suit(self):
        return self.suit
    def grab_rank(rank):
        return self.rank
    def draw(self):
        print (self.suit+self.rank)
#Hand Class (duality values defined)
hand_class:
    def __init__(self):
            self.cards=[]
            self.value=0
            self.ace=False
    def __str__(self):
        """Return a string of current composition"""
        hand_comp:""
        













