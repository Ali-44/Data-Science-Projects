fhandle=open('mbox-short.txt','r')
counts=dict()
for line in fhandle:
    line=line.rstrip()
    if len(line) < 1 :
        continue
    if not line.startswith('From:'):
        continue
    words=line.split()
    emailad=words[1]
    emails=emailad.split()
    for email in emails:
        counts[email]=counts.get(email,0) + 1

bigemail=None
bigcount=None
for email,count in counts.items():
    if bigemail is None or count>bigcount:
        bigemail=email
        bigcount=count
print(bigemail,bigcount)
