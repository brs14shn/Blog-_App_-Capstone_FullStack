
from rest_framework import serializers
from .models import (
    Category,
    Post,
    Comment,
    Like,
    PostView
)
from django.utils.timezone import now



class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields =(
            "id",
            "name"
        )

class CommentSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    post =  serializers.StringRelatedField()
    user_id= serializers.IntegerField()
    post_id= serializers.IntegerField()

    class Meta:
        model=Comment
        fields =(
            "id",
            "post_id",
            "user_id",
            "user",
            "post",
            "content"
        )
    read_only_fields =(
        "time_stamp"
    )

class LikeSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    post =  serializers.StringRelatedField()
    user_id= serializers.IntegerField()
    post_id= serializers.IntegerField()
    class Meta:
        model =  Like
        fields =(
            "id",
            "post_id",
            "user_id",
            "user",
            "post", 
        )
class PostViewSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    post =  serializers.StringRelatedField()
    user_id= serializers.IntegerField()
    post_id= serializers.IntegerField()
    class Meta:
        model =  Like
        fields =(
            "id",
            "post_id",
            "user_id",
            "user",
            "post", 
        )

class BlogPostsSerializers(serializers.ModelSerializer):
    # ! Object-level validation  👇
#   """
#   SerializerMethodField() methodu kullandık, bu method, modelden gelen tabloya serializers işlemi uygularken ek olarak veri eklemek için kullanılıyor
#   """
    days=serializers.SerializerMethodField()
    comment_count =serializers.SerializerMethodField()
    like_count=serializers.SerializerMethodField()
    view_count=serializers.SerializerMethodField()
    category=serializers.StringRelatedField()
    category_id= serializers.IntegerField()
    author=serializers.StringRelatedField()
    author_id=serializers.IntegerField()

    class Meta:
        model=Post

        fields =(
            "id",
            "title",
            "content",
            "image",
            "author",
            "author_id",
            "status",
            "publish_date",
            "last_updated",
            "days",
            "comment_count",
            "like_count",
            "view_count",
            "category",
            "category_id",

        )
    def get_days(self,obj):
        return (now() - obj.publish_date).days 


    def get_comment_count(self,obj):
        return Comment.objects.filter(post=obj.id).count()
    
    def get_like_count(self,obj):
        return Like.objects.filter(post=obj.id).count()
    
    def get_view_count(self,obj):
        return PostView.objects.filter(post=obj.id).count()

     #! Field-level validation
    # def validate_title(self,value):
    #     if value.lower() =="angular" and  value.lower() =="vue" :
    #         raise serializers.ValidationError("angular and vue can not be our blogapp")










# ! Object-level validation  

#   """
#   SerializerMethodField() methodu kullandık, bu method, modelden gelen tabloya serializers işlemi uygularken ek olarak veri eklemek için kullanılıyor
#   """

#! Field-level validation
#   def validate_task(self,value):
#     if value.lower() =="angular" and  value.lower() =="vue" :
#         raise serializers.ValidationError("angular and value can not be our blogapp")

#! Category içerisindeki tüm postlara ulaşmak için related name =categorys için categorys=PostSerializers(many=True) # tüm postları getirebiliriz

#! timezone
# Postun yayınlanma süresini from django.utils.timezone import  ederek days=serializers.SerializerMethodField() kullanarak
#  def get_days(self,obj):
# return (now() - obj.publishdate).days ile bulabiliriz.

#! StringRelatedField()
# category=serializers.StringRelatedField()
  # 🍵 buradaki category post modelindeki filed default id, biz __str__ methodundaki veriyi böylece çağırdık artık field category_name olarak gelir.