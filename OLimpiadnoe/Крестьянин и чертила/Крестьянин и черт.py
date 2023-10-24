import math
MaxN = int(input())
print(sum([MaxN//(2**i -1) for i in range(1, int(math.log2(MaxN + 1)) + 1, 1)]))
