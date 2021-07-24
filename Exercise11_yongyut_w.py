pyramid = int(input("ความสูงพีระมิด"))
space = pyramid
for i in range(pyramid):
    space = space - 1
    print(" "*space,"*"*((i*2)+1))