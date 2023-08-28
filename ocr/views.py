from rest_framework.views import APIView
from rest_framework.response import Response
from PIL import Image
import pytesseract

class OCR(APIView) :
    def get(self, request) :
        text = pytesseract.image_to_string(Image.open('media/Sketches 2.jpeg'), lang='kor+chi_sim+eng')

        with open("media/result.txt", "w", encoding='utf-8') as f :
            f.write(text)
            # f.write(text.replace(" ", ""))

        return Response({})
    
