H, W = map(int,input().split())
if H%3==0 or W%3==0:
  print(0)
  exit()


ans = min(W, H)
for i in range(1, H):
  tmp = max(abs(i*W-(W//2*(H-i))), abs(i*W-(-(-W//2)*(H-i))), abs(W//2*(H-i)-(-(-W//2)*(H-i))))
  ans = min(ans, tmp)
for i in range(1, W):
  tmp = max(abs(i*H-(H//2*(W-i))), abs(i*H-(-(-H//2)*(W-i))), abs(H//2*(W-i)-(-(-H//2)*(W-i))))
  ans = min(ans, tmp)
print(ans)