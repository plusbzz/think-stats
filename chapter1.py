import survey

def ReadTable():
    table = survey.Pregnancies()
    table.ReadRecords()
    return table

def GetLiveBirths(table):
    lv_table = survey.Pregnancies()
    live_births = filter(lambda r: r.outcome == 1, table.records) 
    
    for rec in live_births:
        lv_table.AddRecord(rec)
        
    return lv_table
	
def PartitionPregnancies(table):
    firsts = survey.Pregnancies()
    others = survey.Pregnancies()
	
    for rec in table.records:
        if rec.birthord == 1:
            firsts.AddRecord(rec)
        else:
            others.AddRecord(rec)

    return (firsts,others)
 
def Mean(table,field):
    lst = [getattr(rec,field) for rec in table.records]
    if len(lst) > 0:
        return float(sum(lst))/len(lst)
    else:
        return 0
        
if __name__ == '__main__':
    import sys
    table = ReadTable()
    print "Number of Pregnancies: ",len(table)

    live_births = GetLiveBirths(table)
    print "Number of Live Births: ", len(live_births)
    
    firsts, others = PartitionPregnancies(live_births)
    
    print "Number of First Births: ", len(firsts)
    print "Number of Other Births: ", len(others)
    
    mean_firsts = Mean(firsts,"prglength") 
    mean_others = Mean(others,"prglength")
    print "Mean pregnancy length for firsts: ", mean_firsts
    print "Mean pregnancy length for others: ", mean_others
    print "Difference in pregnancy lengths: ", 7*abs(mean_firsts-mean_others)
