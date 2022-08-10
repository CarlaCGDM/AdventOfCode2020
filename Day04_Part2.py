puzzle_input = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""

lines = puzzle_input.splitlines()

passports = []
new_passport = {}

#when line is empty we start a new passport

for line in lines:
    if line != "":
        fields = line.split()
        for field in fields:
            if field[0:3] != "cid":
                new_passport[field[0:3]] = field[4:]
        if len(new_passport) == 7:
            passports.append(new_passport)
            new_passport = {}
    else:
        new_passport = {}
  
#out of all the passports lets check the valid fields

valid_passports = []

for passport in passports:
  
    #byr
    byr = passport["byr"]
    if byr.isnumeric():
        if int(byr) not in range(1920,2002+1):
            continue
    else:
        continue
        
    #iyr
    iyr = passport["iyr"]
    if iyr.isnumeric():
        if int(iyr) not in range(2010,2020+1):
            continue
    else:
        continue
        
    #eyr
    eyr = passport["eyr"]
    if eyr.isnumeric():
        if int(eyr) not in range(2020,2030+1):
            continue
    else:
        continue
        
    #hgt
    hgt = passport["hgt"]
    unit = hgt[-2:]
    number = int(hgt[:-2])
    if unit == "cm":
        if number not in range(150,193+1):
            continue
    if unit == "in":
        if number not in range(59,76):
            continue
            
    #hcl
    hcl = passport["hcl"]
    if len(hcl) != 7:
        continue
    if hcl[0] != "#":
        continue
    for char in hcl[1:]:
        if char.isalnum() == False:
            continue
            
    #ecl
    if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        continue
        
    #pid
    pid = passport["pid"]
    if len(pid) != 9:
        continue
    if pid.isnumeric() == False:
        continue
        
    valid_passports.append(passport)
    
print(len(valid_passports))
