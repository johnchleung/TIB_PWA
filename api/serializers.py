from rest_framework import serializers
from .models import Tbltib


class TbltibSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tbltib
        fields = ('fldID', 'fldNo', 'fldStatus', 'fldCoordinate ',
                    'fldOrientation', 'fldPicture ', 'fldLastMDate', 
                    'fldEmpNameM ')
        
        # fields = '__all__'