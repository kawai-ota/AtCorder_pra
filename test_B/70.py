a, b, c, d = map(int, input().split())

start_time = max(a, c) 
end_time = min(b, d)

result = max(0, end_time - start_time) 

print(result)