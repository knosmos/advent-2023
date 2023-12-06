'''
- i^2 + ti - rec > 0
-t + sqrt(t^2 - 4*rec) ) / (-2)

Time:        48     93     85     95
Distance:   296   1928   1236   1391
'''
import math

t = 48938595
rec = 296192812361391

print(math.floor((-t - math.sqrt(t**2 - 4*rec)) / (-2)) - (math.floor((-t + math.sqrt(t**2 - 4*rec)) / (-2))+1) + 1)