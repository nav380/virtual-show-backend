from rest_framework import serializers
from Virtual_Showroom_db.models import ProductDetails, UserCart

# Serializer for ProductDetails model
class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetails
        fields = '__all__'  # Include all fields of the model


class UserCartSerializer(serializers.ModelSerializer):
    product_details = serializers.SerializerMethodField()

    class Meta:
        model = UserCart
        fields = '__all__' 

    def get_product_details(self, obj):
        """Fetch serialized details of the associated product."""
        product = obj.product_id
        return {
            "id": product.id,
            "product_code": product.product_code,
            "style_no": product.style_no,
            "product_type": product.product_type,
            "main_image": product.main_image.url if product.main_image else None,
        }
