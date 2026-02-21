numbers = [10, 15, 20, 25, 30]
result=list(filter(lambda x: x>15 and x%5==0,numbers))
print(result)