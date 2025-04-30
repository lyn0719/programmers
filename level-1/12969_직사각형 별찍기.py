# 문제: 프로그래머스 12969 - 직사각형 별찍기
# 난이도: Level 1
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12969

a, b = map(int, input().strip().split(' '))

for i in range(b):
    for j in range(a):
        print("*", end="")
    print()