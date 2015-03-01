#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyPDF2 import PdfFileMerger



class pdfTool(object):
    def mergePdfFile(self, pdflist, fname, removeVal):
        if pdflist and fname:
            merger = PdfFileMerger()
            try:
                    for filename in pdflist:
                        with open(filename, 'rb') as myfile:
                            merger.append(myfile)
                        if removeVal==1:
                            os.remove(filename)
                    with open(fname, 'wb') as ofile:
                        merger.write(ofile)
                    return ('Ok', 'gotowe', True)
            except Exception as err:
                return ("ERROR", err, False)
            finally:
                 merger.close()
        elif not pdflist and not fname:
            return ('ERROR', 'Podaj dane:\n1. Folder roboczy lub plik\n2. Plik wyjściowy', False)
        elif not pdflist:
            return ('ERROR', 'Wybierz folder roboczy\n lub pliki', False)
        elif not fname:
            return ('ERROR', 'Podaj plik wyjściowy', False)
