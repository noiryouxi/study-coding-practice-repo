def solution(keyinput, board):
    x, y = 0, 0
    
    max_x = board[0] // 2
    max_y = board[1] // 2
    
    for key in keyinput:
        if key == "up":
            y = min(y + 1, max_y)
        elif key == "down":
            y = max(y - 1, -max_y)
        elif key == "right":
            x = min(x + 1, max_x)
        elif key == "left":
            x = max(x - 1, -max_x)
    
    return [x, y]