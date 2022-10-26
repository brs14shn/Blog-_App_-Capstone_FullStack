
from .models import (
    Category,
    Post,
    Comment,
    Like,
    PostView
)
from .serializers import (
    CategorySerializers,
    CommentSerializers,
    LikeSerializers,
    PostViewSerializers,
    BlogPostsSerializers,
)
from rest_framework import generics

# from rest_framework.permissions import IsAuthenticated



class CategoryViews(generics.ListCreateAPIView):
    queryset=  Category.objects.all()
    serializer_class= CategorySerializers
    # permission_classes = [IsAuthenticated]

    #! Login olmuş kullanıcıyı ekliyorum.
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)


class CommentView(generics.CreateAPIView):
    queryset= Comment.objects.all()
    serializer_class= CommentSerializers

class LikeView(generics.ListCreateAPIView):
    queryset= Like.objects.all()
    serializer_class= LikeSerializers

class PostView(generics.ListCreateAPIView):
    queryset= PostView.objects.all()
    serializer_class= PostViewSerializers

class PostBlogView(generics.ListCreateAPIView):
    queryset= Post.objects.all()
    serializer_class= BlogPostsSerializers

class PostBlogRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Post.objects.all()
    serializer_class= BlogPostsSerializers
    lookup_field="id"






