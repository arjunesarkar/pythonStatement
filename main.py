#statemant
#from lib2to3.pytree import convert
korea = 155000
if korea >= 300000:
    print("Sure go to Korea")
elif korea > 150000:
    print("Not sure")
else: print("not go")

# Problem solving

width = int(input("Your Width: "))
level = input("(K)g or (L)bs")
if level.upper() =="K":
    converter = width/0.45
    print("width in lbs: "+str(converter))
else:
    converter = width*0.45
    print("width in kgs: "+ str(converter))