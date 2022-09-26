def find_end(n,m,obstacles,teleports):
    pos_i = 0
    pos_j = 0
    reached_obstacle = False
    
    while pos_i < n and pos_j < m and not reached_obstacle:
        for i, j in obstacles:
            if pos_i == i and pos_j == j:
                if pos_i != n-1 and pos_j != m-1:
                    return False
                reached_obstacle = True
                
        for s_d in teleports:
            if s_d[0] == pos_i and s_d[1] == pos_j:
                pos_i = s_d[2]
                pos_j = s_d[3]
        
        pos_j += 1
        if pos_j == m - 1:
            pos_j = pos_j % m
            pos_i += 1
    
    if reached_obstacle:
        return False

    return True

if __name__ == '__main__':
    print(find_end(3,3,[[2,1]],[[0,1,2,0]]))
    print(find_end(3,4,[[1,1]],[[0,2,0,1], [0,3,2,0]]))