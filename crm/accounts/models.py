from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    Name = models.CharField(max_length=200,null=True)
    Phone = models.CharField(max_length=200,null=True)
    Email = models.CharField(max_length=200,null=True)
    Date_created = models.DateTimeField(auto_now_add=True,null=True)

    
    def __str__(self):
        return self.Name

class Category(models.Model):
    Categoryname=models.CharField(max_length=200,null=True)
    # CategoryImage=models.CharField(max_length=200,null=True)
    # CategoryImage = models.ImageField(upload_to ='CategoryImages/')
    CategoryImage=models.ImageField(upload_to='CategoryImages/')
    CategoryDate=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.Categoryname;

class Supplier(models.Model):
    Companyname=models.CharField(max_length=200,null=True)
    Contactname=models.CharField(max_length=200,null=True)
    ContactTitle=models.CharField(max_length=200,null=True)
    Phone=models.CharField(max_length=200,null=True)
    Email=models.EmailField(max_length=200,null=True)
    Date_created=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.Companyname

class tblProducts(models.Model):
    ProductName=models.CharField(max_length=200,null=True)
    CategoryID=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    SupplierID=models.ForeignKey(Supplier,on_delete=models.CASCADE,null=True)
    Quantity=models.CharField(max_length=200,null=True)
    Instock=models.CharField(max_length=200,null=True)
    ProductTitle=models.CharField(max_length=500,null=True)
    PriceIn=models.CharField(max_length=200,null=True)
    PriceOut=models.CharField(max_length=200,null=True)
    ProductImage=models.ImageField(upload_to='ProductImages/')
    ProductDate=models.DateTimeField(auto_now_add=True,null=True)
    ProductDescription=RichTextField(null=True)
    ReviewerName=models.CharField(max_length=200,null=True)
    ReviewDescription=RichTextField(null=True)
    ReviewDate=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.ProductName;



class ListCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Cart for {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(ListCart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(tblProducts, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * self.product.PriceOut

class tblClients(models.Model):
    ClientName=models.CharField(max_length=200,null=True)
    ClientDescription=RichTextField(null=True)
    ClientPosition=models.CharField(max_length=200,null=True)
    ClientImage=models.ImageField(upload_to="pics")

class tblTopMenu(models.Model):
    TopMenuName=models.CharField(max_length=200,null=True)
    TopMenuImage=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.TopMenuName;

class tblSubTopMenu(models.Model):
    SubTopMenuName=models.CharField(max_length=200,null=True)
    SubTopMenuImage=models.CharField(max_length=200,null=True)
    TopMenuID=models.ForeignKey(tblTopMenu,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.SubTopMenuName

class tblSlides(models.Model):
    SlideName=models.CharField(max_length=200,null=True)
    SlideImage=models.ImageField(upload_to='images/',null=True)
    SlideDescription=RichTextField(null=True)
    CategoryId=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    Active=models.CharField(max_length=200,null=True)

class tblSocialMedia(models.Model):
    SocialMediaName=models.CharField(max_length=200,null=True)
    SocialMediaURL=models.CharField(max_length=200,null=True)
    SocialMediaImage=models.CharField(max_length=200,null=True)

class tblProductDetail(models.Model):
    ProductDetailName = models.CharField(max_length=200, null=True)
    ProductDetailDate = models.DateTimeField (auto_now_add=True, null=True)
    ProductID = models.ForeignKey(tblProducts, on_delete=models.CASCADE, null=True)
    ProductSize =  RichTextUploadingField(null=True)
    ProductColor = RichTextUploadingField(null=True)

class tblProductDetailImage(models.Model):
    ProductDetailImageName = models.CharField(max_length=200, null=True)
    ProductID = models.ForeignKey(tblProducts, on_delete=models.CASCADE, null=True)
    ProductDetailImage = models.ImageField(upload_to='',null=True,blank=True)
    ImageDate = models.DateTimeField(auto_now_add=True, null=True)

class tblReviewer(models.Model):
    ReviewerName=models.CharField(max_length=200,null=True)
    ReviewDescription=RichTextUploadingField(null=True)
    ReviewDate=models.DateTimeField(auto_now_add=True,null=True)

class tblFreshOrganic(models.Model):
    OrganicName=models.CharField(max_length=200,null=True)
    CategoryID=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    SupplierID=models.ForeignKey(Supplier,on_delete=models.CASCADE,null=True)
    Quantity=models.CharField(max_length=200,null=True)
    Instock=models.CharField(max_length=200,null=True)
    OrganicTitle=models.CharField(max_length=500,null=True)
    PriceIn=models.CharField(max_length=200,null=True)
    PriceOut=models.CharField(max_length=200,null=True)
    OrganicImage=models.ImageField(upload_to='ProductImages/')
    OrganiclDate=models.DateTimeField(auto_now_add=True,null=True)
    OrganiclDescription=RichTextField(null=True)

class BestSeller(models.Model):
    BestSellerName=models.CharField(max_length=200,null=True)
    CategoryID=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    SupplierID=models.ForeignKey(Supplier,on_delete=models.CASCADE,null=True)
    Quantity=models.CharField(max_length=200,null=True)
    Instock=models.CharField(max_length=200,null=True)
    BestSellerTitle=models.CharField(max_length=500,null=True)
    PriceIn=models.CharField(max_length=200,null=True)
    PriceOut=models.CharField(max_length=200,null=True)
    BestSellerImage=models.ImageField(upload_to='ProductImages/')
    BestSellerDate=models.DateTimeField(auto_now_add=True,null=True)
    BestSellerDescription=RichTextField(null=True)

    def __str__(self):
        return self.BestSellerName
    


















