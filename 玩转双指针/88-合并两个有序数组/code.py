class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        ### Version 1 ###
        ## nums1 = sorted(nums1[:m] + nums2[:n]) #地址变了不能这么写
        # nums1[m:] = nums2[:n]
        # nums1.sort()

        ### Version 2 ###
        pos = m + n -1

        # 当有一个数组已经被处理完毕
        while m>0 and n>0 :
            # 前面大于后面
            if nums1[m-1] > nums2[n-1]:
                nums1[pos] = nums1[m-1]
                m -= 1
            else:
                nums1[pos] = nums2[n-1]
                n -= 1
            pos -= 1
        # 如果nums1 没有完毕 -》 直接当作正确输出
        # 如果nums2 没有完毕
        nums1[:n] = nums2[:n]



nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
s = Solution()
s.merge(nums1, m, nums2, n)