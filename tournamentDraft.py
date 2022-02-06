from random import randrange

def lowestReach(factions):
    reach = {
    "marquise" : 10,
    "duchy" : 8,
    "eyrie" : 7,
    "vagabond" : 5,
    "riverfolk" : 5,
    "woodland" : 3,
    "corvid" : 3,
    "lizard" : 2,
    "vagabond2" : 2,
    "warlord" : 9,
    "keepers" : 8
    }
    lowestReach = factions[0]
    for i in range(1, len(factions)):
        if reach[lowestReach] > reach[factions[i]]:
            lowestReach = factions[i]
    return lowestReach

white = [
    "vagabond",
    "riverfolk",
    "woodland",
    "corvid",
    "lizard",
    "vagabond2"
]
red = [
    "marquise",
    "duchy",
    "eyrie",
    "warlord",
    "keepers"
]

numFactions = int(input("Please input the number of players playing: "))

draft = []
redfacs = 1
draft.append(red.pop(randrange(len(red))))
factions = red + white

for i in range(numFactions):
    faction = factions.pop(randrange(len(factions)))
    if faction in red:
        redfacs += 1
    draft.append(faction)

locked = redfacs == 1
lowestReach = lowestReach(draft)
draft.remove(lowestReach)
print("Factions:")
for i in range(numFactions):
    print(draft[i])
if(locked):
    print("LOCKED:")
print(lowestReach)
