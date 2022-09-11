#TC - O(E), E is the number of edges
#SC - O(N), N is the number of people
class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        degree = [0] *(n+1)
        #print(Degree)
        for person,trusted in trust:
            degree[person]-=1
            degree[trusted]+=1
        
        for i in range(1,len(degree)):
            if degree[i] == n-1:
                return i
        
        return -1
        
class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        degree = [0] *n
        #print(Degree)
        for person,trusted in trust:
            degree[person-1]-=1
            degree[trusted-1]+=1
        
        for i in range(len(degree)):
            if degree[i] == n-1:
                return i+1
        
        return -1