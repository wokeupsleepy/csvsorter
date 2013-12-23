import csv

def listreader(listfile):
    freshset = []
    with open(listfile) as csvfile:
        readlist = csv.reader(csvfile)
        for line in readlist:
            freshset.append(line[0])
    return freshset

#listcomparison method returns everything in a that is not in b
def listcomparison(a,b):
    c = set(set(a) - set(b))
    return c

alpha = listreader('11itemarrayalpha.csv')
beta = listreader('11itemarraybeta.csv')
gamma = listreader('12itemarray.csv')

print(listcomparison(alpha, beta))
print(listcomparison(alpha, gamma))