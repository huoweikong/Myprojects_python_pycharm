import re

with open('input.fas', 'r') as fin:
    sequences = [(m.group(1), ''.join(m.group(2).split()))
for m in re.finditer(r'(?m)^>([^ n]+)[^n]*([^>]*)', fin.read())]
with open('output.phy', 'w') as fout:
    fout.write('%d %dn' % (len(sequences), len(sequences[0][1])))
for item in sequences:
    fout.write('%-20s %sn' % item)