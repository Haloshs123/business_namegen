import random

#vweights in format [[letters], start weight, midweight, endweight]
vweights = [['a', '.5', '1', '.1'], ['ai', '.7', '1', '.2'], ['ay', '.1', '.3', '.5'], ['au', '.05', '.3', '.05'], ['ua', '.01', '.1', '.01'], ['e', '1', '1', '2'], ['ee', '.3', '.7', '.4'], ['ea', '.2', '.8', '.3'], ['ei', '.1', '.2', '.05'], ['ey', '.05', '.1', '.3'], ['eo', '.2', '.2', '.1'], ['eu', '.2', '.3', '.05'], ['i', '.8', '1', '1'], ['ie', '.2', '1', '.5'], ['o', '1', '1', '1'], ['o', '1', '1', '1'], ['oe', '.05', '.1', '.1'], ['ou', '.05', '.15', '.08'], ['oi', '.05', '.1', '.04'], ['oy', '.01', '.03', '.06'], ['oo', '.05', '.8', '.3'], ['oa', '.03', '.2', '.02'], ['u', '.4', '1', '.1'], ['ue', '.05', '.1', '.1'], ['ui', '.02', '.1', '.01'], ['y', '.02', '.2', '.8'], ['ye', '.4', '.2', '.2']]
vkey = ["letter","sv","mv","ev"]
#cweights in format [letter, startweight, endweight]
cweights = [['b', '1', '1'], ['c', '1', '.3'], ['d', '1', '.6'], ['f', '.8', '.3'], ['g', '1', '.3'], ['l', '.7', '.7'], ['m', '1', '.8'], ['n', '1', '1'], ['p', '.7', '.2'], ['r', '1', '.6'], ['s', '1', '.3'], ['t', '1', '.7'], ['x', '.05', '.05'], ['z', '.1', '.05'], ['bt', '.01', '.05'], ['ch', '1', '1'], ['ck', '.01', '1'], ['ct', '.01', '1'], ['ft', '.01', '1'], ['gh', '.1', '.8'], ['gn', '.08', '.3'], ['lb', '.01', '.5'], ['ld', '.01', '.5'], ['lf', '.01', '.4'], ['lk', '.01', '.5'], ['ll', '.2', '.7'], ['lm', '.01', '.4'], ['ln', '.01', '.4'], ['lp', '.01', '.2'], ['lt', '.01', '.5'], ['mb', '.07', '.3'], ['mn', '.03', '.2'], ['mp', '.01', '.3'], ['nk', '.01', '.25'], ['ng', '.01', '.8'], ['nt', '.01', '.6'], ['ph', '.8', '.7'], ['pt', '.01', '.5'], ['rb', '.01', '.15'], ['rc', '.01', '.3'], ['rd', '.01', '.4'], ['rf', '.01', '.2'], ['rg', '.01', '.3'], ['rk', '.01', '.3'], ['rl', '.01', '.2'], ['rm', '.01', '.2'], ['rn', '.01', '.2'], ['rp', '.01', '.3'], ['rt', '.01', '.4'], ['rv', '.01', '.05'], ['rz', '.01', '.03'], ['sh', '1', '.8'], ['sk', '.8', '.8'], ['sp', '.7', '.4'], ['ss', '.01', '.7'], ['st', '.8', '.6'], ['zz', '.01', '.03'], ['lch', '.01', '.7'], ['lsh', '.01', '.6'], ['lth', '.01', '.5'], ['rch', '.01', '.5'], ['rsh', '.01', '.4'], ['rst', '.01', '.6'], ['rth', '.01', '.4'], ['sch', '.5', '.2'], ['tch', '.05', '.7'], ['h', '.7', '.2'], ['j', '.6', '.01'], ['k', '.8', '.6'], ['v', '.5', '.2'], ['w', '.4', '.4'], ['y', '.02', '.6'], ['bl', '.3', '.05'], ['br', '.8', '.08'], ['cl', '.7', '.01'], ['cr', '.7', '.02'], ['dr', '.8', '.01'], ['fl', '.7', '.02'], ['fr', '.8', '.01'], ['gl', '.4', '.07'], ['gr', '.8', '.02'], ['kn', '.4', '.01'], ['pl', '.6', '.02'], ['pr', '.4', '.01'], ['qu', '.1', '.01'], ['sc', '.5', '.1'], ['sl', '.6', '.06'], ['sm', '.5', '.2'], ['sn', '.6', '.15'], ['th', '.6', '.8'], ['tr', '.7', '.1'], ['wh', '.2', '.08'], ['wr', '.2', '.01'], ['scr', '.6', '.01'], ['shm', '.01', '.1'], ['shr', '.4', '.05'], ['squ', '.05', '.01'], ['str', '.4', '.02']]
ckey = ["letter","sc","ec"]
#oweights in format [type, start vowel, mid vowel, end vowel, start const, end const, (end)]
oweights = \
    [["sv", 0, 0, 0, 0, 1, 0],
     ["mv", 0, 0, 0, 0, 1, 0],
     ["ev", 0, 0, 0, .3, 0, 1],
     ["sc", 0, 1, 1, 0, 0, 0],
     ["ec", 0, 1, 1, 0, 0, 3],
     ["start", 1, 0, 0, 1, 0, 0]]
owkey = ["type", "sv","mv","ev","sc","ec","end"]

businesstypes = [" Corp.", " Inc.", " LLC", ", Nonprofit", " Group", " Ltd.", " plc."]


def letterchoice(type):
    sum = 0
    if type[1] == "v":
        for i in range(len(vkey)):
            if type == vkey[i]:
                for j in range(len(vweights)):
                    sum = sum + float(vweights[j][i])
                num = random.uniform(0.0,sum)
                for j in range(len(vweights)):
                    num = num - float(vweights[j][i])
                    if num <= 0:
                        return(vweights[j][0])
    else:
        for i in range(len(ckey)):
            if type == ckey[i]:
                for j in range(len(cweights)):
                    sum = sum + float(cweights[j][i])
                num = random.uniform(0.0,sum)
                for j in range(len(cweights)):
                    num = num - float(cweights[j][i])
                    if num <= 0:
                        return(cweights[j][0])

def wordgen(structure):
    word = ""
    abbrev = ""
    for i in range(len(structure)):
        newpart = letterchoice(structure[i])
        word = word + newpart
        if i < 3:
            abbrev = abbrev + newpart[0]
    return(word, abbrev)

def structuregen():
    structure = []
    structure.append(owkey[structurechoice(oweights[5])])
    while True:
        currenttype = structure[len(structure)-1]
        for i in range(len(oweights)):
            if currenttype == oweights[i][0]:
                currentarray = oweights[i]
        choice = structurechoice(currentarray)
        if owkey[choice] == "end":
            return(structure)
        else:
            structure.append(owkey[choice])

def structurechoice(array):
    sum = 0
    for i in range(len(array)):
        if type(array[i]) != str:
            sum = sum + array[i]
    num = random.uniform(0.0,sum)
    for i in range(len(array)):
        if type(array[i]) != str:
            num = num - array[i]
        if num <= 0:
            return(i)

def businessfy(name):
    num = random.randint(0, len(businesstypes)-1)
    title = businesstypes[num]
    return(name.capitalize()+title)

structure = structuregen()
names = wordgen(structure)
title = names[0]
if len(names[1]) < 3: abbreviation = names[0][0:3].upper()
else: abbreviation = names[1].upper()
businessname = businessfy(title)

print(businessname+"\n"+abbreviation)

