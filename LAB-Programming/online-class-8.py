import scipy.integrate
import pylab
import random
#Merkezi Limit Teoremi
def gaussian(x,mu,sigma):
    factor1=(1/(sigma*((2*pylab.pi)**0.5)))
    factor2=pylab.e**-(((x-mu)**2)/(2*sigma**2))
    return factor1*factor2

area=round(scipy.integrate.quad(gaussian,-3,3,(0,1))[0],4)
print('Probability of being within 3','of true mean of tight dist. =', area)


area=round(scipy.integrate.quad(gaussian,-3,3,(0,100))[0],4)


print('Probability of being within 3','of true mean of wide dist. =', area)




def testSamples(numTrials,sampleSize):
    tightMeans,wideMeans=[],[]
    for t in range(numTrials):
        sampleTight,sampleWide=[],[]
        for i in range(sampleSize):
            sampleTight.append(random.gauss(0,1))
            sampleWide.append(random.gauss(0,100))
        tightMeans.append(sum(sampleTight)/len(sampleTight))
        wideMeans.append(sum(sampleWide)/len(sampleWide))
    return tightMeans, wideMeans

tightMeans,wideMeans=testSamples(1000,40)
pylab.plot(wideMeans,'y*',label='SD=100')
pylab.plot(tightMeans,'bo',label='SD=1')
pylab.xlabel('Sample Number')
pylab.ylabel('Sample Mean')
pylab.title('Means of Samples of Size ' + str(40))
pylab.legend()
pylab.show()

pylab.figure()
pylab.hist(wideMeans,bins=20,label='SD=100')
pylab.title('Distribution of Sample Means')
pylab.xlabel('Sample Mean')
pylab.ylabel('Frequency of Occurrence')
pylab.legend()
pylab.show()



def variance(X):
    mean=sum(X)/len(X)
    tot=0.0
    for x in X:
        tot+=(x-mean)**2
    return tot/len(X)

def stdDev(X):
    return variance(X)**0.5

def plotMeans(numDicePerTrial,numDiceThrown,numBins,legend,color,style):
    means=[]
    numTrials=numDiceThrown//numDicePerTrial
    for i in range(numTrials):
        vals=0
        for j in range(numDicePerTrial):
            vals+=5*random.random()
        means.append(vals/numDicePerTrial)
    pylab.hist(means, numBins, color = color, label = legend,weights = pylab.array(len(means)*[1])/len(means),hatch = style)
    return sum(means)/len(means), variance(means)

mean, var=plotMeans(1,100000,11,'1 die','w','*')
print('Mean of rolling 1 die =', round(mean,4),'Variance =', round(var,4))
mean,var=plotMeans(100,100000,11,'Mean of 100 dice','w','//')
print('Mean of rolling 100 dice =', round(mean, 4),'Variance =', round(var, 4))
pylab.title('Rolling Continuous Dice')
pylab.xlabel('Value')
pylab.ylabel('Probability')
pylab.legend()
pylab.show()