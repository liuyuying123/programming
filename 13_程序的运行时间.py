#给定程序的输入输出时间，计算程序具体的执行时间
class Solution:
    def time(self,inputs):
        enter_time={}
        exit_time={}
        for input in inputs:
            name,key,time=input.split(' ')
            if key=='Enter':
                if name not in enter_time.keys():
                    enter_time[name]=[time]
                else:
                    enter_time[name].append(time)
            else:
                if name not in exit_time.keys():
                    exit_time[name]=[time]
                else:exit_time[name].append(time)
        
        #计算总执行时间：
        ans=[]
        for key in enter_time.keys():
            enter=enter_time[key]
            exit=exit_time[key]
            exec_time=0
            for j in range(len(enter)):
                exec_time+=int(exit[j])-int(enter[j])
            ans.append(key+'|'+str(exec_time))
        return ans

if __name__=='__main__':
    Sol=Solution()
    a=["F1 Enter 10","F1 Exit 18","F2 Enter 18","F2 Exit 20","F1 Enter 20","F1 Exit 24"]
    print(Sol.time(a))
