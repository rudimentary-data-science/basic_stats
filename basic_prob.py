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

def greater(col : list[float|int], val:Any)->list[bool]:
    '''Returns a boolean list that has true if the corresponding list element is greater than the given number'''
    g = lambda x : True if x >val else False
    return [x>val for x in col]

def equal(col : list[float|int], val:Any)->list[bool]:
    '''Returns a boolean list that has true if the corresponding list element is equal to the given number'''
    return [x==val for x in col]

def less(col : list[float|int], val:Any)->list[bool]:
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

def minimum(col : list[float|int])->float|int:
    ''' returns minimum list element'''
    return percentile(col,1)

def maximum(col : list[float|int])->float|int:
    ''' returns maximum list element'''
    return percentile(col,100)

def first_quart(col : list[float|int])->float|int:
    ''' returns 25th percentile of the column'''
    return percentile(col,25)

def third_quart(col : list[float|int])->float|int:
    ''' returns 75th percentile of the column'''
    return percentile(col,75)

def iqr(col : list[float|int])->float|int:
    ''' returns difference between the 2 quartiles'''
    return percentile(col,75) - percentile(col,25)

def percentile(col : list[float|int],per : int)->list:
    ''' returns nth percentile of the column'''
    if per>=1 and per<=100:
        return sorted(col)[round((per/100)*(len(col)))-1]
    else:
        raise ValueError("Percentile value should be between 1 and 100")

def trimmed_mean(col : list[float|int],per : int)->float:
    ''' returns the trimmed_mean'''
    if per>=1 and per<=100:
        k = round((per/100)*len(col))
        return mean(sorted(col)[k:len(col)-k])
    else:
        raise ValueError("Percentage value should be between 1 and 100")
#sum((x-x_mean)^2)
def var(col : list[float|int])->float:
    ''' returns variance of the column'''
    return sum(square(sub(col,mean())))/(len(col)-1)

def sd(col : list[float|int])->float:
    ''' returns standard deviation of the column'''
    return sqrt(var(col))

def isBoolean(col : list)->bool:
    ''' checks if the entire column is made up of boolean values'''
    return all(isinstance(x, bool) for x in col)

def prob(col : list[bool])->float:
    ''' returns probability of 1's in the column'''
    if isBoolean(col):
        return mean(col)
    else:
        raise TypeError("Expected a list of Boolean values")

def add(col:list[float],val:float|list)->list[float]:
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

def sub(col:list[float],val:float|list)->list[float]:
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

def mul(col:list[float],val:float|list)->list[float]:
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