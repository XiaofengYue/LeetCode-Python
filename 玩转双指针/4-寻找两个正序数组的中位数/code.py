# 方法一 二分查找

# 思路是怎么出来的呢
# m+n的长度 需要寻找 m+n/2 (3//2=1、4//2=2)
nums1 = [1]
nums2 = []
m, n = len(nums1), len(nums2) 

lens = m+n


def find_k_smallest_number(k):
    offset_1, offset_2 = 0, 0
    # 二分查找流程
    # 先排除k/2的数字
    ## 比如k=4 k//2 -1 = 1 比较0, 1 就是排除了k//2 = 2
    ## 比如k=5 k//2 -1 = 1 比较0, 1 就是排除了k//2 = 2
    while True:
        # 这里是预防一个数组已经便利完的情况
        if offset_1 == m:
            return nums2[offset_2 + k - 1]
        if offset_2 == n:
            return nums1[offset_1 + k - 1]
        if k == 1:
            return min(nums1[offset_1], nums2[offset_2])

        ## 需要注意访问越界的情况
        pred_off_1 = min(k//2-1, m-1-offset_1)
        pred_off_2 = min(k//2-1, n-1-offset_2)
        if nums1[offset_1 + pred_off_1] <= nums2[offset_2 + pred_off_2]: # 排除nums1的k//2个数据
            offset_1 += (pred_off_1+1)
            k = k - (pred_off_1+1)
        else:
            offset_2 += (pred_off_2+1)
            k = k - (pred_off_2+1)




if lens % 2 == 1:
    print(find_k_smallest_number((lens+1)//2))
else:
    print(( find_k_smallest_number(lens//2) + find_k_smallest_number(lens//2+1) )/2 )