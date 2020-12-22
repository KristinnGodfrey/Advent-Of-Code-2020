import re

counter = 0

with open('input.txt') as f:
    Output = f.read()
Passar = Output.split('\n\n')
ValidPassports = 0
for Passi in Passar:
    SplitPassalina2 = re.split('(\s|\n)',Passi)
    Fields = []
    for Field in SplitPassalina2:
        Fields.append(Field.split(':')[0])
    if 'byr' in Fields and 'iyr' in Fields and 'eyr' in Fields and 'hgt' in Fields and 'ecl' in Fields and 'hcl' in Fields and 'pid' in Fields :
        print(counter)
        print(Field)
        ValidPassports += 1
    counter += 1
