import basic_prob as bp
import pandas as pd
from time import time
import timeit
df = pd.read_csv('Crime_R.csv')
col = df['CrimeRate'].to_list()
val1 = 50
val2 = 75
# print(bp.prob(bp.aand(bp.greater(col,100),bp.less(col,120))))
a=[0,0,2,6,2,1,5,7,1,1,0,0]

# person = ['m','m','m','m']
shirt =  ['r','r','r','g']
sh = {'r':0.4,'g':0.4}
p_m = {'r':0.3,'g':1}
bp.sqrt(25)

l1 = [1,3,4,1,1,2]
l2 = {1:0.5,2:0.2,3:0.3}
l3 = {1:0.6,2:0.2}
# a = bp.Discrete_RV(l2)
# print(a.cdf(4))

a1 = {-2:1/15,-1:2/15,0:3/15,1:4/15,2:5/15}
d = {1:1/6,2:1/6,3:1/6,4:1/6,5:1/6,6:1/6}
# rv = bp.Emperical_DRV(d)
# a2 = {val:[i for i,j in a1.items() if j==val] for val in set(a1.values())}
rv = bp.Binomial_rv(0.5,10)
a = lambda x:x**2
from time import time

def test_time2():
    start_time = time()
    print(time()-start_time)


E = bp.E
print(E(rv.transform(lambda x:x)))
print([E(rv+2),E(2+rv),E(2*rv),E(rv*2),E(rv**2)])
f = lambda x:x**2
print()
