import re
with open('input.txt') as f:
    lines = f.read()

def checkByr(state):
    print("noice")
    state = int(state)
    if state >= 1920 and state <= 2002:
        state = str(state)
        return re.match('[1920-2002]', state) #and state >= 1920 and state <= 2002
# init
states = {'byr': False,'iyr': False,'eyr': False,'hgt': False,'hcl': False,'ecl': False,'pid': False,'cid': False }
valid = 0

# set states 
lines = lines.split('\n\n') 
for li in lines:
    li = re.split('\s|\\n',li) 

    for i in li:
        i = i.split(':')    
        if 'byr' in i and checkByr(i[1]):
            states['byr'] = True 
        if 'iyr' in i: states['iyr'] = True
        if 'eyr' in i: states['eyr'] = True
        if 'hgt' in i: states['hgt'] = True
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