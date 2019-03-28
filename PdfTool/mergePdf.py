from pyPdf import PdfFileReader,PdfFileWriter
import glob
import os

def mergePdfFile(outFilePath,pdfFileList):
    outputPdfFile = PdfFileWriter()
    for pdfFile in pdfFileList :
        tmpFile = file(pdfFile,"rb")
        inputPdfFile = PdfFileReader(tmpFile)
        for page in inputPdfFile.pages:
            outputPdfFile.addPage(page)
    outFile=file(outFilePath,"wb")
    outputPdfFile.write(outFile)
    outFile.close()

if(__name__=="__main__"):
    #filelist = glob.glob('*.pdf')
    filelist =os.listdir("e:\pdftest")
    files = []
    for f in filelist:
        files.append("e:\\pdftest\\" + f)
    mergePdfFile("merge.pdf",files)

