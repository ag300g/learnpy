#!/usr/bin/env python
# -*- coding:UTF-8 -*-

'''
给出一个整数list, 返回最大和的子序列

e.g. input: [1,2,3,-3,1,1,-5,3,3,3,-1,2,-1,3,-10,1,1,3]
     output: 12 ([3,3,3,-1,2,-1,3])
'''

class Solution:
    # @param, a list of integer
    # @return an integer

    '''
    思路:
    (1) 从第一个元素开始累加, 累加结果大于0就继续累加, 这时还是有希望得到更大的的值得, 一旦累加结果小于或者等于0, 就要重新累加, 因为前一部分数据肯定不会存在于最优子序列中
    (2) 记录当前所有累加段的最大值即为全局最大值
    '''
    def maxSubsum(self, vl):
        if vl == []: return 0
        if max(vl) <= 0: return max(vl)
        sub_sum = vl[0]
        max_sub_sum = vl[0]
        for i in range(1, len(vl)):
            if sub_sum <= 0: sub_sum = vl[i]
            else: sub_sum += vl[i]
            max_sub_sum = max(max_sub_sum,sub_sum)
        return max_sub_sum

if __name__ == '__main__':
    vl = [1, 2, 3, -3, 1, 1, -5, 3, 3, 3, -1, 2, -1, 3, -10, 1, 1, 3]
    test = Solution()
    out = test.maxSubsum(vl)
    print(out)


