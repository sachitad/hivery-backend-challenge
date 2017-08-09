from .models import Employee

from rest_framework import serializers


class FriendSerializer(serializers.ModelSerializer):
    """
    Only show basic info
    """
    class Meta:
        model = Employee
        fields = ('name', '_id', 'has_died')


class EmployeeSerializer(serializers.ModelSerializer):
    gender = serializers.ReadOnlyField(source='get_gender_display')
    balance = serializers.ReadOnlyField(source='balance_aud')
    tags = serializers.ReadOnlyField(source='get_tags')
    fruits = serializers.ReadOnlyField(source='get_favorite_fruits')
    vegetables = serializers.ReadOnlyField(source='get_favorite_vegetables')
    friends = FriendSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = ('_id', 'company', 'has_died', 'balance', 'picture_url',
                  'age', 'eye_color', 'name', 'gender', 'username', 'email',
                  'phone', 'address', 'about', 'registered', 'tags',
                  'greeting', 'friends', 'fruits', 'vegetables',)


class EmployeeAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('name', 'age', 'address', 'phone')


class EmployeeFavoriteFoodSerializer(serializers.ModelSerializer):
    fruits = serializers.ReadOnlyField(source='get_favorite_fruits')
    vegetables = serializers.ReadOnlyField(source='get_favorite_vegetables')

    class Meta:
        model = Employee
        fields = ('username', 'age', 'fruits', 'vegetables')