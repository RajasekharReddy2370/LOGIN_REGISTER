from rest_framework.serializers import ModelSerializer
from .models import Details

class Detailsserializer(ModelSerializer):
    class Meta:
        model = Details
        fields = '__all__'