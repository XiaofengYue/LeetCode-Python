# 寻找两数之和的下标
```Python
for i in range(len(numbers)):
    obj = target - numbers[i] # 需要找到的数字
    if obj in numbers[i+1:]:
        j = numbers.index(obj, i+1)
        return [i+1,j+1]
```
> O(n^2)超出了时间限制

## 太多相同的元素参与循环会导致时间复杂度过高
> 尝试用两个指针来滑动寻找

思路:i固定不变
    j向右移动
        如果碰壁或者i与j的值之和大于目标值了 说明i向前挪一步j该换个方向了: i+=1 j.way = -1
    i向左移动
        如果碰壁i或者i与j的值小于目标值了 说明j该换个方向了 j.way = 1

```Python
i, j = 0, 1
way = 1
while True:
    if numbers[i] + numbers[j] == target:
        return [i+1,j+1]
    else:
        # 一直向右前进 直到碰壁或者之和大于target
        if way == 1 and (j == len(numbers)-1 or numbers[i]+numbers[j] > target):
            way = -way
            i += 1
        # 一直向左前进 直到碰壁(i)或者之和小于Target
        elif way == -1 and (j == i+1 or numbers[i] + numbers[j] < target):
            way = -way
        else:
            j+= way
```
## 双指针 头尾双指针夹向中间
> 有单调性、O(n)时间

如果两数之和大于目标值我们可以让尾巴向内走，两数之和小于目标值我们让左边的头部前进一点.

```Python
i, j = 0, len(numbers)-1
while i < j:
    if numbers[i] + numbers[j] == target:
        return [i+1, j+1]
    elif numbers[i] + numbers[j] > target:
        j -= 1
    else:
        i += 1
```
