
def sum_all(*args) :
    return sum(args)

def sum_alllll(*args) :
    print(args)
    for i in args :
        print(i + i)
    return sum(args)


print(sum_all(1, 2, 3))
#print(sum_all(1, 2, 3, 23, 213, 2))
#print(sum_all(1, 2, 3, 4, 43, 53, 53, 23, 23))


print(sum_alllll(1, 2, 3))