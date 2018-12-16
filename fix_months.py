import re
from shutil import copyfile

library_file = 'library.bib'

new_file = []

copyfile(library_file, library_file+'.bk')

with open(library_file, 'r', encoding="utf-8") as f:
    for line in f:
        if line.strip()[:5] == 'month':
            line = re.sub('[{}]', '', line)
        
        new_file.append(line)

with open(library_file, 'w', encoding="utf-8") as f:
    for line in new_file:
        f.write(line)