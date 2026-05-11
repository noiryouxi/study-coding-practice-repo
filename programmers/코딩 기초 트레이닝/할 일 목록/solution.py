def solution(todo_list, finished):
    answer = []
    
    for todo, done in zip(todo_list, finished):
        if not done:
            answer.append(todo)
            
    return answer