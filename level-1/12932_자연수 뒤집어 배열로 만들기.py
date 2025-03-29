# 문제: 프로그래머스 12932 - 자연수 뒤집어 배열로 만들기
# 난이도: Level 1
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    answer = []
    nlist = str(n)[::-1]
    
    for i in nlist:
        answer.append(int(i))
    
    return answer