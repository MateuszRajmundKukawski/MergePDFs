# -*- coding: utf-8 -*-
from Tkinter import Frame, Tk, Button, StringVar, Label, IntVar, Checkbutton, W,E, SE
import os, glob
from tkFileDialog import askdirectory, asksaveasfilename,askopenfilename
from tkMessageBox import showinfo, showwarning
from PyPDF2 import PdfFileMerger




class mainGUI(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        pad_x = 10
        pad_y = 5
        buttonWidth = 25
        self.pdflist=[]
        self.fname = None
        self.workDir=None
        self.workDirText = StringVar()
        self.workDirText.set("Folder roboczy: ")
        self.var = IntVar()

        self.setWorkDir = Button(self, text='Wybierz folder roboczy', command=self.setDir, width=buttonWidth)
        self.setWorkDir.grid(row=1, column=0, sticky=W, padx=pad_x,pady = pad_y)

        multiFIleButton = Button(self, text ='Wybierz pliki do płączenia', command=self.getMulitiFile, width=buttonWidth)
        multiFIleButton.grid(row=1,column=1, sticky=W, padx=pad_x,pady = pad_y)


        self.removeCheckkButton = Checkbutton(self, variable=self.var, text="Usun pliki robocze", width=buttonWidth)
        self.removeCheckkButton.grid(row=2, column=1, sticky=W, padx=pad_x,pady = pad_y)

        self.saveFileButton = Button(self, text='Plik wyjściowy', command=self.saveFile, width=buttonWidth)
        self.saveFileButton.grid(row=2, column=0, sticky=W, padx=pad_x,pady = pad_y)


        self.workDirLabel = Label(self, textvariable=self.workDirText)
        self.workDirLabel.grid(row =0, column=0, columnspan=2, sticky=W)


        self.runAppButton = Button(self, text='Polacz pliki', command=self.mergePdfFile, width=buttonWidth)
        self.runAppButton.grid(row=3, column=0, columnspan=2, padx=pad_x,pady = pad_y)


        exitButton=Button(self, text='Exit', command=self.close_window, width=15)
        exitButton.grid(row=4, column=1,sticky = SE, padx=pad_x,pady = pad_y)

        self.pack(anchor='nw')


    def getInitDir(self):
        if self.workDir is None:
            initDir='D:\\'
        else:
            initDir=self.workDir
        return initDir


    def setDir(self):
        initDir= self.getInitDir()
        self.workDir = askdirectory(title='Set Dir', initialdir=initDir)
        self.pdflist = glob.glob(self.workDir+'\\*.pdf')
        self.workDirText.set("Folder roboczy: "+self.workDir)


    def saveFile(self):
        initDir= self.getInitDir()
        self.fname = asksaveasfilename(defaultextension='.pdf', initialdir=initDir, filetypes = [('pdf files', '.pdf'), ('text files', '.pdf')])


    def getMulitiFile(self):
        initDir= self.getInitDir()
        self.pdflist = askopenfilename(multiple=1, initialdir=initDir, filetypes = [('pdf files', '.pdf'), ('text files', '.pdf')])
        self.workDir = os.path.dirname(self.pdflist[0])
        self.workDirText.set("Folder roboczy: "+self.workDir)


    def mergePdfFile(self):
        if len(self.pdflist)<>0 and self.fname is not None:
            merger = PdfFileMerger()
            try:
                    for filename in self.pdflist:
                        with open(filename, 'rb') as myfile:
                            merger.append(myfile)
                        if self.var.get()==1:
                            os.remove(filename)
                    with open(self.fname, 'wb') as ofile:
                        merger.write(ofile)
                    showinfo(title='Ok', message='gotowe')
            finally:
                 merger.close()
        elif len(self.pdflist)==0 and self.fname is None:
            showwarning(title='ERROR', message='Podaj dane:\n1. Folder roboczy lub plik\n2. Plik wyjściowy')
        elif len(self.pdflist)==0:
            showwarning(title='ERROR', message='Wybierz folder roboczy\n lub pliki')
        elif self.fname is None:
            showwarning(title='ERROR', message='Podaj plik wyjściowy')


    def close_window(self):
        myWindow.quit()
        myWindow.destroy()



myWindow = Tk() #TWORZY OKNO
myWindow.minsize(348, 200) # DEFINIUJE ROZMIAR OKNA

myWindow.title("Połącz pliki pdf") # DEFINIUJE TUTUL OKNA/NAZWA PROGRAMU
app = mainGUI(master=myWindow) #LADUJE OKNO DO APLIKACJI
app.mainloop()