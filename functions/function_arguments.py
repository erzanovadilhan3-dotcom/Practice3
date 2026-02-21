def my_func(x,y,z):
    return(x==y+z)
x,y,z=list(map(int,input().split()))
print(my_func(x,y,z))