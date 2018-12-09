import re
import numpy as np
from shutil import copyfile
import glob


def rkc(word, replacement, text):
    def func(match):
        g = match.group()
        if g.islower(): return replacement.lower()
        if g.istitle(): return replacement.title()
        if g.isupper(): return replacement.upper()
        return replacement      
    return re.sub(word, func, text, flags=re.I)

if __name__ == "__main__":
    replacement_table = np.loadtxt('replacements.txt', delimiter=', ', dtype=str)

    tex_files = glob.glob('./**/*.tex', recursive=True)

    for fname in tex_files:
        #copyfile(fname, fname+'.bk')

        with open(fname, 'r') as f:
            file_string = f.read()

        for re_pair in replacement_table:
            file_string = rkc(re_pair[0], re_pair[1], file_string)

        with open(fname, 'w') as o:
            o.write(file_string)
