#include<vector>
#include<iostream>
using namespace std;
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
         
        if(nums.empty()){
            return vector<int>{-1,-1};
        }
        int rb = getrightboard(nums,target);
        int lb = getleftboard(nums,target);

        
        if(rb == -2 || lb == -2){
            return vector<int>{-1,-1};
        }
        if(rb - lb > 1){
            return vector<int>{lb+1,rb-1};
        }
        return vector<int>{-1,-1};
        
    }
private:
    int getrightboard(vector<int>& nums, int target){
        // int left = 0;
        // int right = nums.size();
        // int rightboart = -2;
        // while(left <= right){
        //     int mid = left + (right-left)/2;
        //     if(nums[mid] > target){
        //         right = mid - 1;
        //     }else{
        //         left = mid + 1;
        //         rightboart = left;

        //     }
        // }
        
        // 遵循左闭右开原则
        int left = 0;
        int right = nums.size();
        int rightboart = -2;
        while(left<right){ //不用<=的原因是，左闭右开 [3,3)这种情况就不需要再进来了 ，因为他里面一个元素都没有
            int mid = left + (right-left)/2;
            if(nums[mid] > target){// 在左边找
                right = mid; //取mid原因是因为 右开原则，新数组是不需要访问到mid的
            }else{// 在右边找
                left = mid+1; //取mid的原因是、左闭原则，答案有可能就是这个mid，我们是要取这个mid的
                rightboart = left;
            }
        }
        return rightboart;
    }
    int getleftboard(vector<int>& nums, int target){
        int left = 0;
        int right = nums.size();
        int leftboard = -2;
        while(left <= right){
            int mid = left + (right-left)/2;
            if(nums[mid] >= target){
                right = mid - 1;
                leftboard = right;
            }else{
                left = mid + 1;
            }
        }
        return leftboard;
    }
};

int main(){
    Solution s = Solution();
    vector<int>nums;
    nums.push_back(2);
    nums.push_back(2);
    int target = 3;
    s.searchRange(nums, target);
    return 0;
}