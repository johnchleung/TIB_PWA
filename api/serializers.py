from rest_framework import serializers
from .models import Tib


class TibSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tib
        fields = ('fldID', 'fldNo', 'fldStatus', 'fldCoordinate',
                    'fldOrientation', 'fldPicture', 'fldLastMDate', 
                    'fldEmpNameM')
        
        # fields = '__all__'