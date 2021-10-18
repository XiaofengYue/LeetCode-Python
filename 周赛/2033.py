grid = [[1,5],[2,3]]
x = 1

nums = []
for l in grid:
    nums += l

num_min = min(nums)
num_max = max(nums)

res = float('inf')

for target in range(num_min, num_max+1, 1):
    _sum = 0
    flag = True
    for num in nums:
        if (target-num)%x == 0:
            _sum += abs(target-num)//x
        else:
            flag = False
            break
    if flag:
        res = min(res, _sum)
    
print(res)