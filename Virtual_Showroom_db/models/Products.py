from django.db import models
from django.conf import settings  # Import settings to reference AUTH_USER_MODEL

class ProductDetails(models.Model):
    product_code = models.CharField(max_length=50, verbose_name="Product_Code", blank=True, null=True)
    style_no = models.CharField(max_length=50, verbose_name="Style_No", blank=True, null=True)
    product_type = models.CharField(max_length=100, verbose_name="Product_Type", blank=True, null=True)
    designer_head = models.CharField(max_length=100, verbose_name="Designer_Head", blank=True, null=True)
    entered_by = models.CharField(max_length=100, verbose_name="Entered_By", blank=True, null=True)
    category = models.CharField(max_length=100, verbose_name="Category", blank=True, null=True)
    season = models.CharField(max_length=50, verbose_name="Season", blank=True, null=True)
    fabric = models.CharField(max_length=100, verbose_name="Fabric", blank=True, null=True)
    value_driver = models.CharField(max_length=100, verbose_name="Value_Driver", blank=True, null=True)
    sustainable = models.BooleanField(verbose_name="Sustainable", default=False, blank=True, null=True)
    designer_status = models.CharField(max_length=50, verbose_name="Designer_Status", blank=True, null=True)
    dmm_status = models.CharField(max_length=50, verbose_name="DMM_Status", blank=True, null=True)
    remarks = models.TextField(blank=True, null=True, verbose_name="Remarks")
    comment = models.TextField(blank=True, null=True, verbose_name="Comment")
    is_active = models.BooleanField(default=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    main_image = models.ImageField(upload_to='main_image/', blank=True, null=True)
    inspiration_image = models.ImageField(upload_to='inspiration_image/', blank=True, null=True)
    front_image = models.ImageField(upload_to='front_image/', blank=True, null=True)
    details_image = models.ImageField(upload_to='details_image/', blank=True, null=True)
    back_image = models.ImageField(upload_to='back_image/', blank=True, null=True)
    sleeve_image = models.ImageField(upload_to='sleeve_image/', blank=True, null=True)
    fabric_image = models.ImageField(upload_to='fabric_image/', blank=True, null=True)



class UserCart(models.Model):
    product_id = models.ForeignKey(ProductDetails, on_delete=models.DO_NOTHING, related_name="cart_products", blank=True, null=True)
    is_active = models.IntegerField(default=1, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)

    
