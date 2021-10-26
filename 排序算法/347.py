from collections import defaultdict, Counter

nums = [1,1,1,2,2,3]

[i[0] for i in Counter(nums).most_common(k)]







from collections import Counter

nums = [1,1,1,2,2,3]
k = 2

def shift_down(arr, root, k):
    val = arr[root]
    while root<<1 < k:
        child = root<<1
        if child|1 < k and arr[child|1][1] < arr[child][1]:
            child |= 1
        if arr[root][1] < val[1]:
            arr[root] = arr[child]
            root = child
        else:
            break
    arr[root] = val

def shift_up(arr, child):
    val = arr[child]
    while child>>1 > 0 and arr[child>>1][1] > val[1]:
        arr[child] = arr[child>>1]
        child >>= 1
    arr[child] = val

stat = Counter(nums)
stat = list(stat.items())
heap = [(0,0)]

for i in range(k):
    heap.append(stat[i])
    shift_up(heap, len(heap)-1)

for i in range(k, len(stat)):
    if stat[i][1] > heap[1][1]:
        heap[1] = stat[i]
        shift_down(heap, 1, k+1)

print([item[0] for item in heap[1:]])