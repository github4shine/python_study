from PyPDF2 import PdfFileReader,PdfFileWriter
import glob
import os

def mergePdfFile(outFilePath,pdfFileList):
    outputPdfFileWriter = PdfFileWriter()
    for pdfFile in pdfFileList :
        inputPdfFile = PdfFileReader(file(pdfFile,"rb"))
        for page in inputPdfFile.pages:
            outputPdfFileWriter.addPage(page)
    outFileStream=file(outFilePath,"wb")
    outputPdfFileWriter.write(outFileStream)
    outFileStream.close()

def splitPdfFile(outFilePath,inputFile,startPages,EndPages):
    outputPdfFileWriter = PdfFileWriter()
    inputPdfFile = PdfFileReader(open(inputFile,"rb"))
    for pageIndex in range(startPages, EndPages):
        outputPdfFileWriter.addPage(inputPdfFile.pages[pageIndex])
    outFileStream=open(outFilePath,"wb")
    outputPdfFileWriter.write(outFileStream)
    outFileStream.close()

if(__name__=="__main11__"):
    #filelist = glob.glob('*.pdf')
    filelist =os.listdir("e:\pdftest")
    files = []
    for f in filelist:
        files.append("e:\\pdftest\\" + f)
    mergePdfFile("merge.pdf",files)

