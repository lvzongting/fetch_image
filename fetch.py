import gl

#default num of download img
img_num=50   

file = open("list.lst")

for line in file.readlines():
    line=line.split()
    line.append(img_num)
#    print line[0]
#    print type(int(line[1]))
    gl.get_img(str(line[0]),'.',int(line[1]))

#gl.get_img('nano','.',1)
