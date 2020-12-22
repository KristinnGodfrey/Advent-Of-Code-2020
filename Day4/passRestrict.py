import re
with open('input.txt') as f:
    lines = f.read()

def checkByr(state):
    return int(state) >= 1920 and int(state) <= 2002

def checkIyr(state):
    return int(state) >= 2010 and int(state) <= 2020

def checkEyr(state):
    return int(state) >= 2020 and int(state) <= 2030

#Virkar kannski ekki
def checkHgt(state):
    if 'cm' in state:
        state = state.split('cm')
        state[0] = int(state[0])      
        if state[0] >= 150 and state[0] <= 193: return True
    elif 'in' in state:
        state = state.split('in')
        state[0] = int(state[0])      
        if state[0] >= 59 and state[0] <= 76: 
            print(state)
            return True
    return True

# init
states = {'byr': False,'iyr': False,'eyr': False,'hgt': False,'hcl': False,'ecl': False,'pid': False,'cid': False }
valid = 0

# set states 
lines = lines.split('\n\n') 
for li in lines:
    li = re.split('\s|\\n',li) 

    for i in li:
        i = i.split(':')            
        if 'byr' in i and checkByr(i[1]): states['byr'] = True 
        if 'iyr' in i and checkIyr(i[1]): states['iyr'] = True
        if 'eyr' in i and checkEyr(i[1]): states['eyr'] = True            
        if 'hgt' in i and checkHgt(i[1]): states['hgt'] = True           
            # if 'cm' in i[1]:
            #     print(i[1])
            # elif 'in' in i[1]:
            #     print(i[1])
            # states['hgt'] = True
            # print(i)
        if 'hcl' in i: states['hcl'] = True
        if 'ecl' in i: states['ecl'] = True
        if 'pid' in i: states['pid'] = True

        # print(i)
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