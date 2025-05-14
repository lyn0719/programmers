# 문제: 프로그래머스 142086 - 가장 가까운 같은 글자
# 난이도: Level 1
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/142086

def solution(s):
    answer = []
    test = {}
    
    s_list = list(s)
    
    for i in range(len(s_list)):
        if s_list[i] not in test:
            answer.append(-1)
            test[s_list[i]] = i
        else:
            answer.append(i - test[s_list[i]])
            test[s_list[i]] = i
    
    return answer
