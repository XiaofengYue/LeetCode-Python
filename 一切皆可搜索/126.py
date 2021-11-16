from collections import defaultdict, deque
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        def judge_joint(str1, str2):
            return 1 if sum([0 if str1[i]==str2[i] else 1 for i in range(len(str1))]) == 1 else 0
        
        # 建立图结构
        wordList.insert(0, beginWord)
        if endWord not in wordList:
            return []
        endIndex = wordList.index(endWord)
        graph = [[0 for i in range(len(wordList))] for j in range(len(wordList))]
        for i in range(len(wordList)-1):
            for j in range(i+1, len(wordList)):
                graph[i][j] = judge_joint(wordList[i], wordList[j])
                graph[j][i] = graph[i][j]
        
        # BFS寻找每层节点
        successors = defaultdict(set)
        def _bfs(begin_index, end_index, graph, successors):
            queue = deque()
            queue.append(begin_index)
            visited = set()
            visited.add(begin_index)

            while queue:
                queue_back = queue.copy()
                for i in range(len(queue)):
                    now = queue.popleft()
                    visited.add(now)
                    for next in range(len(graph[0])):
                        if graph[now][next] == 1 and next not in visited and next not in queue_back:
                            queue.append(next)
                            successors[now].add(next)
        _bfs(0, endIndex, graph, successors)

        # DFS回溯法
        path = [0]
        res = []
        def _dfs(begin_index, successors, end_index):
            if begin_index == end_index:
                res.append(path[:])
            if begin_index not in successors:
                return 
            for next in successors[begin_index]:
                path.append(next)
                _dfs(next, successors, end_index)
                path.pop()
        _dfs(0, successors, endIndex)

        return [[wordList[index] for index in word_list]for word_list in res]


s = Solution()
s.findLadders(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"])