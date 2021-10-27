class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        cities = len(isConnected)
        Book = [0] * cities
        count = 0
        def dfs(x):
            Book[x] = 1
            for y in range(cities):
                if Book[y] ==0 and isConnected[x][y] == 1:
                    dfs(y)


        
        for i in range(cities): # 遍历每一个城市
            if Book[i] == 0:
                count += 1
                dfs(i)
        return count

        
s = Solution()
print(s.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))