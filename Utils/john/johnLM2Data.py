def readFile(fname):
    with open(fname) as f:
        content = f.readlines()
    
    content = [x.strip() for x in content] 
    return content


def parse(dumpFilePath, potFilePath, outFilePath):
    dumpFile=readFile(dumpFilePath)
    potFile=readFile(potFilePath)
    outFile=open(outFilePath, "w")

    for domainHash in dumpFile:
        domainHashSplit=domainHash.split(':')
        username = domainHashSplit[0]
        lmHash = domainHashSplit[3]
        for crackedPassword in potFile:
            if lmHash in crackedPassword:
                password = crackedPassword.split(':')[1]
                outFile.write("{}:{}\n".format(username, password))

parse("dumpfile", "johnpotfile", "outputfile")
