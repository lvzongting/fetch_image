import gl
import fkr
import bg

#default num of download img
img_num=10   

file = open("list.lst")

for line in file.readlines():
    line=line.split()
    line.append(img_num)
#    print line[0]
#    print type(int(line[1]))
#    gl.get_img(str(line[0]),'google',int(line[1]))
#    fkr.get_img(str(line[0]),'fkr',int(line[1]))
    bg.get_img(str(line[0]),'bg',int(line[1]))
