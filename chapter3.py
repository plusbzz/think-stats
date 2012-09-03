import chapter1
from chapter1 import *
import Pmf


def UnbiasPmf(pmf):
    old_dict = pmf.GetDict()
    new_dict = dict([(k,float(v)/k) for k,v in old_dict.items()])
    return Pmf.MakePmfFromDict(new_dict)

def ClassSizes():
    class_size_dean_dict = {
             7:8,    
            12:8,    
            17:14,    
            22:4,    
            27:6,    
            32:8,
            37:8,    
            42:8,    
            47:8   
    }
    class_size_student_dict = dict([(k,k*v) for k,v in class_size_dean_dict.items()])
    
    
    class_size_dean_pmf = Pmf.MakePmfFromDict(class_size_dean_dict)
    class_size_student_pmf = Pmf.MakePmfFromDict(class_size_student_dict)
    
    print "Mean class size from Dean's perspective: ", class_size_dean_pmf.Mean()
    print "Mean class size from Student's perspective: ", class_size_student_pmf.Mean()
    
    class_size_dean_pmf = UnbiasPmf(class_size_student_pmf)
    print "Mean class size from Dean's perspective using unbiasing: ", class_size_dean_pmf.Mean()
   
       
if __name__ == '__main__':
    ClassSizes()