puzzle_input = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

lines = puzzle_input.splitlines()

valid_passports = 0
passport_fields = []

#when line is empty we start a new passport

for line in lines:
    if line != "":
        fields = line.split()
        for field in fields:
            if field[0:3] != "cid":
                passport_fields.append(field[0:3])
        if len(passport_fields) == 7:
            valid_passports += 1
            passport_fields = []
    else:
        passport_fields = []
        
print(valid_passports)
