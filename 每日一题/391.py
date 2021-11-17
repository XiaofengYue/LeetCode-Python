class Solution:
    def isRectangleCover(self, rectangles) -> bool:
        lines = []
        # true for right, false for left

        for rectangle in rectangles:
            lines.append((rectangle[0], rectangle[1], rectangle[3], True))
            lines.append((rectangle[2], rectangle[1], rectangle[3], False))
        
        # 多级排序
        lines = sorted(sorted(sorted(lines, key = lambda z: z[1]), key = lambda y: y[0]), key=lambda x: x[3])
        print(lines)
        sumLines = []
        sumLine = None
        for i in range(len(lines)):
            line = lines[i]
            if sumLine == None:
                sumLine = line
                continue
            if line[0] != sumLine[0] or line[3] != sumLine[3]:
                sumLines.append(sumLine)
                sumLine = line
                continue
            if sumLine[2] != line[1]:
                sumLines.append(sumLine)
                sumLine = line
                continue
            sumLine = (line[0], sumLine[1], line[2], sumLine[3])
        
        sumLines.append(sumLine)

        lineMap = {}

        for line in sumLines:
            key = (line[:3])
            if key not in lineMap:
                lineMap[key] = line[3]
            else:
                if line[3] != lineMap[key]:
                    lineMap.pop(key)
                else:
                    return False
        
        edges = list(lineMap.keys())

        if len(edges) == 2 and edges[0][1] == edges[1][1] and edges[0][2] == edges[1][2]:
            return True
        return False


s = Solution()
s.isRectangleCover([[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]])

