from rest_framework import serializers
from .models import canscan


class canscanSerializer(serializers.ModelSerializer):
    class Meta:
        model = canscan
        fields = ('id', 'Recycling_type', 'Green_points_earned', 'Bin_opened')
