from rest_framework import serializers


class UrlValidator:
    def __call__(self, value):
        if 'youtube.com' not in value:
            raise serializers.ValidationError("Нельзя использовать ссылки на сторонние ресурсы, кроме youtube.com")