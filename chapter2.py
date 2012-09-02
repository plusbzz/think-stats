import Pmf

def RemainingLifetime(pmf,age):
    new_pmf = Pmf.Pmf()
    
    for val in new_pmf.Values():
        remainder = val - age
        if remainder > 0:
            new_pmf.set(remainder, pmf.Prob(val))
            
    return new_pmf

def PmfMean(pmf):
    pmf.Normalize()
    return sum([prob*val for val,prob in pmf.Items()])

def PmfVar(pmf):
    mu = PmfMean(pmf)
    return sum([prob*((val-mu)**2) for val,prob in pmf.Items()])
    

def BinProb(pmf,bin_start=None,bin_end=None):
    '''Calculate probability for the range (bin_start,bin_end]'''
    pmf.Normalize()
    frac = 0.0
    for val in pmf.Values():
        if bin_start is None or val > bin_start:
            if bin_end is None or val <= bin_end:
                frac+=pmf.Prob(val)
    
    return  frac          
         
     
def ProbEarly(pmf):
    return BinProb(pmf,bin_end=37)

def ProbOnTime(pmf):
    return BinProb(pmf,37,40)

def ProbLate(pmf):
    return BinProb(pmf,40)
    