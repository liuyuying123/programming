#[1,3,4],[2,3,5]合并为[1,2,3,3,4,5]
class Solution:
    def mergeSortedArray(self,A,B):
        len_A=len(A)
        len_B=len(B)
        i,j=0,0
        sorted_Array=[]
        while i<len_A and j<len_B:
            if A[i]<B[j]:
                sorted_Array.append(A[i])
                i+=1
            else:
                sorted_Array.append(B[j])
                j+=1
        while i<len_A:
            sorted_Array.append(A[i])
            i+=1
        while j<len_B:
            sorted_Array.append(B[j])
            j+=1
        return sorted_Array

if __name__=='__main__':
    A=[1,3,5]
    B=[1,2,4,6]
    sol=Solution()
    merged_Array=sol.mergeSortedArray(A,B)
    print(merged_Array)
