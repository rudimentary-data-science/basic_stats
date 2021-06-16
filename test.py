import basic_prob as bp
import pandas as pd
df = pd.read_csv('Crime_R.csv')
col = df['CrimeRate'].to_list()
val1 = 50
val2 = 75
print(bp.prob(bp.aand(bp.greater(col,100),bp.less(col,120))))
a=[0,0,2,6,2,1,5,7,1,1,0,0]

person = ['m','f','m','m','f','m','f','f','f','f']
shirt = ['r','r','g','r','g','g','r','r','g','r']
print(bp.conditional(bp.equal(person,'m'),bp.equal(shirt,'r')))
import math
bp.sqrt()
bp.greater()
bp.mul()