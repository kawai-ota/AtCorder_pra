N = int(input())

amari1 = False
amari2 = False
amari_all = N % 3

N = str(N)
for i in range(len(N)):
  keta_num = N[i]
  keta_num = int(keta_num)
  if keta_num % 3 == 1:
    amari1 = True
  elif keta_num % 3 == 2:
    amari2 = True

if amari_all == 0:
  print(0)
elif amari_all == 1:
  if amari1 == True:
    if len(N) <= 1:
      print(-1)
    else:
      print(1)
  else:
    if len(N) <= 2:
      print(-1)
    else:
      print(2)
elif amari_all == 2:
  if amari2 == True:
    if len(N) <= 1:
      print(-1)
    else:
      print(1)
  else:
    if len(N) <= 2:
      print(-1)
    else:
      print(2)