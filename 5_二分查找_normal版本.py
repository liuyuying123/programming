#二分查找，目标数组是升序的，找到目标数字第一次出现的下标

class Solution:
    def binary_search(self,nums,key):
        i=0
        j=len(nums)-1
        while i<=j:
            mid=(i+j)//2
            if key==nums[mid]:
                return mid
            if key<nums[mid]:
                j=mid-1
            else:
                i=mid+1
        
        return -1

if __name__=='__main__':
    Sol=Solution()
    nums=[1,4,4,5,7,7,8,9,9,10]
    key=1
    print(Sol.binary_search(nums,key))
    nums=[1,2,3,4,5,10]
    key=6
    print(Sol.binary_search(nums,key))


