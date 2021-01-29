import random
import Rules
cards = [['A','2','3','4','5','6','7','8','9','10','J','Q','K'], ['A','2','3','4','5','6','7','8','9','10','J','Q','K'], ['A','2','3','4','5','6','7','8','9','10','J','Q','K'], ['A','2','3','4','5','6','7','8','9','10','J','Q','K']]

def deckShuffle():
	count = 0
	while count != 52:
		ans = input()
		if ans != 'exit':
			num = random.randint(0, len(cards)-1)
			suit = random.randint(0, len(cards[1])-1)
			count += 1
			print('Card: ' + cards[num][suit])
			#print(Rules.drinkingGameRules[rule])
			del cards[num][suit]
			
#deckShuffle()