def find_missing(a,b):
    # checks for positive only integer
    if a > 0 and b > 0:
        if (a == None and b == None ) or a == b:
            return 0
            # checks for the missing number
        elif len(b) -len(b) == 1:
            lst=list(set(a)-set(b))
        return lst[0]
print find_missing([2,5],[2,5,7])
