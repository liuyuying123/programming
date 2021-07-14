#例如将123反转成321
class Solution:
    def reverse(self,number):
        a=int(number/100)
        b=int((number%100)/10)
        c=number%10
        return c*100+b*10+a

if __name__=='__main__':
    number=123
    sol=Solution()
    nummber_reverse=sol.reverse(number)
    print('---before reverse：{}'.format(number))
    print('---after reverse: {}'.format(nummber_reverse))