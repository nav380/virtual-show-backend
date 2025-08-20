from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from Virtual_Showroom_db.models import ProductDetails, UserCart
from .serializers import ProductDetailsSerializer, UserCartSerializer
from rest_framework.permissions import IsAuthenticated

from django.http import HttpResponse

class ProductMasterAPI(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, pk=None):
        product_id = request.GET.get("product_id")  
        print('id', product_id)  #
        
        if pk:  
            try:
                product = ProductDetails.objects.get(pk=pk)  
                serializer = ProductDetailsSerializer(product)  # Serialize the single product
                print('accha_data', serializer.data)
                return Response(serializer.data, status=status.HTTP_200_OK)
                
            except ProductDetails.DoesNotExist:
                return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        else:  
            products = ProductDetails.objects.all()  # Fetch all products
            print("object data", products)    
            serializer = ProductDetailsSerializer(products, many=True)  # Serialize all products
            print("python data", serializer)  
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductDetailsSerializer(data=request.data)  # Deserialize JSON request data
        if serializer.is_valid():
            serializer.save()  # Save the product to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            product = ProductDetails.objects.get(pk=pk)  
        except ProductDetails.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductDetailsSerializer(product, data=request.data, partial=False)  # Update the product
        if serializer.is_valid():
            serializer.save()  # Save updated product
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            product = ProductDetails.objects.get(pk=pk) 
        except ProductDetails.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductDetailsSerializer(product, data=request.data, partial=True)  # Update the product partially
        if serializer.is_valid():
            serializer.save()  # Save updated product
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddToCartAPI(APIView):
    def get(self, request, product_id=None):
        """
        Fetch all cart entries or a specific cart entry by its product_id.
        """
        user = request.user.id

        if product_id:
            try:
                cart_entry = UserCart.objects.get(product_id=product_id, created_by=user, is_active=True)
                cart_serializer = UserCartSerializer(cart_entry)
                return Response(cart_serializer.data, status=status.HTTP_200_OK)
            except UserCart.DoesNotExist:
                return Response({"error": "Cart entry not found"}, status=status.HTTP_404_NOT_FOUND)

        cart_entries = UserCart.objects.filter(created_by=user, is_active=True)
        if not cart_entries.exists():
            return Response({"message": "No products in the cart"}, status=status.HTTP_404_NOT_FOUND)

        cart_serializer = UserCartSerializer(cart_entries, many=True)
        return Response({"cart": cart_serializer.data}, status=status.HTTP_200_OK)



    def post(self, request):
        """
        Add or update a product in the cart.
        """
        user = request.user  # Get the logged-in user

        # Get the product_id from the request data
        # data = request.data
        product_id = request.data.get('product_id')
        if not product_id:
            return Response({"error": "Product ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Try to get the product based on the product_id
        try:
            product = ProductDetails.objects.get(id=product_id)
        except ProductDetails.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        
        cart_entry, created = UserCart.objects.get_or_create(
            created_by=request.user.id, 
            product_id=product,
            defaults={"is_active": True}
        )

        if not created:
            cart_entry.is_active = True  
            cart_entry.save()

        # Serialize the cart entry and return it in the response
        cart_serializer = UserCartSerializer(cart_entry)
        return Response(
            {
                "message": "Product added to cart successfully" if created else "Cart entry updated",
                "cart": cart_serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )


    def delete(self, request, product_id=None):
        
        """
        Remove a product from the cart by product_id.
        """
        user = request.user.id

        
        if not product_id:
            product_id = request.data.get('product_id')
            if not product_id:
                return Response({"error": "Product ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            
            cart_entry = UserCart.objects.get(product_id=product_id, created_by=user, is_active=True)
        except UserCart.DoesNotExist:
            
            return Response({"error": "Cart entry not found"}, status=status.HTTP_404_NOT_FOUND)

       
        cart_entry.is_active = False
        cart_entry.save()

        return Response({"message": "Product removed from cart successfully"}, status=status.HTTP_200_OK)