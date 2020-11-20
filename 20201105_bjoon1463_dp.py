"""
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
"""

x = int(input())
ans = 0

def dev3(x):
    if x%3 ==0: return x/3
def dev2(x):
    if x%2 ==0: return x/2
def sub1(x):
    return x-1

min_lst = []

def three_exp(min_lst, num):
    for i in range(num+1):
        min_lst.append(-1)
    min_lst[0]=0
    for i in range(1, num+1):
        if i ==1: min_lst[i] = 0
        elif i%6 ==0:
            min_lst[i]=min(min_lst[i//2], min_lst[i//3], min_lst[i-1])+1
        elif i%3==0:
            min_lst[i]=min(min_lst[i//3], min_lst[i-1])+1
        elif i%2==0:
            min_lst[i]= min(min_lst[i//2], min_lst[i-1])+1
        else: min_lst[i] = min_lst[i-1]+1
    # print(min_lst)
    return min_lst[num]



print(three_exp(min_lst, x))
