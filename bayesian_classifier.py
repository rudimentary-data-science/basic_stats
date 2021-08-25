import basic_prob as bp
import numpy as np
import pandas as pd


def decision(X,C,x):
    posterior = {}
    print(x)
    evidence = 1 
    for i in range(len(X)):
        #print(list((X[i]==x[i]).values())[0])
        evidence*= list((X[i]==x[i]).values())[0]
    for cls,priori in C.probs.items():
        likelihood = bp.conditional(X==x,C==cls)
        posterior[cls] = (priori*likelihood)/evidence
    return max(posterior, key = lambda x: posterior[x])
        

def main():
    df = pd.read_csv('cleaned_data.csv')
    df.drop(df.iloc[:, 0:2], inplace = True, axis = 1)
    X = []
    for i in range(len(df.columns)-1):
        X.append(bp.Emperical_drv(list(df.iloc[:, i])))
    C = bp.Emperical_drv(list(df.iloc[:, -1]))
    d1 = list(df.iloc[0])
    print(decision(X,C,d1[:-1]))
    print(d1[-1])

if __name__ == '__main__':
    main()