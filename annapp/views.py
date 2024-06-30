from .models  import Ann
from .serializers import AnnSerializer
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
class AnnList(ListModelMixin,
              CreateModelMixin,
              RetrieveModelMixin,
              DestroyModelMixin,
              UpdateModelMixin,
              GenericViewSet
              ):
    queryset = Ann.objects.all()
    serializer_class = AnnSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

