data = [("ARTEM KOTENKO", 17), ("Dana", 16), ("Max", 18)]
result=sorted(data,key=lambda x: x[1]%3)
print(result)