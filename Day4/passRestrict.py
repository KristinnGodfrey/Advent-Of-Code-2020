import re
with open('input.txt') as f:
    lines = f.read()

def checkByr(state):
    return int(state) >= 1920 and int(state) <= 2002

def checkIyr(state):
    return int(state) >= 2010 and int(state) <= 2020        

def checkEyr(state):
    return int(state) >= 2020 and int(state) <= 2030

def checkHgt(state):
    if 'cm' in state:
        state = state.split('cm')
        return int(state[0]) >= 150 and int(state[0]) <= 193
    elif 'in' in state:
        state = state.split('in')
        return int(state[0]) >= 59 and int(state[0]) <= 76

def checkHcl(state):
    return re.match('#([0-9]|[a-f]){6}', str(state))

def checkEcl(state):
    return re.match('(amb|blu|brn|gry|grn|hzl|oth)', str(state))
        
def checkPid(state):
    return re.match('0*\d{9}', str(state))

# init
states = {'byr': False,'iyr': False,'eyr': False,'hgt': False,'hcl': False,'ecl': False,'pid': False,'cid': False}
valid = 0

lines = lines.split('\n\n') 
for li in lines:
    li = re.split('\s|\\n',li) 

    for i in li:
        i = i.split(':')     
        if 'byr' in i and checkByr(i[1]): states['byr'] = True 
        if 'iyr' in i and checkIyr(i[1]): states['iyr'] = True
        if 'eyr' in i and checkEyr(i[1]): states['eyr'] = True
        if 'hgt' in i and checkHgt(i[1]): states['hgt'] = True                  
        if 'hcl' in i and checkHcl(i[1]): states['hcl'] = True
        if 'ecl' in i and checkEcl(i[1]): states['ecl'] = True
        if 'pid' in i and checkPid(i[1]): states['pid'] = True
        
    # validate    
    counter = 0

    state = states.values()    
    for i in state:
        if i == True:
            counter += 1
    if counter >= 7: 
        valid +=1

    # reset states
    states = {'byr': False,'iyr': False,'eyr': False,'hgt': False,'hcl': False,'ecl': False,'pid': False,'cid': False}

print(valid)