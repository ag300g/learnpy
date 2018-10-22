#!/usr/bin/env python
# -*- coding:UTF-8 -*-

'''
给出一个整数list, 返回最大和的子序列

e.g. input: [1,2,3,-3,1,1,-5,3,3,3,-1,2,-1,3,-10,1,1,3]
     output: 12 ([3,3,3,-1,2,-1,3])
'''

class Solution:
    # @param prices, a list of integer
    # @return an integer

    ## (1)
    '''
    思路: 子序列扩充,
    '''
    def maxSubsum(self, vl):
        if vl == []: return 0
        if min(vl) <= 0: return min(vl)
        start_index = 0
        end_index = len(vl)-1
        for i in range(len(prices)):
            if sum(vl[start_index:i]) < 0: start_index = i+1
            max_profit = max(prices[i]-current_min_price, max_profit)
        return max_profit

if __name__ == '__main__':
    vl = [1,2,3,-3,1,1,-5,3,3,3,-1,2,-1,3,-10,1,1,3]
    test = Solution()
    out1 = test.maxSubsum(vl)
    out2 = test.maxSubsum(vl)
    print(out1)
    print(out2)


def maxsub(lt):
    maxi, sumi = lt[0], lt[0]
    j=1
    for i in lt[1:]:
        print("************loop***********:"+str(j))
        j = j+1
        if sumi <= 0:
            sumi = i  ## 相当于restart
            print("条件1:"+str(sumi))
        else:
            sumi += i
            print("条件2:"+str(sumi))
        maxi = max(maxi, sumi)
        print("当前最优值:"+str(maxi))
    return maxi

lt = [1, 2, 3, -3, 1, 1, -5, 3, 3, 3, -1, 2, -1, 3, -10, 1, 1, 3]
maxsub(lt)
