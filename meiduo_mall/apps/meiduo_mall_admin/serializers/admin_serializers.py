
from rest_framework import serializers

from users.models import User


class AdminModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'mobile', 'password',
                  'groups', 'user_permissions']

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        groups = validated_data.pop('groups')
        user_permissions = validated_data.pop('user_permissions')
        user = User.objects.create_superuser(**validated_data)
        user.groups = groups
        user.user_permissions = user_permissions
        user.save()
        return user
