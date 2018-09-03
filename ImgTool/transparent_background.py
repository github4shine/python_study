from PIL import Image

def ComputerNear(cl1,cl2):
    if(abs(cl1-cl2) < 10):
        return True

def PureBlack(item, rate):
    return (0,0,0,item[3])


def TransparentImg(srcImageName,dstImageName):
    img = Image.open(srcImageName)
    img = img.convert("RGBA")
    datas = img.getdata()
    newData = list()
    cl=img.getpixel((10,10))
    for item in datas:
        if ComputerNear(item[0],cl[0]) and ComputerNear(item[1],cl[1]) and ComputerNear(item[2],cl[2]):
            newData.append(( 255, 255, 255, 0))
        else:
            newData.append(PureBlack(item,1))

    img.putdata(newData)
    img.save(dstImageName,"PNG")




import glob,os
if __name__ == '__main__':
    flist=glob.glob(".\\*.*")
    for f in flist:
        fi,ext = os.path.splitext(f)
        if(".jpg|.png".find(ext) == -1):
            continue
        TransparentImg(f, fi + "Trans.png")
