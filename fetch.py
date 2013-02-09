import gl
import fkr
import bg

#default num of download img
img_num=10   

file = open("list.lst")

for line in file.readlines():
    line=filter(None,(line[:-1] + '   ' + str(img_num)).split('  '))
#    print line
#    print line[0]
#    print line[1]
#    print type(int(line[1]))
#    print '####'
#    gl.get_img(str(line[0]),'google',int(line[1]))
#    fkr.get_img(str(line[0]),'fkr',int(line[1]))
    bg.get_img(str(line[0]),'bg',int(line[1]))
