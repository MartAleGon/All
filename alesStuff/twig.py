from PIL import Image
im= Image.open("twiggy.jpg")
im.getdata()
newData = []
print (im.size)
x=list(im.getdata())
xLen= len(x)
print(xLen)
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)
for i in range(0, xLen-1):
    Sum= x[i][0] + x[i][1] + x[i][2]
    if Sum<182:
        newData.append(darkBlue)
    elif (Sum < 364):
        newData.append(red)
    elif (Sum < 546):
        newData.append(lightBlue)
    else:
        newData.append(yellow)
        
im.putdata(newData)
    
im.show()


