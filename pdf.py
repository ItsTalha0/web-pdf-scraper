import PyPDF2 as p2
import pandas as pd
import numpy as np
na_list=[]
roll_list=[]
def roll_extract(a):
    roll_no=''
    for i in range(20,35):
            if name[i][-10:]=='118College':
                for j in name[i][:-10]:
                    if j in '1234567890':
                        roll_no=roll_no+str(j)
    return roll_no
                
    
with open("pdf.pdf","rb") as p:
    my_pdf=p2.PdfFileReader(p)
    for j in range(my_pdf.getNumPages()):
        my_page=my_pdf.getPage(j)
        text=my_page.extractText()
        n=''
        name=[]
        for i in text:
            if i != ' ':
                n=n+i
            else:
                name.append(n)
                n=""
                
        name[2]=name[2][:-4]
        na_list.append(name[0]+' '+name[1]+' '+name[2])
        roll_list.append(roll_extract(name[20:35]))
        df=pd.DataFrame({"Name":na_list,"roll":roll_list})
        df.to_csv("roll.csv")
        
            
