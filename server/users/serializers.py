from rest_framework import serializers,validators
from django.contrib.auth.models import User





class RegisterSerializers(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True,
        validators=[validators.UniqueValidator(queryset=User.objects.all(),message="Email must unique")]   
    )
    password =serializers.CharField(
        required=True,
        write_only=True,
        style={"input_type":"password"}
    )



    class Meta:
        model =User