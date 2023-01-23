##PDFCROPPER.py
## 
## Original: https://www.reddit.com/r/techsupport/comments/du9z82/comment/f7ne9ml/?utm_source=share&utm_medium=web2x&context=3
## Edited by snowynguyen

from PyPDF2 import PdfWriter, PdfReader
from math import ceil, floor
from copy import copy

inpdf = input("Input the pdf path >>>")
outputfilename = "SPLIT - %s"%inpdf
papersizes = {'a4p':[595,842],'a4l':[842,595],'a3p':[842,1190],'a3l':[1190,842]}
sizeprompt = int(input("What paper size? \n1. A4 Portrait\n2. A4 Landscape\n3. A3 Portrait\n4. A3 Landscape \n5. Custom\nType your number >>>"))
dictofsizes = {1:'a4p', 2:'a4l', 3:'a3p', 4:'a3l'}	
if sizeprompt ==5:
	customwidth = int(input("Enter the paper width in PostScript >>>"))
	customheight = int(input("Enter the paper height in PostScript >>>"))

	sizewanted = [customwidth,customheight]
	
else:
	try:
		sizewanted = papersizes.get(dictofsizes.get(sizeprompt))
	except:
		print ("The number you entered is not an option. Please restaert the program.")
	



def readFile(inpdf):
    input1 = PdfReader(open(inpdf, "rb"))
    output1 = PdfWriter()
    
    pages = len(input1.pages)

    doTheThing(input1, output1, pages)
    
    
    
def doTheThing(input1,output1,pages):


    for pagenum in range(pages):
    
        page = input1.pages[pagenum]
        size = input1.pages[pagenum].mediabox
        width = ceil(size.width) #input1.getPage(pagenum).cropBox.getUpperLeft()
        height = ceil(size.height)
        
        ratioheight = (width/sizewanted[0])*sizewanted[1]#(width/papersizes.get('a4')[0])*papersizes.get('a4')[1]
        
        pageheight = height-ratioheight
        currenttotalheight = pageheight
        numofdivs = height/ratioheight
        numofiter = 1
        vardict = {}

        while numofiter <= ceil(numofdivs):
        
            pagecopy = None
            pagecopy = copy(page)
            pagecopy.cropbox.lower_left = (0, currenttotalheight)
            pagecopy.cropbox.upper_right = (width, currenttotalheight+ratioheight)
            output1.add_page(pagecopy)
            page = input1.pages[pagenum]
            
            currenttotalheight = currenttotalheight - ratioheight
            numofiter = numofiter + 1
            
            
    finalCountdown(output1)
    


def finalCountdown(output):
    
    with open(outputfilename, "wb") as out_f:
        output.write(out_f)
        

		
		
readFile(inpdf)