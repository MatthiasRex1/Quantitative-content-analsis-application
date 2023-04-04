import pdfminer.high_level as pdf
import numpy as numpy
from operator import itemgetter
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QAction,QFileDialog,QTextBrowser
from PyQt5.QtCore import QCoreApplication
#from PyQt5.QtDialog import 


listoffiles = []



    
   # self.textbox.setText('Готово')


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
         
        openfile = QPushButton('Add file', self)
        self.runbut = QPushButton('Run',self)
        self.runbut.setFlat(True)
        self.runbut.move(0, 340)

        #btn.resize(btn.sizeHint())
        openfile.clicked.connect (self.showDialog)
        openfile.move(0, 300)
        self.textbox = QTextBrowser(self)
        self.textbox.move(0,0)
        self.textbox.resize(300,300)
        #self.textbox.setText('asd')
        self.textbox.setReadOnly(True)
        self.textbox.setText('')
        self.runbut.clicked.connect (self.analysis)


        self.setGeometry(0, 0, 300, 200)
        self.resize (500,400)
        self.setWindowTitle('Content-analysis tool')
        self.show()


    def showDialog(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        listoffiles.append(fname)
      #  displaylist[fg-1]=displaylist[fg-1].append('/n')
        self.runbut.setFlat(False)
        self.textbox.setText('\n'.join(listoffiles))
        
    
        
        #self.lbl.setText(fname)
       # print(fname)

    def analysis(self):
        #print('sdsd')
        self.textbox.setText('Процесс пошел')
        wordstofind =[] 
        f=open('wordstofind.txt',encoding='utf-8')
        wordstofind=f.readlines()

        f.close()
       # print('sdsd1')
        yazaebals=len(wordstofind)
        for h in range(yazaebals):
            wordstofind[h]=wordstofind[h].rstrip()
        

       # print('sdsd2')
        #text = ''
        fgh=len(listoffiles)
        text = []
        for i in range(fgh):
            doptext=pdf.extract_text(listoffiles[i])
            text.append(doptext)

        lentext = len(text)
        #print(type(text[0]))
        #print(text[0])
        #print('asd')
        for i in range (lentext):
            #print(i)
            #print(text[i])
            
            doptext2=text[i]
            
            doptext2 = "".join(c for c in doptext2 if (c.isalpha() or c ==' ' or c=='\n' or c=='\t' ))
            doptext2 = doptext2.replace('\t',' ')
            print(doptext2)
            #doptext2 = " ".join(c for c in doptext2 if ())
            
           # print(doptext2)
            doptext2 = doptext2.lower()
            #print(doptext2)
            textmassive = doptext2.split()
            text2 = numpy.unique(textmassive)
            text2 = text2.tolist()
            n=len(text2)
            listofwords=[]
            #print(textmassive,'sd2')
            for gf in range(n):
                  j = textmassive.count(text2[gf])
              #self.textbox.setText(str(random()))
                  listofwords.append([text2[gf],j])
            #print(i)
            #print(listoffiles[i])
            #nameofwords='ss'
            
            #nomersimvola = listofwords[i].rfind('/')
            #print(listoffiles[i].rsplit('/',1))
            nameofwords= listoffiles[i].rsplit('/',1)
        
            #print(nameofwords)
            file = open(nameofwords[1]+'.txt','w',encoding='utf-8')
   
            listofwords = sorted(listofwords, key=itemgetter(1))
   # print('sd')
    #print (listofwords)
            i=0
            fgh2=len(listofwords)
            for j in range(fgh2):
              #print('sd')
                  file.write(str(listofwords[j][0])+' '+str(listofwords[j][1])+' '+str(listofwords[j][1]/len(text2))+'\n')

            file.write ('Total: '+str(len(textmassive)))
            file.close()
            #nameofwords='sd'
            
           # print(nameofwords)
            file = open(nameofwords[1]+'2.txt', 'w',encoding='utf-8')
            #print(wordstofind)
            fgh2=len(listofwords)
            fgh3=len(wordstofind)
            for h in range(fgh3):
                for j in range(fgh2):
                      if listofwords[j][0].find(wordstofind[h])!=-1:
                          file.write(str(listofwords[j][0])+' '+str(listofwords[j][1])+' '+str(listofwords[j][1]/len(text2))+'\n')
                      #break
            file.write ('Total: '+str(len(textmassive)))
            file.close()
        self.textbox.setText('Всё')
        



app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
