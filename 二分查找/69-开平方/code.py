x = 100
l, r =0, x

while l <= r:
    mid = (l+r)//2 

    res = pow(mid,2)
    if res > x:
        r = mid - 1
    elif res == x:
        print(mid)
    else:
        if pow(mid+1, 2) > x:
            print(mid)
        else:
            l = mid + 1
