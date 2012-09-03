import chapter1
from chapter1 import *
import Pmf

def RemainingLifetime(pmf,age):
    new_pmf = Pmf.Pmf()
    
    for val in pmf.Values():
        remainder = val - age
        if remainder > 0:
            new_pmf.Set(remainder, pmf.Prob(val))
            
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
 
def GetFieldAsList(table,field):
    return [getattr(rec,field) for rec in table.records]
    
def RelativeRisk(firsts_pmf, others_pmf):

    rr_f_o_early = ProbEarly(firsts_pmf)/ProbEarly(others_pmf)   
    print "Relative risk of early birth for first babies: ", rr_f_o_early
    
    rr_f_o = ProbOnTime(firsts_pmf)/ProbOnTime(others_pmf)   
    print "Relative risk of on-time birth for first babies: ", rr_f_o
        
    rr_f_o_late = ProbLate(firsts_pmf)/ProbLate(others_pmf)   
    print "Relative risk of late birth for first babies: ", rr_f_o_late
 
def ConditionalDist(pmf,age):
    new_pmf = Pmf.Pmf()
    
    for val in pmf.Values():
        if val > age:
            new_pmf.Set(val, pmf.Prob(val))
     
    new_pmf.Normalize()       
    return new_pmf
       
def ConditionalProb(firsts_pmf, others_pmf):
    results = []
    for x in xrange(34,45):
        x_firsts_prob = ConditionalDist(firsts_pmf,x).Prob(x+1)
        x_others_prob = ConditionalDist(others_pmf,x).Prob(x+1)
        results.append((x,x_firsts_prob,x_others_prob))
    
    print results
    

if __name__ == '__main__':
    # Read data
    table = ReadTable()
    live_births = GetLiveBirths(table)    
    firsts, others = PartitionPregnancies(live_births)
    
    # Get PMFs for each one
    live_birth_pmf  = Pmf.MakePmfFromList(GetFieldAsList(live_births,"prglength"))
    firsts_pmf      = Pmf.MakePmfFromList(GetFieldAsList(firsts,"prglength"))
    others_pmf      = Pmf.MakePmfFromList(GetFieldAsList(others,"prglength"))
    
    RelativeRisk(firsts_pmf,others_pmf)

    ConditionalProb(firsts_pmf,others_pmf)
    
    