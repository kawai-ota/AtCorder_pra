def main():  
  k = int(input())
  an = 7
  if an % k == 0:
    return 1
  for i in range(0, k):
    an = (10 * an + 7) % k
    if an % k == 0:
      return i + 2
  return -1  



print(main())    


