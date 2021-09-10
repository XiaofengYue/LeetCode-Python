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
        i, j = 0, 0
        flag = True
        while i < m or j < n:
            # 后面下标数字大于前面的 我们要让i++  注意碰壁
            while nums1[i] < nums2[j]:
                i += 1
                if i == m + j:# 碰壁了 直接后边插入
                    nums1[i:] = nums2[j:]
                    flag = False

            # 到这里说明要执行插入
            front = nums1[i]
            while nums2[j] < front and j < n and flag:
                nums1.insert(i, nums2[j])
                nums1.pop()
                j += 1
                i += 1

s = Solution()
s.merge([1,4,5,0,0,0,0,0,0,0], 3, [0,2,2,3,7,8,9],7)