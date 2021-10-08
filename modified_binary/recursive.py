def bar(n):
    if n <= 1:
        return
    bar(n-1)

bar(500)