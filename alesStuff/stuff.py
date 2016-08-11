from PIL import Image
im= Image.open("3 cute2.jpg")
im.getdata()
newData = []
print (im.size)
x=list(im.getdata())
xLen= len(x)
print(xLen)
violet = (148, 0, 211)
brown = (205, 133, 63)
lightBlue = (124, 252, 0)
yellow = (255, 20, 147)
for i in range(0, xLen-1):
    Sum= x[i][0] + x[i][1] + x[i][2]
    if Sum<182:
        newData.append(violet)
    elif (Sum < 364):
        newData.append(yellow)
    elif (Sum < 546):
        newData.append(lightBlue)
    else:
        newData.append(brown)
        
im.putdata(newData)
    
im.show()
