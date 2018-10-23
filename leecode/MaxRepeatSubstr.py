#!/usr/bin/env python
# -*- coding:UTF-8 -*-

'''
给出一个字符串, 返回一个最长的子串, 要求这个子串中元素都连续且相同

e.g. input: dacccccjgkbbbbklajaaa
     output: cccccc
'''

class Solution:
    # @param, a list of char
    # @return an string

    '''
    思路:
    (1) 记录上一个字符, 当下一个字符和上一个字符一样时, 这个字符的重复次数+1
    (2) 当下一个字符与上一个字符不一致时, 更新上一次字符的内容, 并且重新计算重复次数
    '''
    def maxSubstr(self, str):
        if str == '': return 'the string is null'
        current_char = str[0]
        repeat_cnt = 1
        nonrepeat_char_list = []
        repeat_cnt_list = []
        for i in range(1, len(str)):
            if str[i] != current_char:
                nonrepeat_char_list.append(current_char)
                repeat_cnt_list.append(repeat_cnt)
                current_char = str[i]
                repeat_cnt = 1
            else:
                repeat_cnt += 1

        nonrepeat_char_list.append(current_char)
        repeat_cnt_list.append(repeat_cnt)
        cnt = max(repeat_cnt_list)
        i = repeat_cnt_list.index(cnt)
        return nonrepeat_char_list[i]*cnt

if __name__ == '__main__':
    str = 'dacccccjgkbbbbklajaaa'
    test = Solution()
    out = test.maxSubstr(str)
    print(out)