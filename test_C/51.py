sx,sy,tx,ty = map(int,input().split())
xsub=tx-sx
ysub=ty-sy
Ans=""
Ans+='U'*ysub
Ans+='R'*xsub
Ans+='D'*ysub
Ans+='L'*(xsub+1)
Ans+='U'*(ysub+1)
Ans+='R'*(xsub+1)
Ans+='D'
Ans+='R'
Ans+='D'*(ysub+1)
Ans+='L'*(xsub+1)
Ans+='U'
print(Ans)