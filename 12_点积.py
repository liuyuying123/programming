class Solution:
    def dotmul(self,a,b):
        if len(a)!=len(b) or len(a)==0 or len(b)==0:
            return -1
        sum=0
        for i in range(len(a)):
            sum+=a[i]*b[i]
        return sum
if __name__=='__main__':
    Sol=Solution()
    a=[1,2,3]
    b=[4,5,6]
    print(Sol.dotmul(a,b))