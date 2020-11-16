"""
정수 배열이 주어졌을 때, 짝수 위치의 원소가 양 옆의 원소보다 큰 수가 되도록 배치하시오.
배열에는 중복 원소가 없다고 가정합니다.

Input: [1, 2, 3, 4, 5, 6, 7]
Output: [1, 3, 2, 5, 4, 7, 6]

Input: [9, 6, 8, 3, 7]
Output: [6, 9, 3, 8, 7]

Input: [6, 9, 2, 5, 1, 4]
Output: [6, 9, 2, 5, 1, 4]
"""

""" 재배열 말고 조건에 맞지 않는 부분만 수정하기를 원했던 문제인 것 같다"""
inp = input()[1:-1].split(",")
sort_inp = sorted([int(i) for i in inp])

len_inp = len(sort_inp)
len_hlf_inp = len(sort_inp)//2

max_lst = sort_inp[-len_hlf_inp:]
min_lst = sort_inp[:-len_hlf_inp]

ans_lst = []

for i in range(len_hlf_inp):
    ans_lst.append(min_lst[i])
    ans_lst.append(max_lst[i])

if len_inp %2 ==1: ans_lst.append(min_lst[len_hlf_inp])

print(ans_lst)









