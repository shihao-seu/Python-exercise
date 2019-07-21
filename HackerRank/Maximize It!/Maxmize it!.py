# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
if __name__=='__main__':
    K,M=map(int,input().split())
    Source=[]
    for _ in range(K):
        N,*my_list=map(int,input().split())
        Source.append(my_list)
    def fn_S(L):
        a=list(map(lambda x:x**2,L))
        sum=0
        for _ in a:
            sum+=_
        return sum%M
    L_source=list(product(*Source))
    print(max(map(fn_S,L_source)))