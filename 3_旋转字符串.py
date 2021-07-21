#给定一个字符串和一个offset，例如abcdef和2，返回旋转的字符串efabcd

class Solution:
    def string_reverse(self,strings,offset):
        string_length=len(strings)
        if offset>string_length:
            offset%=string_length
        temp_string=(strings+strings)[string_length-offset:2*string_length-offset]
        for i in range(string_length):
            strings[i]=temp_string[i]
        # return strings
    

if __name__=='__main__':
    s=['a','b','c','d','e']
    offset=2
    sol=Solution()
    sol.string_reverse(s,offset)
    print(s)