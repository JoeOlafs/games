import random
import Rules
import Cards
games = ("Icelandic","Casino","Reverse Casino","Dummy Poker","Drinking Game")
num = random.randint(0, len(games)-1)
print(games[num])
if games[num]=="Drinking Game":
	for x in Rules.drinkingGameRules:
		print(x)
	Cards.deckShuffle()