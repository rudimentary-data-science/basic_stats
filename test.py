import basic_prob as bp
import pandas as pd
df = pd.read_csv('Crime_R.csv')
col = df['CrimeRate'].to_list()
val1 = 50
val2 = 75
print(bp.prob(bp.aand(bp.greater(col,100),bp.less(col,120))))
a=[0,0,2,6,2,1,5,7,1,1,0,0]

#person = ['m','m','m','m']
shirt =  ['r','r','r','g']
sh = {'r':0.4,'g':0.4}
p_m = {'r':0.3,'g':1}
#print(bp.conditional(bp.equal(person,'m'),bp.equal(shirt,'r')) + bp.conditional(bp.equal(person,'m'),bp.equal(shirt,'g')))
bp.sqrt(25)

l1 = [1,3,4,1,1,2]
l2 = {1:0.5,2:0.2,3:0.3}
l3 = {1:0.6,2:0.2}
a = bp.Discrete_RV(l2)
print(a.cdf(4))