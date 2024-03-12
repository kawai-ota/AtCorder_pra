DEBUG = False                                                                                                                                                     
import sys                                                                                                                                                        
sys.setrecursionlimit(2_000_000)                                                                                                                                  
                                                                                                                                               
if DEBUG:                                                                                                                                                         
    # ans: 4                                                                                                                                                      
    N, M = 8, 6                                                                                                                                                   
    A = [2, 3, 5, 7, 11, 13, 17, 19]                                                                                                                              
    N, M = 10, 1                                                                                                                                                  
    A = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]                                                                                                                            
    N, M = 10, 998244353                                                                                                                                          
    A = [100000007, 0, 1755647, 998244353, 495, 1000000000, 1755648, 503, 1755649, 998244853]                                                                     
else:                                                                                                                                                             
    N, M = [int(x) for x in input().split(" ")]                                                                                                                   
    A = [int(x) for x in input().split(" ")]                                                                                                                      
A = sorted(A)                                                                                                                                                     
if DEBUG:                                                                                                                                                         
    print(A)
k = 0                                                                                                                                                 
cnt = 1                                                                                                                                                           
max_cnt = 1                                                                                                                                                       
for i, a in enumerate(A):                                                                                                                                         
    if DEBUG:                                                                                                                                                     
        print(i)                                                                                                                                                  
    while True:                                                                                                                                                   
        if DEBUG:                                                                                                                                                 
            print(" -", k, cnt)                                                                                                                                   
        if k == N - 1:                                                                                                                                            
            break                                                                                                                                                 
        if A[k+1] - a < M:                                                                                                                                        
            k += 1                                                                                                                                                
            cnt += 1                                                                                                                                              
        else:                                                                                                                                                     
            break                                                                                                                                                 
    max_cnt = max(cnt, max_cnt)                                                                                                                                   
    cnt -= 1                                                                                                                                                      

print(max_cnt)