#num1是numm2的子集，现要求找到num1中的数字在num2中下一个更大的数字，就是右边第一个比它更大的数字，没有的话
# 则返回-1，如num1=[4,1,2] num2=[1,3,4,2]，则返回[-1,3,-1]

#这道题很巧妙，它是将num2中每个数字的下一个更大的数字都找到，使用了栈来实现。

class Solution:
    def next_largets_num(self,num1,num2):
        stack=[]
        largest_num={}
        for x in num2:
            while stack and stack[-1]<x:
                largest_num[stack[-1]]=x
                del stack[-1]
            stack.append(x)
        
        for num in stack:
            largest_num[num]=-1

        return [largest_num[x] for x in num1]

if __name__=='__main__':
    Sol=Solution()
    num1=[4,1,2]
    num2=[1,3,4,2]
    print(Sol.next_largets_num(num1,num2))