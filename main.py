import random
import Rules
games = ("icelandic","casino","reverse casino","dummy poker","drinking game")
num = random.randint(0, len(games)-1)
print(games[num])
if games[num]=="drinking game":
	for x in Rules.rules:
		print(x)