#!/usr/bin/env python
# -*- coding:UTF-8 -*-

'''
给出一个股票的时序数据,返回最大获利的值

e.g. input: [10,9,8,7,2,5,6,11,3,9,4,15,5]
     ## (1) 只允许买卖一次: output: 12 (3块买进==15块卖出)
     ## (2) 允许任意次买卖, 卖出后才能再次买入: output: 26 (2买进--11卖出,3买进--9卖出,4买进--15卖出)
     ## (3) 最多允许2次买卖, 卖出后才能再次买入: output: 21 (2买进--11卖出, 3买进--15卖出)

思路: 只需要记录当前价格最低点, 和当前的收益值就行
'''



class Solution:
    # @param prices, a list of integer
    # @return an integer

    ## (1)
    def maxProfit1(self, prices):
        if prices == []: return 0
        max_profit = 0
        current_min_price = max(prices)
        for i in range(len(prices)):
            if prices[i] < current_min_price: current_min_price = prices[i]
            max_profit = max(prices[i]-current_min_price, max_profit)
        return max_profit

    ## (2)
    '''
    只要后一个值比前一个值大, 就会把增加的值计入到收益中
    相当于计算 max_profit = max(0,a[i+1]-a[i])
    '''
    def maxProfit2_1(self, prices):
        if prices == []: return 0
        lowest = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] > lowest:
                max_profit += prices[i]-lowest
            lowest = prices[i]
        return max_profit


    def maxProfit2_2(self,prices):
        if prices == []: return 0
        max_profit = 0
        for i in range(len(prices) - 1):
            max_profit += max(0, prices[i+1] - prices[i])
        return max_profit

    ## (3)
    '''
    从左边开始记录到当前时间为止的最大收益, 存入一个list
    从右边开始计算从j开始到最后的最大收益, 然后逐个比较 左半+右半 找出最大的
    '''
    def maxProfit3(self, prices):
        if prices == []: return 0
        maxtol, leftmax, rightmax = 0, 0, 0
        left = []
        low, high = prices[0], prices[-1]
        for i in range(len(prices)):
            leftmax = max(leftmax, prices[i] - low)
            left.append(leftmax)
            if prices[i] < low: low = prices[i]
        for j in range(len(prices) - 1, -1, -1):
            rightmax = max(rightmax, high - prices[j])
            maxtol = max(maxtol, left[j] + rightmax)
            if prices[j] > high: high = prices[j]
        return maxtol


if __name__ == '__main__':
    prices = [10, 9, 8, 7, 2, 5, 6, 11, 3, 9, 4, 15, 5]
    test = Solution()
    out1 = test.maxProfit1(prices)
    out2 = test.maxProfit2(prices)
    out3 = test.maxProfit3(prices)
    print(out1)
    print(out2)
    print(out3)

