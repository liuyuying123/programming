#问题描述，给定选手的得分，然后前三名分别位gold medal silver medal bronze medal，接下来就是相对排名
# 例如[2,3,4,5,1]:[4，bronze medal,sliver medal,gold medal,5]

class Solution:
    def sort_xiangdui(self,score):
        #得到分数-顺序的键值对
        score_order={}
        for i in range(len(score)):
            score_order[score[i]]=i
        
        #给分数排个序
        answer=[0]*len(score)
        sorted_score=sorted(score,reverse=True)
        for i in range(len(sorted_score)):
            if i==0:
                ans='gold medal'
            elif i==1:
                ans='silver medal'
            elif i==2:
                ans='bronze medal'
            else:
                ans=i+1
            answer[score_order[sorted_score[i]]]=ans
        return answer

if __name__=='__main__':
    score=[5,4,3,2,1]
    Sol=Solution()
    rank=Sol.sort_xiangdui(score)
    print(rank)
            
            

