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
        if 'cid' in i: states['cid'] = True

    # validate
    counter = 0
    for state in states:
        if states[state] == False:
            counter += 1
    
    if counter < 2 and states['hgt'] == True:
        valid +=1
    
    print(counter)
    print(states)

    states = {'byr': False,'iyr': False,'eyr': False,'hgt': False,'hcl': False,'ecl': False,'pid': False,'cid': False }

print(valid)
        
    
        


    






# seperator = '\n'
# for li in lines:
#     li = str(li).split()
#     li = seperator.join(li)
#     print(li)