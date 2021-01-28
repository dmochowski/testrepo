import random

colors = ['h','d','c','s']
figures = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']

allCards = []

for f in figures:
    for c in colors:
        allCards.append("%s:%s" % (f,c))
        #print(allCards)

random.shuffle(allCards)
print(allCards)

player1 = []
player2 = []

max = len(allCards)

for i in range(max):
    if i %  2 == 0: #jesli parzysta
        player1.append(allCards[i])
    else:
        player2.append(allCards[i])

print("gracz 1 =", player1, "\ngracz 2 =", player2)

player1 = allCards[:26] # wyswietla karty do 26
player2 = allCards[26:] # wyswietla karty od 26
print(player1)
print(player2)
