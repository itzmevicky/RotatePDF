import PyPDF2
from rest_framework.response import Response
from .serializer import *
from rest_framework import generics
import os

class PDF(generics.GenericAPIView):
    serializer_class =  PDFRotateSerializer


    def get(self,request):
        return Response()

    def post(self, request,):

        File = request.FILES.get('Upload_File')
        rotation = str(request.data['Rotation']).split(' ')[0]
        pagenumber = request.data['Page_Number_To_Rotate']            
        
        if not bool(File):
            return Response('File Missig :( ')

        if (bool(rotation) or bool(pagenumber))  == False:
            return Response('Either Rotation or Pagenumber Missig :( ')


        if str(File).split('.')[1] == 'pdf' :
            pdfReader = PyPDF2.PdfFileReader(File)
            pdfWriter = PyPDF2.PdfFileWriter()
            if int(pagenumber) > pdfReader.numPages :
                return Response(f'Enterd Page Number Cannot be greater than {pdfReader.numPages}')

            for x in range(pdfReader.numPages):
                page = pdfReader.getPage(x)
                if x == (int(pagenumber) - 1):
                    page = pdfReader.getPage(x).rotateCounterClockwise(int(rotation))
                pdfWriter.addPage(page)

            with open(str(File),'wb') as pr:
                pdfWriter.write(pr)      

            path = os.path.abspath(str(File))
            

            return Response(f'File Stored Successfully : {path}')
        return Response('Invalid File Format')
        

    


    