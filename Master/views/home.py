from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Virtual_Showroom_db.models import ProductDetails
from .serializers import ProductDetailsSerializer

class Home(APIView):
    def get(self, request):
        products = ProductDetails.objects.all()
        serializer = ProductDetailsSerializer(products, many=True)  # Serialize all products
        return Response({"products": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductDetailsSerializer(data=request.data)  # Deserialize JSON request data
        if serializer.is_valid():
            product = serializer.save()  # Save the product to the database
            return Response({"message": "Product created successfully", "product": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
