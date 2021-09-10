# 合并两个有序数组

## Version 1
最简单的思路也是把两个数组拼接然后重新排序
```Python
nums1[m:] = nums2[:n]
nums1.sort()
```

## Version 2
用两个指针来遍历