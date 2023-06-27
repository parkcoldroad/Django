from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Image, Documentation
from rest_framework.response import Response
from .serializers import ImageSerializer, DocumentationSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = [MultiPartParser, FormParser]


class DocumentationViewSet(viewsets.ModelViewSet):
    queryset = Documentation.objects.all()
    serializer_class = DocumentationSerializer
    parser_classes = [MultiPartParser]

    def create(self, request, *args, **kwargs):
        file = request.data['file']
        uploaded_file = Documentation.objects.create(name=file.name, file=file)
        serializer = DocumentationSerializer(uploaded_file)
        return Response(serializer.data)
