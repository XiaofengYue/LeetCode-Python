from collections import Counter


# 大顶堆
class Solution:
    from collections import Counter
    def frequencySort(self, s: str) -> str:
        arr = Counter(s)
        arr = list(arr.items())
        heap = [('',0)]
        res = ''
        for i in range(len(arr)):
            heap.append(arr[i])
            self.shift_up(heap, len(heap)-1)
        for i in range(len(arr)):
            res += heap[1][0] * heap[1][1]
            heap[1] = ('', 0)
            self.shift_down(heap, 1, len(arr)+1)
        return res

    def shift_up(self, arr, child):
        val = arr[child]
        while child>>1 > 0 and arr[child>>1][1] < val[1]:
            arr[child] = arr[child>>1]
            child >>= 1
        arr[child] = val


    def shift_down(self, arr, root, k):
        val = arr[root]
        while root<<1 < k:
            child = root<<1
            if child|1 < k and arr[child|1][1] > arr[child][1]:
                child |= 1
            if arr[child][1] > val[1]:
                arr[root] = arr[child]
                root = child
            else:
                break
        arr[root] = val

s = Solution()
print(s.frequencySort('tree'))