from random import randrange

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

def getReach(faction):
    return reach[faction]

white = [
    "vagabond",
    "riverfolk",
    "woodland",
    "corvid",
    "lizard"
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
    if faction == "vagabond":
        if "vagabond" in draft:
            faction = "vagabond2"
        else:
            factions.append("vagabond")
    if faction in red:
        redfacs += 1
    draft.append(faction)

locked = redfacs == 1
draft.sort(key=getReach, reverse=True)
lowestReach = draft.pop(len(draft) - 1)
print("Factions:")
for i in range(numFactions):
    print(draft[i])
if(locked):
    print("LOCKED:")
print(lowestReach)
