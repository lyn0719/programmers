# 문제: 프로그래머스 181885 - 할 일 목록
# 난이도: Level 0
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181885

def solution(todo_list, finished):
    answer = []
    
    for i in range(len(todo_list)):
        if finished[i] == False:
            answer.append(todo_list[i])
    return answer