# 문제: 프로그래머스 120823 - 직각삼각형 출력하기
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120823

n = int(input())

for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()
