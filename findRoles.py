import random
reachvals = [None, None, 17, 18, 21, 25, 28]
teams = {
    "marquise" : 10,
    "duchy" : 8,
    "eyrie" : 7,
    "vagabond" : 5,
    "riverfolk" : 5,
    "woodland" : 3,
    "corvid" : 3,
    "lizard" : 2,
    "vagabond2" : 2
}

print("How many players are playing?")
playernum = 0
while(playernum < 2 or playernum >= len(reachvals)):
    playernum = int(input())
    if playernum >= len(reachvals) or reachvals[playernum] is None:
        print("Invalid number of players inputted, please input between 2 and 6")
chosenTeams = []
while(len(chosenTeams) == 0):
    print("Any teams that you want to exclude? Seperate with Space, type * for none")
    print("Options:")
    t = "[ "
    for key in [key for key in teams]:
        t += key + ", "
    t = t[0:len(t) - 2]
    t += "]"
    print(t)
    inteams = input()
    if inteams == "*":
        chosenTeams = []
        break
    else:
        chosenTeams = inteams.split(" ")
    if len(teams) - len(chosenTeams) < playernum:
        print("You have not provided enough teams")
        chosenTeams = []
        continue
    totalReach = []
    for key in teams:
        totalReach.append(teams[key])
    cont = False
    for team in chosenTeams:
        if cont:
            continue
        if team.lower() not in teams:
            print("Team " + team + " is not a valid team")
            cont = True
        else:
            totalReach.remove(teams[team.lower()])
    totalReach.sort(reverse=True)
    if cont:
        chosenTeams = []
    elif sum(totalReach[0:playernum]) < reachvals[playernum]:
        print("Cannot generate a valid team from these inputs")
        chosenTeams = []
    #print(sum(totalReach[0:playernum]))

validTeams = False
myTeam = []
availableTeams = []
for thing in teams:
    if thing not in chosenTeams:
        availableTeams.append(thing)
while(not validTeams):
    random.shuffle(availableTeams)
    myTeam = availableTeams[0 : playernum]
    totalReach = 0
    for team in myTeam:
        totalReach += teams[team]
    validTeams = totalReach >= reachvals[playernum] and not "vagabond2" in myTeam or "vagabond" in myTeam

print(myTeam)