from typing import Any
def E(val):
    if (type(val)==Emperical_DRV):
        return val.E()

def var(val )->float:
    if type(val) == list:
        return sum(square(sub(col,mean())))/(len(col)-1)
    elif type(val)==Emperical_DRV:
        return val.var()

def sd(val)->float:
    if type(val) == list:
        return sqrt(var(col))
    elif type(val)==Emperical_DRV:
        return val.sd()
# add moment generating function

def sqrt(num : float )->float:
    '''Returns the square root of the given number'''
    xn=1
    xn1=0
    while True:
        #xn1 = xn - (xn*xn - num)/(2*xn) #newton's method
        xn1 = (xn + num/xn)/2 # Babylon/Heron's method
        if(abs(xn1-xn)<0.0000000001):
            break
        else:
            xn = xn1 
    return xn

def greater(col : list[float], val:Any)->list[bool]:
    '''Returns a boolean list that has true if the corresponding list element is greater than the given number'''
    g = lambda x : True if x >val else False
    return [x>val for x in col]

def equal(col : list[float], val:Any)->list[bool]:
    '''Returns a boolean list that has true if the corresponding list element is equal to the given number'''
    return [x==val for x in col]

def less(col : list[float], val:Any)->list[bool]:
    '''Returns a boolean list that has true if the corresponding list element is lesser than the given number'''
    return [x<val for x in col]

def aand(col1 : list[bool],col2 : list[bool])->list[bool]:
    '''Returns a boolean list by performing logical and between the 2 list elements'''
    if isBoolean(col1) and isBoolean(col2):
        if len(col1)==len(col2):
            return [x and y for x,y in zip(col1,col2) ]
        else:
            raise ValueError("Lists should be of the same length")
    else:
        raise TypeError("Expected a list of Boolean values")

def oor(col1 : list[bool],col2 : list[bool])->list[bool]:
    '''Returns a boolean list by performing logical or between the 2 list elements'''
    if isBoolean(col1) and isBoolean(col2):
        if len(col1)==len(col2):
            return [x or y for x,y in zip(col1,col2) ]
        else:
            raise ValueError("Lists should be of the same length")
    else:
        raise TypeError("Expected a list of Boolean values")

def xor(col1 : list[bool],col2 : list[bool])->list[bool]:
    ''' returns the elementwise xor
    '''
    if isBoolean(col1) and isBoolean(col2):
        if len(col1)==len(col2):
            return [x != y for x,y in zip(col1,col2) ]
        else:
            raise ValueError("Lists should be of the same length")
    else:
        raise TypeError("Expected a list of Boolean values")

def nnot(col : list[bool])->list[bool]:
    ''' Returns the elementwise not '''
    if isBoolean(col):
        return [not x for x in col]
    else:
        raise TypeError("Expected a list of Boolean values")       

def mean(col : list[bool])->float:
    ''' returns mean of the column'''
    return sum(col)/len(col)

def median(col : list[bool])->float:
    ''' returns median of the column'''
    return percentile(col,50)

def minimum(col : list[float])->float:
    ''' returns minimum list element'''
    return percentile(col,1)

def maximum(col : list[float])->float:
    ''' returns maximum list element'''
    return percentile(col,100)

def first_quart(col : list[float])->float:
    ''' returns 25th percentile of the column'''
    return percentile(col,25)

def third_quart(col : list[float])->float:
    ''' returns 75th percentile of the column'''
    return percentile(col,75)

def iqr(col : list[float])->float:
    ''' returns difference between the 2 quartiles'''
    return percentile(col,75) - percentile(col,25)

def percentile(col : list[float],per : int)->list:
    ''' returns nth percentile of the column'''
    if per>=1 and per<=100:
        return sorted(col)[round((per/100)*(len(col)))-1]
    else:
        raise ValueError("Percentile value should be between 1 and 100")

def trimmed_mean(col : list[float],per : int)->float:
    ''' returns the trimmed_mean'''
    if per>=1 and per<=100:
        k = round((per/100)*len(col))
        return mean(sorted(col)[k:len(col)-k])
    else:
        raise ValueError("Percentage value should be between 1 and 100")
#sum((x-x_mean)^2)


def isBoolean(col : list)->bool:
    ''' checks if the entire column is made up of boolean values'''
    if type(col)==list:
        return all(isinstance(x, bool) for x in col)
    else:
        return False

def prob(col : list[bool])->float:
    ''' returns probability of 1's in the column'''
    if isBoolean(col):
        return mean(col)
    elif type(col)==dict:
        return sum(col.values())
    else:
        raise TypeError("Expected a list of Boolean values")

def add(col:list[float],val:list)->list[float]:
    ''' returns a list incremented by val if the 2nd arg is a float

        returns the elementwise sum if the 2nd argument is a list
    '''
    if type(val) == list:
        if len(val) == len(col):
            return [x+y for x,y in zip(col,val)]
        else:
            raise ValueError("Lists should be of same length")
    else:
        return [x+val for x in col]

def sub(col:list[float],val:list)->list[float]:
    ''' returns a list decremented by val if the 2nd arg is a float

        returns the elementwise difference if the 2nd argument is a list
    '''
    if type(val) == list:
        if len(val) == len(col):
            return [x-y for x,y in zip(col,val)]
        else:
            raise ValueError("Lists should be of same length")
    else:
        return [x-val for x in col]

