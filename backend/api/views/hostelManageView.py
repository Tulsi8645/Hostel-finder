from rest_framework import generics
from api.models import Hostel,User
from api.serializers import HostelSerializer,UpdateHostelListSeriliazer, SingleHostelUpdateSeriliazer
from sklearn.feature_extraction.text import TfidfVectorizer
from django.conf import settings
from rest_framework.response import Response

#hostel register
class HostelList(generics.ListCreateAPIView):
    queryset=Hostel.objects.all()
    serializer_class=HostelSerializer
  
 

class UpdateHostelList(generics.ListAPIView):
     queryset=Hostel.objects.all()
     serializer_class=UpdateHostelListSeriliazer
     def get_queryset(self):
        identifier = self.kwargs.get('identifier', None)
        if identifier:
            if identifier.isdigit():
                user = User.objects.get(pk=identifier)
            else:
                user = User.objects.get(email=identifier)
            return user.hostel.all() #related name used here
        return Hostel.objects.all()
     
class SingleHostelUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset=Hostel.objects.all()
    serializer_class=SingleHostelUpdateSeriliazer
    # lookup_field='hostel_id'
