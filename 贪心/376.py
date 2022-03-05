from typing import List


# 贪心算法 使用图示的峰值表示
# class Solution:
#     def wiggleMaxLength(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return 1
        
#         total = 0
#         pre_grad = 0

#         for i in range(1, len(nums)):
#             cur_grad = nums[i] - nums[i-1]
#             if (cur_grad > 0 and pre_grad <= 0) or (cur_grad < 0 and pre_grad >= 0):
#                 total += 1
#                 print(nums[i-1])
#                 pre_grad = cur_grad
        
#         return total + 1

# s = Solution()
# s.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8])

# 动态规划解法
# class Solution {
# public:
#     int dp[1005][2];
#     int wiggleMaxLength(vector<int>& nums) {
#         memset(dp, 0, sizeof dp);
#         dp[0][0] = dp[0][1] = 1;

#         for (int i = 1; i < nums.size(); ++i)
#         {
#             dp[i][0] = dp[i][1] = 1;

#             for (int j = 0; j < i; ++j)
#             {
#                 if (nums[j] > nums[i]) dp[i][1] = max(dp[i][1], dp[j][0] + 1);
#             }

#             for (int j = 0; j < i; ++j)
#             {
#                 if (nums[j] < nums[i]) dp[i][0] = max(dp[i][0], dp[j][1] + 1);
#             }
#         }
#         return max(dp[nums.size() - 1][0], dp[nums.size() - 1][1]);
#     }
# };


s = Solution()
s.wiggleMaxLength([1,2,3])