def mul(col:list[float],val:list)->list[float]:
    ''' returns a list scaled by val if the 2nd arg is a float

        returns the elementwise product if the 2nd argument is a list
    '''

    if type(val) == list:
        if len(val) == len(col):
            return [x*y for x,y in zip(col,val)]
        else:
            raise ValueError("Lists should be of same length")
    else:
        return [x*val for x in col]

def square(col:list[float])->list[float]:
    '''returns a new list with the elements squared'''
    return power(col,2)

def cube(col:list[float])->list[float]:
    '''returns a new list with the elements cubed'''
    return power(col,3)

def power(col:list[float],n:int)->list[float]:
    ''' returns a new list with elements raised to n '''
    return [x**n for x in col]

def conditional(cond1 :list[bool],cond2:list[bool])-> float:
    ''' returns the probability of condition1 given condition2 '''
    if isBoolean(cond1) and isBoolean(cond2):
        if len(cond1) == len(cond2):
            return prob(aand(cond1,cond2))/prob(cond2)
        else:
            raise ValueError("Lists should be of same length")
    else:
        raise TypeError("Expected a list of Boolean values")

def independent(col1:list[bool],col2:list[bool])-> bool:
    ''' returns true id col1 and col2 are independent'''
    if isBoolean(col1) and isBoolean(col1):
        if len(col1) == len(col1):
            return conditional(col1,col2)==conditional(col2,col1)
        else:
            raise ValueError("Lists should be of same length")
    else:
        raise TypeError("Expected a list of Boolean values")

def normalize(prob1):
    s = sum(prob1)
    return [i/s for i in prob1]
        
def total_prob(prob1,col):
    if type(col) == list:
        if all(x<=1 for x in prob1.values()):
            s = 0
            for key,value in prob1.items():
                s += value * prob(equal(col,key))
            return s
        else:
            raise ValueError("Probability values should be less than 1")
    else:
        if all(x<=1 for x in prob1.values()) and all(x<=1 for x in col.values()):
            if sum(col.values())==1:
                s = 0
                for key,value in prob1.items():
                    s += value * col[key]
                return s
            else:
                raise ValueError("Sum of probability values of the 2nd argument should be equal to 1")
        else:
            raise ValueError("Probability values should be less than 1")

class Emperical_DRV:    
    
    def __init__(self):
        self.probs = {}  
    
    def __init__(self,l1):
        unique_items = lambda list_with_duplicates: list(dict.fromkeys(list_with_duplicates))
        if type(l1)==list:
            if all(isinstance(x,int) or isinstance(x,float) for x in l1):
                self.probs = {x:l1.count(x)/len(l1) for x in set(l1)} 
            else:
                raise TypeError("Expected a list of numbers")      
        elif type(l1)==dict:
            if all(isinstance(x,int) or isinstance(x,float) for x in l1.keys()):
                s = sum(l1.values())
                if s==1:
                    self.probs = l1.copy()
                elif s>0:
                    self.probs = {x:y for x,y in zip(l1.keys(),normalize(l1.values()))}
                else:
                    raise ValueError("Expected positive values")
            else:
                raise TypeError("Expected keys to be numbers")  
        else:
            raise TypeError("Expected list or dict")
    
    def __eq__(self, rhs):
        if type(rhs)==int or type(rhs)==float:
            if rhs in self.probs.keys():
                return {rhs:self.probs[rhs]}
            else:
                return {}
        elif type(rhs)==type(self):
            return self.probs == rhs.values
        else:
            raise ValueError("Expected a dict or int or float")
    
    def __lt__(self, rhs):
        if type(rhs)==int or type(rhs)==float:
            return {x:y for x,y in self.probs.items() if x<rhs}
        elif type(rhs)==type(self):
            return self.probs < rhs.values
        else:
            raise ValueError("Expected a dict or int or float")

    def __gt__(self, rhs):
        if type(rhs)==int or type(rhs)==float:
            return {x:y for x,y in self.probs.items() if x>rhs}
        elif type(rhs)==type(self):
            return self.probs > rhs.values
        else:
            raise ValueError("Expected a dict or int or float")

    def __ge__(self, rhs):
        if type(rhs)==int or type(rhs)==float:
            return {x:y for x,y in self.probs.items() if x>=rhs}
        elif type(rhs)==type(self):
            return self.probs >= rhs.values
        else:
            raise ValueError("Expected a dict or int or float") 

    def __le__(self, rhs):
        if type(rhs)==int or type(rhs)==float:
            return {x:y for x,y in self.probs.items() if x<=rhs}
        elif type(rhs)==type(self):
            return self.probs <= rhs.values
        else:
            raise ValueError("Expected a dict or int or float") 
    


    def pmf(self,key):
        return prob(self==key)
    
    def cdf(self,key):
        return prob(self<=key)
    
    def E(self):
        return sum(x*y for x,y in self.probs.items())

    def transform(self,f):
        a1 = {x:f(x) for x in self.probs.keys()}    
        a2 = {val:sum([self.probs[i] for i,j in a1.items() if j==val]) for val in set(a1.values())}
        return Emperical_DRV(a2)

    def var(self):
        return self.transform(lambda x:x**2).expectation()-self.expectation()**2

    def sd(self):
        return sqrt(self.variance())


    