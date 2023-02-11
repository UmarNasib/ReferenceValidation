import re

testString = ''
with open('processedTextFile1.txt') as f:
    sample = ''
    lines = f.readlines()
    for line in lines:
        sample = sample + line
    testString = sample.rstrip()
splittedString = testString.split(".")

for x in splittedString:
    r2 = re.findall("\[*[^\]]*\]",x)
    if len(r2) > 0:
        r2[0].rstrip()
        print(r2)
