#!/bin/env python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from PIL import Image
import os, sys
import zlib

def getFileName(filepath):
    file_list = []
    for root,dirs,files in os.walk(filepath):
        files.sort(key= lambda x:int(x[x.index('(')+1:-1]))
        for filespath in files:
            #print(os.path.join(root,filespath))
            file_list.append(os.path.join(root,filespath))

    return file_list

def MergePDF(filepath,outfile):
    fl = getFileName(filepath)
    canv=canvas.Canvas(outfile)
    for f in fl:
        img = Image.open(f)
        width,height = img.size;
        #width,height = (int(width*0.75),int(height*0.75))
        canv._pagesize = (width,height);
        img = img.resize((width,height),Image.ANTIALIAS)
        img.save(f+'.png')
        #print('img_width:' + str(img.width) + 'img_height:'+ str(img.height))
        size = canv.drawInlineImage(f+'.png',0,0)
        #print('page_size' + str(size))
        canv.showPage()
    canv.save()

def compressImg(img):
    imBytes = img.tobytes()
    compressedBytes =zlib.compress(imBytes)
    imReturn = Image.frombytes('RGB',img.size,zlib.decompress(compressedBytes))

if __name__=='__main__':
    #d = os.path.dirname(sys.argv[0])
    d=sys.argv[1]
    #print(d)
    outFileName= 'merge.pdf'
    if not d:
        d = os.getcwd()
    MergePDF(d,outFileName)
