class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1/self.myPow(x,-n)
        if n % 2 == 1:
            return x*self.myPow(x,n-1)
        return self.myPow(x*x,n//2)