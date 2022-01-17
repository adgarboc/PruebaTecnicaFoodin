from rest_framework.serializers import ModelSerializer, ValidationError

from foodin_api_v1.models import Product


class ProductModelSerializer(ModelSerializer):

    def validate_precio(self, value):
        if not value > 0:
            raise ValidationError("Price must be greater than zero")
        return value

    class Meta:
        model = Product
        fields = '__all__'

