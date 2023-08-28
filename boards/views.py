import pytesseract
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, SAFE_METHODS
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.status import HTTP_204_NO_CONTENT
from pyuploadcare import Uploadcare
from .models import Board
from .serializers import *

'''
class BoardViewSet(ModelViewSet) :
    serializer_class = BoardSerializer
    queryset = Board.objects.all()
'''

def index(request) :
    return render(request, "board_form.html", {"name" : request.user.username })

class Boards(APIView) :
    permission_classes = [IsAuthenticatedOrReadOnly]

    async def test(self, uploadcare, file_object) :
        return uploadcare.upload(file_object)

    async def upload(self, file_path) :
        try :
            uploadcare = Uploadcare(public_key=settings.UC_PUBLIC_KEY, secret_key=settings.UC_SECRET_KEY)
            with open(file_path, 'rb') as file_object:
                result = await self.test()
        except :
            result = None
        return result

    def post(self, request) :
        serializer = BoardSerializer(data=request.data)

        if serializer.is_valid() :
            board = serializer.save()   

            if "file" in request.FILES :
                board.loadedfile = request.FILES["file"]
                board.save()   

                uploadcare = Uploadcare(public_key=settings.UC_PUBLIC_KEY, secret_key=settings.UC_SECRET_KEY)
                
                # 1. multipart upload 100M 초과 
                # with open(board.loadedfile.path, 'rb') as file_object:
                #     ucare_file = uploadcare.multipart_upload(file_object)

                # 2. direct upload 100M 이하 
                print("board.loadedfile.size : ", board.loadedfile.size)
                if board.loadedfile.size < settings.FILE_SIZE_LIMIT :
                    with open(board.loadedfile.path, 'rb') as file_object:
                        ucare_file = uploadcare.upload(file_object)
                    
                    # response = asyncio.run(self.upload(board.loadedfile.path)) 
                    iamge_path = f"https://ucarecdn.com/{ucare_file.uuid}/"
                    board.file_link = iamge_path

            board.author = request.user
            board.save()
            return Response(BoardSerializer(board).data)
        else :
            return Response(serializer.errors)
    
    def get(self, request) :
        boards = Board.objects.all()
        serializer = BoardOverviewSerializer(boards, many=True)
        return Response(serializer.data)
        
class BoardDetail(APIView) :
    permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk) :
        board = self.get_object(pk)
        serializer = BoardSerializer(board)
        return Response(serializer.data)
    
    def put(self, request, pk) :
        board = self.get_object(pk)

        if not board.author == request.user :
            raise PermissionDenied

        serializer = BoardSerializer(
            instance= board,
            data= request.data,
            partial= True
        )

        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors)
    
    def delete(self, request, pk) :
        board = self.get_object(pk)
        board.delete()
        return Response(HTTP_204_NO_CONTENT)

    def get_object(self, pk) :
        try :
            board = Board.objects.get(pk=pk)
            return board
        except Board.DoesNotExist :
            raise NotFound


'''
@api_view(['GET'])
def get_board_all(request) :
    boards = Board.objects.all()
    return Response({
    'status' : '200 OK'
})
'''