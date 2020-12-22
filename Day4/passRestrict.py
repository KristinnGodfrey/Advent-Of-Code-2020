import re
with open('input.txt') as f:
    lines = f.read()

# init
states = {'byr': False,'iyr': False,'eyr': False,'hgt': False,'hcl': False,'ecl': False,'pid': False,'cid': False }
valid = 0

# set states 
lines = lines.split('\n\n') 
for li in lines:
    li = re.split('\s|\\n',li) 

    for i in li:       
        if 'byr' in i: states['byr'] = True 
        if 'iyr' in i: states['iyr'] = True
        if 'eyr' in i: states['eyr'] = True
        if 'hgt' in i: states['hgt'] = True
        if 'hcl' in i: states['hcl'] = True
        if 'ecl' in i: states['ecl'] = True
        if 'pid' in i: states['pid'] = True

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