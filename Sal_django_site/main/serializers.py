from rest_framework import serializers
from .models import UserPost, DonorPost, RecipientPost, Availability, CustomUser

class RegistrationSerializer(serializers.ModelSerializer):
   class Meta:
       model=CustomUser
       fields=('email','password','your_name')
       extra_kwargs={'password':{'write_only':True}}
       
   def create(self,validated_data):
       password=validated_data.pop('password',None)
       instance=self.Meta.model(**validated_data)
       if password is not None:
           instance.set_password(password)
       instance.save()
       return instance
class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = ("post_day","start_min","end_min","start_hour","end_hour",)

class UserPostSerializer(serializers.ModelSerializer):
    availability_set = AvailabilitySerializer(many=True, read_only=True)
    class Meta:
        model = UserPost

        fields = ("post_title","post_lat","post_long","post_deliver","donor_or_recip", "post_desc", "post_image", "post_slug","availability_set", )


class DonorPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonorPost
        fields =  "__all__"

class RecipientPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipientPost
        fields =  "__all__"




