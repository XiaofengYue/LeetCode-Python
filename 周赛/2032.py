import collections
nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]
res1 = collections.defaultdict(int)
res2 = collections.defaultdict(int)
res3 = collections.defaultdict(int)
for i in nums1:
    res1[i] = 1

for i in nums2:
    res2[i] = 2 if i in res1 else 1

for i in nums3:
    res3[i] = res2[i]+1 if i in res2 else res1[i]+1

#print(res1, res2, res3)
res = set()
for key,value in res2.items():
    if value == 2:
        res.add(key)

for key,value in res3.items():
    if value >= 2:
        res.add(key)

print(list(res))