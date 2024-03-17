movie_num, watch_movie = map(int, input().split())
rate_list = list(map(int, input().split()))
rate_list = sorted(rate_list)

rate = 0
if movie_num == watch_movie:
  for i in range(watch_movie):
    rate = (rate + rate_list[i]) / 2
else:
  for i in range(movie_num - watch_movie, movie_num):
    rate = (rate + rate_list[i]) / 2

print(rate)