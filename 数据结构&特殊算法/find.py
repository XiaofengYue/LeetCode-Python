class UF():
    def __init__(self, n):
        self.fa = [i for i in range(n+1)] # 从下标1开始
    
    def find(self, x):
        if self.fa[x] == x:
            return x
        else:
            self.fa[x] = self.find(self.fa[x]) # 路径压缩、把每个节点的父亲设置为根结点
            return self.fa[x]
    
    def merge(self, i, j):
        self.fa[self.find(i)] = self.find(j) # i的父亲的父亲=j的父亲
