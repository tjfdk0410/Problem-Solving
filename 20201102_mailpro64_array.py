"""
바이너리 배열을 주어졌을 때, 한 개의 0을 1로 바꿔 연속된 1의 수가 가장 많아지도록 하는 0의 인덱스를 찾으시오.

Input: [0, 0, 1, 0, 1, 1, 1, 0, 1, 1]

Output: 7
"""

inp = input("Input: ")

inp = inp[1:-1].split(", ")
new_arr = []
for i in inp:
    new_arr.append(int(i))

print(new_arr)

def count_one(order, lst):
    lst[order] = 1
    print(lst)
    count = 0
    max_count = 0
    for i in lst:
        if i == 0:
            if max_count < count:
                max_count = count
            count ==0
        else: count +=1
    return max_count

count_num = 0
max_count_num =0
index = 0
for i in range(len(inp)):
    if inp[i] == 0:
        count_num = count_one(i, inp)
        if count_num > max_count_num:
            max_count_num = count_num
            index = i

print(index)




