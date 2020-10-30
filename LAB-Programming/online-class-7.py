import random, matplotlib.pylab as pylab
#Trees
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)


def search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)


def minValueNode(node):
    current = node
    while (current.left is not None):
        current = current.left
    return current


def deleteNode(root, key):
    if root is None:
        return root

    if key < root.val:
        root.left = deleteNode(root.left, key)

    elif (key > root.val):
        root.right = deleteNode(root.right, key)

    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minValueNode(root.right)
        root.val = temp.val
        root.right = deleteNode(root.right, temp.val)

    return root


r = Node(50)
insert(r, Node(30))
insert(r, Node(20))
insert(r, Node(40))
insert(r, Node(70))
insert(r, Node(60))
insert(r, Node(80))

inorder(r)
print()

result = search(r, 200)
print(result)

inorder(r)
print()

root = deleteNode(r, 20)
inorder(root)
print()


print("\n\n")
print("--------------------------")
print("\n\n")
#atılan zarda kaç kere tura geldiği
# Zar Sonucunu Döndürür
def rollDie():
    return random.choice([1,2,3,4,5,6])


def rollN(n):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    return result

print("Atılan zarlar: ", rollN(5))
print("\n\n")
print("--------------------------")
print("\n\n")

# n-kez atılan parada tura gelme olasılığını döndürür
def flip(numFlips):
    heads = 0.0
    for i in range(numFlips):
        if random.choice(('H', 'T')) == 'H':  # if random.random() < 0.5:
            heads += 1
    return heads/numFlips

print("Deneye göre tura gelme olasılığı: ", flip(10))
print("\n\n")
print("--------------------------")
print("\n\n")

# deney sayısı ve her deneydeki deneme sayıları alınarak yapılan tura gelme olasılığını döndürür
def flipSim(numFlipsPerTrial, numTrials):
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    mean = sum(fracHeads)/len(fracHeads)
    return mean

print("Deneylere göre tura gelme olasılığı: ", flipSim(1000, 1))
print("\n\n")
print("--------------------------")
print("\n\n")

def regressToMean(numFlips, numTrials):
    fracHeads = []
    for t in range(numTrials):
        fracHeads.append(flip(numFlips))
    extremes, nextTrials = [], []
    for i in range(len(fracHeads)-1):
        if fracHeads[i] < 0.33 or fracHeads[i] > 0.66:
            extremes.append(fracHeads[i])
            nextTrials.append(fracHeads[i+1])
    pylab.plot(range(len(extremes)), extremes, 'ko', label='Extreme')
    pylab.plot(range(len(nextTrials)), nextTrials, 'k^', label='Next Trial')
    pylab.axhline(0.5)
    pylab.ylim(0,1)
    pylab.xlim(-1, len(extremes)+1)
    pylab.xlabel('Extreme Example and Next Trial')
    pylab.ylabel('Fraction Heads')
    pylab.title('Regression to the Mean')
    pylab.legend(loc = 'best')
    pylab.show()

regressToMean(15,40)

def flipPlot(minExp, maxExp):
    ratios, diffs, xAxis = [], [], []
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        numHeads = 0
        for n in range(numFlips):
            if random.choice(('H', 'T')) == 'H':  # if random.random() < 0.5:
                numHeads += 1
        numTails = numFlips - numHeads
        try:
            ratios.append(numHeads/numTails)
            diffs.append(abs(numHeads - numTails))
        except ZeroDivisionError:
            continue
    pylab.title('Difference Between Heads and Tails')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Abs(#Heads - #Tails)')
    pylab.plot(xAxis, diffs, 'k')
    pylab.figure()
    pylab.title('Heads/Tails Ratios')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('#Heads/#Tails')
    pylab.plot(xAxis, ratios, 'k')
    pylab.show()
random.seed(0)
flipPlot(4, 20)


def variance(X):
    mean = float(sum(X)) / len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    return tot / len(X)


def stdDev(X):
    return variance(X) ** 0.5




def makePlot(xVals, yVals, title, xLabel, yLabel, style,
             logX=False, logY=False):
    pylab.figure()
    pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.plot(xVals, yVals, style)
    if logX:
        pylab.semilogx()
    if logY:
        pylab.semilogy()



def runTrial(numFlips):
    numHeads = 0
    for n in range(numFlips):
        if random.choice(('H', 'T')) == 'H':  # if random.random() < 0.5:
            numHeads += 1
    numTails = numFlips - numHeads
    return (numHeads, numTails)





def flipPlot1(minExp, maxExp, numTrials):
    ratiosMeans, diffsMeans, ratiosSDs, diffsSDs = [], [], [], []
    xAxis = []
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2 ** exp)
    for numFlips in xAxis:
        ratios, diffs = [], []
        try:
            for t in range(numTrials):
                numHeads, numTails = runTrial(numFlips)
                ratios.append(numHeads / numTails)
                diffs.append(abs(numHeads - numTails))
            ratiosMeans.append(sum(ratios) / numTrials)
            diffsMeans.append(sum(diffs) / numTrials)
            ratiosSDs.append(stdDev(ratios))
            diffsSDs.append(stdDev(diffs))
        except ZeroDivisionError:
            continue

    numTrialsString = ' (' + str(numTrials) + ' Trials)'

    title = 'Mean Heads/Tails Ratios' + numTrialsString
    makePlot(xAxis, ratiosMeans, title, 'Number of flips', 'Mean Heads/Tails', 'ko', logX=True)

    title = 'SD Heads/Tails Ratios' + numTrialsString
    makePlot(xAxis, ratiosSDs, title, 'Number of Flips', 'Standard Deviation', 'ko',
             logX=True, logY=True)



flipPlot1(4, 20, 20)