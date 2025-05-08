# 문제: 프로그래머스 42748 - K번째수
# 난이도: Level 1
# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    
    for command in commands:
        slice_list = array[command[0]-1:command[1]]
        slice_list.sort()
        answer.append(slice_list[command[2]-1])
        
    return answer