from rest_framework import serializers


def not_me(name):
    if name == 'me':
        raise serializers.ValidationError('Имя "me" нельзя использовать')
    if name is None or name == "":
        raise serializers.ValidationError('Вы не указали имя')
