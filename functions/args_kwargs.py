def kill(*names,**namestwo):
    for x in names:
        print(x,end=" is dead ")
    for key,value in namestwo.items():
        print(f"{key}={value}")
kill( "Clare","Kate","Andrew",age=25, reason="because of killer")
