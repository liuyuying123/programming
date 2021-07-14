#递归版二分查找

class Solution():
    def find_index(self,nums,key):
        i=0
        j=len(nums)-1
        return self.binary_search(nums,i,j,key)
        
    def binary_search(self,nums,i,j,key):
        if i>j:
            return -1
        mid=(i+j)//2
        if nums[mid]==key:
            return mid
        if nums[mid]>key:
            return self.binary_search(nums,i,mid-1,key)
        else:
            return self.binary_search(nums,mid+1,j,key)


if __name__=='__main__':
    Sol=Solution()
    nums=[1,4,4,5,7,7,8,9,9,10]
    key=1
    print(Sol.find_index(nums,key))
    nums=[1,2,3,4,5,10]
    key=6
    print(Sol.find_index(nums,key))
