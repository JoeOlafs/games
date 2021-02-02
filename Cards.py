import random
import Rules
cards = [['A','2','3','4','5','6','7','8','9','10','J','Q','K'], ['A','2','3','4','5','6','7','8','9','10','J','Q','K'], ['A','2','3','4','5','6','7','8','9','10','J','Q','K'], ['A','2','3','4','5','6','7','8','9','10','J','Q','K']]
suits = ['Hearts','Spades','Diamonds','Clubs']
def deckShuffle():
	count = 0
	while count != 52:
		ans = input()
		if ans != 'exit':
			suit = random.randint(0, len(cards)-1)
			num = random.randint(0, len(cards[suit])-1)
			count += 1
			print('Card: ' + cards[suit][num] + ' of ' + suits[suit])
			#print('Count: ' + str(count))
			Rules.PrintRule(cards[suit][num])
			#print(Rules.drinkingGameRules[rule])
			del cards[suit][num]
			
deckShuffle()
