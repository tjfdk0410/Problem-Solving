"""
두 개의 정렬된 배열 X, Y가 주어졌을 때,
두 배열의 크기를 유지하면서 두 배열의 전체를 정렬하시오.

즉, 배열 X에는 작은 수들로 배열 Y에는 큰 수들로 구성되고
원소들은 정렬되어 있어야 합니다.

단, 정렬 시 다른 자료 구조를 사용하지 않고 주어진 배열만을 이용해야 합니다.

Input
X: [1, 4, 7, 8, 10]
Y: [2, 3, 9]

Output
X: [1, 2, 3, 4, 7]
Y: [8, 9, 10]
"""

X = input('X: ')
Y = input('Y: ')

def make_arr(inp):
    arr = inp[1:-1].split(', ')
    new_arr = []
    for i in arr:
        new_arr.append(int(i))
    return new_arr

X = make_arr(X)
Y = make_arr(Y)

new_arr = sorted(X+Y)

count = 0
new_X = []
new_Y = []
for i in new_arr:
    if count < len(X):
        new_X.append(i)
        count +=1
    else: new_Y.append(i)

print(new_X, new_Y)




