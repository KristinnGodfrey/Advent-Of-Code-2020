import re
with open('input.txt') as f:
    lines = f.read()

def checkByr(state):
    return int(state) >= 1920 and int(state) <= 2002

def checkIyr(state):
    return int(state) >= 2010 and int(state) <= 2020

def checkEyr(state):
    return int(state) >= 2020 and int(state) <= 2030

#Virkar mögulega ekki
def checkHgt(state):
    if 'cm' in state:
        state = state.split('cm')
        state[0] = int(state[0])      
        if state[0] >= 150 and state[0] <= 193: return True
    elif 'in' in state:
        state = state.split('in')
        state[0] = int(state[0])      
        if state[0] >= 59 and state[0] <= 76: return True

def checkHcl(state):
    return re.match('#[0-9]|[a-f]{6}', str(state))

def checkEcl(state):
    if not re.search('amb|blu|brn|gry|grn|hzl|oth', str(state)):
        # print(state)
        return False
    # if re.search('amb|blu|brn|gry|grn|hzl|oth', str(state)):
    #     print(state)
    # return re.search('amb|blu|brn|gry|grn|hzl|oth', str(state))
    return True

def checkPid(state):
    return re.match('0*\d{9}', str(state))


# init
states = {'byr': False,'iyr': False,'eyr': False,'hgt': False,'hcl': False,'ecl': False,'pid': False,'cid': False }
valid = 0

# set states 
lines = lines.split('\n\n') 
for li in lines:
    li = re.split('\s|\\n',li) 

    for i in li:
        i = i.split(':')     
        # print(i)       
        if 'byr' in i and checkByr(i[1]): states['byr'] = True 
        else:
            print("YEEEEEEEEEEEEEEEE: ")
            print(i)
        if 'iyr' in i and checkIyr(i[1]): states['iyr'] = True
        else:
            print("YEEEEEEEEEEEEEEEE: ")
            print(i)
        if 'eyr' in i and checkEyr(i[1]): states['eyr'] = True            
        else:
            print("YEEEEEEEEEEEEEEEE: ")
            print(i)
        if 'hgt' in i and checkHgt(i[1]): states['hgt'] = True      
        else:
            print("YEEEEEEEEEEEEEEEE: ")
            print(i)
        if 'hcl' in i and checkHcl(i[1]): states['hcl'] = True
        else:
            print("YEEEEEEEEEEEEEEEE: ")
            print(i)
        if 'ecl' in i and checkEcl(i[1]): states['ecl'] = True
        else:
            print("YEEEEEEEEEEEEEEEE: ")
            print(i)
        if 'pid' in i and checkPid(i[1]): states['pid'] = True
        else:
            print("Didnt work: ")
            print(i)

    # validate    
    counter = 0

    state = states.values()    
    for i in state:
        if i == True:
            counter += 1
    if counter >= 7: 
        valid +=1

    # reset states
    states = {'byr': False,'iyr': False,'eyr': False,'hgt': False,'hcl': False,'ecl': False,'pid': False,'cid': False }

print(valid)