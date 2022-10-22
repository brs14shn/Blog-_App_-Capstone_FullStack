
from .models import (
    Category,
    Post,
    Comment,
    Like,
    PostView
)
from .serializers import (
    CategorySerializers,
)
from rest_framework import generics

from rest_framework.permissions import IsAuthenticated



class CategoryViews(generics.ListCreateAPIView):
    queryset=  Category.objects.all()
    serializer_class= CategorySerializers
    permission_classes = [IsAuthenticated]

    #! Login olmuş kullanıcıyı ekliyorum.
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)