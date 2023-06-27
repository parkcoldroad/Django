from rest_framework import viewsets
from .models import Essay
from .serializers import EssaySerializer
from rest_framework.filters import SearchFilter

class EssayViewSet(viewsets.ModelViewSet):
    # 초기화
    queryset = Essay.objects.all()
    serializer_class = EssaySerializer

    filter_backends = [SearchFilter]
    search_fields = ('title', 'body')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # 현재 request를 보낸 유저
    # == self.request.user

    # ModelViewSet내에 있는 get_queryset을 오버라이딩하여 권한이 있는 사용자만 CRUD 작업을 수행할 수 있게 함
    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_superuser:
            qs = qs.all()
        elif self.request.user.is_authenticated:
            qs = qs.filter(author = self.request.user)
        else:
            qs=qs.none()
        return qs