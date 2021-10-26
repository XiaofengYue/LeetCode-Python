# nums = [1]
# k = 1
# def search_k_num(nums, k):
#     for i in range(k):
#         max = i
#         for j in range(i+1, len(nums)):
#             if nums[j] > nums[max]:
#                 max = j
#         if max!= i:
#             nums[i], nums[max] = nums[max], nums[i]
#     return nums[k-1]


# print(search_k_num(nums, k))


# nums = [3,2,1,5,6,4]
# k = 2

# import heapq
# heap = []
# for i in nums:
#     heapq.heappush(heap, i)
# print(heapq.nlargest(k, heap)[-1])


