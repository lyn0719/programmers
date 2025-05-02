# 문제: 프로그래머스 68622 - 두 개 뽑아서 더하기
# 난이도: Level 1
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            a = numbers[i] + numbers[j]
            if a not in answer:
                answer.append(a)
    answer.sort()
        
    return answer