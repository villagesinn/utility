#repo
#Jianna West
#CSCI 102-Section A
#Week 12 - Part A

def PrintOutput(string):
    return print('OUTPUT>', string)

def LoadFile(file):
    with open(file) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content
    
def UpdateString(string, new, index):
    letters = list(string)
    letters[index] = new
    return PrintOutput(''.join(letters))
    
def FindWordCount(wordList, look):
    for i in range(len(wordList)):
        x = wordList[i].count(look)
        tot = tot + x
    return PrintOutput(tot)

def ScoreFinder(players, scores, name):
    name.lower()
    x.lower() for x in players
    if name in players:
        where = players.index(name)
        theirScore = scores[where]
        print('OUTPUT', name, 'got a score of' theirScore)
    else:
        print('OUTPUT player not found')

def Union(list1, list2):
    newlist = list1 + list2
    return newlist

def Intersection(list1, list2):
    newlist = []
    for i in range(len(list1)):
        if list1[i] in list2:
            newlist.append(list1[i])
    return newlist

def NotIn(list1, list2):
    newlist = []
    if len(list1) > len(list2):
        for i in range(len(list1)):
            if list1[i] not in list2:
                newlist.append(list1[i])
    elif len(list1) < len(list2):
        for i in range(len(list2)):
            if list2[i] not in list1:
                newlist.append(list2[i])
    return newlist
