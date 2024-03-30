n = int(input())

t_sum = a_sum = 0

for _ in range(n):
  t, a = map(int, input().split())
  
  if (t < t_sum and a < a_sum and t_sum / a_sum >= t / a) or (t < t_sum and a >= a_sum):
    t_sum = (t_sum + t - 1) // t * t
    a_sum = t_sum * a // t
  
  elif(t < t_sum and a < a_sum and t_sum / a_sum < t / a) or (a < a_sum and t >= t_sum):
    a_sum = (a_sum + a - 1) // a * a
    t_sum = a_sum * t // a
  
  else:
    t_sum, a_sum = t, a
    
print(t_sum + a_sum)