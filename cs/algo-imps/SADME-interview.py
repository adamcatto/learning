# module -- Skiena Algo Design Manual Example interview problems

def Interview_1_28(a1, b1):
    a=a1
    b=b1
    count=0
    remainder=0
    divided=0
    def subDiv(n,d):
        nonlocal count
        if(n-d>=0):
            nonlocal count
            count += 1
            subDiv(n-d, d)
        else:
            nonlocal remainder
            remainder=n
        nonlocal divided
        divided=float(count)+(float(remainder)/float(d))
    subDiv(a,b)
    print(f'\n{a} divided by {b} is {count} with remainder {remainder}\n\nIn other words, {a} divided by {b} is {divided}\n\ni.e. {a}/{b}={divided}')

Interview_1_28(26,5)