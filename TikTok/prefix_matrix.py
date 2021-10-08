#got this
def prefix_matrix(arr):
    top = 0
    bottom = len(arr) - 1
    left = 0
    right = len(arr[0]) - 1
    res = [[0] * len(arr[0]) for i in range(0, len(arr))]
    
    for i in range(0, len(arr)):
        for j in range(0, len(arr[0])):
            left_ele = 0
            top_ele  = 0
            dia_ele = 0
            if j - 1 >= left:
                left_ele = arr[i][j-1]
            if i - 1 >= top:
                top_ele = arr[i-1][j]
            if i-1 >= top and j-1 >= left:
                dia_ele = arr[i-1][j-1]
            res[i][j] = arr[i][j] - left_ele - top_ele + dia_ele
    
    print(res)
    
if __name__ == "__main__":
    prefix_matrix([[1,2], [2,4]])
    prefix_matrix([[4,10,11],[9,22,25],[12,33,45]])