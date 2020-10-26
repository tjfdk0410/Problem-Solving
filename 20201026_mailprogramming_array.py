"""
사이즈가 m인 배열 X와 사이즈가 n인 배열 Y가 주어집니다.

두 배열은 모두 정렬된 상태입니다.

배열 X에는 정확히 n개의 비어있는 셀이 있다고 할 때,
배열 Y의 원소를 X 배열로 합치며 원소들을 정렬 시키시오.

Input
X = [0, 2, 0, 3, 0, 5, 6, 0, 0] (비어있는 셀은 0으로 표현되었음)
Y = [1, 8, 9, 10, 15]

Output
X = [1, 2, 3, 5, 6, 8, 9, 10, 15]
"""

# m = input("The size of first array: ")
# n = input("The size of second array: ")

X = input('X =')
Y = input('Y =')

def replace(arr):
    arr = arr[1:-1].split(', ')
    new_arr =[]
    for i in arr:
        if i != '0':
            new_arr.append(int(i))
    return new_arr

X = replace(X)
Y = replace(Y)

ans = sorted(X+Y)

print(ans)

