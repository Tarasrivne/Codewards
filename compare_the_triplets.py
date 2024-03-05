def compareTriplets(a, b):
    sol_a=0
    sol_b=0
    for i in range(3):
        if a[i]>b[i]:
            sol_a+=1
        if a[i]<b[i]:
            sol_b+=1
    return [sol_a,sol_b]