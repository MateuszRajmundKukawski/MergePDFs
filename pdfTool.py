# -*- coding: utf-8 -*-
from PyPDF2 import PdfFileMerger



class pdfTool(object):
    def mergePdfFile(self, pdflist, fname):
        if len(pdflist)<>0 and fname is not None:
            merger = PdfFileMerger()
            try:
                    for filename in pdflist:
                        with open(filename, 'rb') as myfile:
                            merger.append(myfile)
                        if self.var.get()==1:
                            os.remove(filename)
                    with open(fname, 'wb') as ofile:
                        merger.write(ofile)
                    return ('Ok', 'gotowe', True)
            except Exception as err:
                return ("ERROR", err, False)
            finally:
                 merger.close()
        elif len(pdflist)==0 and fname is None:
            return ('ERROR', 'Podaj dane:\n1. Folder roboczy lub plik\n2. Plik wyjściowy', False)
        elif len(pdflist)==0:
            return ('ERROR', 'Wybierz folder roboczy\n lub pliki', False)
        elif fname is None:
            return ('ERROR', 'Podaj plik wyjściowy', False)
