# Problem: Given two integer arrays, a and b, as the data needs to be queried.
# and given an array of queries, each query maybe one of the two forms below:

# modify query: [0, i, x] means we need to assign b[i] with the value of x. don’t need to return anything
# calculate query: [1, x] means we have to find the total number of pairs in a and b such that a[i] + b[j] = x. (for all i and j)
# Return an array of integers where each element represents the count of pairs that sum to x returned by each calculate query.
# Duplicate numbers should be counted.

def coolFeature(a, b, queries):
    a_dict = {}
    b_dict = {}
    for i in range(len(a)):
        if a[i] in a_dict:
            a_dict[a[i]] += 1
        else:
            a_dict[a[i]] = 1

    for i in range(len(b)):
        if b[i] in b_dict:
            b_dict[b[i]] += 1
        else:
            b_dict[b[i]] = 1

    returnArr = []
    for query in queries:
        if query[0] == 0:
            i = query[1]
            x = query[2]
            b_dict[b[i]] -= 1
            if x in b_dict:
                b_dict[x] += 1
            else:
                b_dict[x] = 1

        if query[0] == 1:
            x = query[1]
            counter = 0
            for key in list(a_dict.keys()):
                if x - key in b_dict:
                    counter += b_dict[x-key] * a_dict[key]

            returnArr.append(counter)

    return returnArr
