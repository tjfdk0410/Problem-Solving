"""
정수 배열이 주어졌을 때, 배열 안에서 곱이 최대가 되는 두 정수를 찾으시오.

Input: [-10, -3, 5, 6, -2]

Output: [-10, -3] 또는 [5, 6]
"""

inp = input()[1:-1].split(",")
new_inp =[]
for i in inp:
    new_inp.append(int(i))

# print(new_inp)
max_multi = 0
max_pair = []

for i in range(len(new_inp)):
    for j in range(len(new_inp)):
        if i <j:
            multi = new_inp[i] *new_inp[j]
            if multi > max_multi:
                max_multi= multi
                max_pair =[]
                max_pair.append([i, j])
            elif multi == max_multi:
                max_pair.append([i, j])


# print(max_pair, max_multi)
count = 0
for i in max_pair:
    print([new_inp[i[0]], new_inp[i[1]]])
    count +=1
    if count < len(max_pair): print("또는")


