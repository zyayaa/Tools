import re
import argparse

def readFile(fname):
    with open(fname) as f:
        content = f.readlines() 
        content = [x.strip() for x in content]
    return content

def writeFile(hashes, fname):
    f = open(fname, "w")
    for h in hashes:
        f.write("{}\n".format(h))
    return

domainAdmins=[]
domainUsers=[]

parser = argparse.ArgumentParser(description="Domain Hash Filter")
parser.add_argument('--hashes', help='NTDS hashes file')
parser.add_argument('--domainadmins', help='Domain Admin file(one per line)')
parser.add_argument('--outputadmins', help='Domain Admins output file',)
parser.add_argument('--outputusers', help='Domain Users output file')
args = parser.parse_args()

domainAdminsFile = readFile(args.domainadmins)
hashFile = readFile(args.hashes)
domainAdminsHashFile = args.outputadmins
domainUsersHashFile = args.outputusers

regex = ""
for da in domainAdminsFile:
    regex = "{}|{}".format(regex, da)
    
#remove first |
regex = regex[1:]

for h in hashFile:
    #ignore computer accounts
    if "$" in h:
        continue

    m = re.search(regex, h)
    if m:
        domainAdmins.append("{}".format(m.string))
    else:
        domainUsers.append(h)

writeFile(domainAdmins, domainAdminsHashFile)
writeFile(domainUsers, domainUsersHashFile)

print("Done!")