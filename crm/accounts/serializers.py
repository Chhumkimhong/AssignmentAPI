from rest_framework import serializers

from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:        
        model = tblProducts
        fields = ['id', 'ProductName', 'PriceOut','ProductImage','ProductDate']
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:        
        model = Category
        fields = ['id', 'Categoryname', 'CategoryImage','CategoryDate']

class BestSellerSerializer(serializers.ModelSerializer):
    class Meta:        
        model = BestSeller
        fields = ['id', 'BestSellerName', 'CategoryID','SupplierID','SupplierID','PriceOut','BestSellerImage','BestSellerDate','BestSellerDescription']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:        
        model = Customer
        fields = ['id', 'Name', 'Phone','Email','Date_created']

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:        
        model = Supplier
        fields = ['id', 'Companyname', 'Contactname','ContactTitle','Phone','Email','Date_created']

class ClientsSerializer(serializers.ModelSerializer):
    class Meta:        
        model = tblClients
        fields = ['id', 'ClientName', 'ClientDescription','ClientPosition','ClientImage']

class FreshOrganicsSerializer(serializers.ModelSerializer):
    class Meta:        
        model = tblFreshOrganic
        fields = ['id', 'OrganicName', 'CategoryID','SupplierID','Quantity','Instock','OrganicTitle','PriceOut','OrganicImage','OrganiclDate','OrganiclDescription']
 
class SildesSerializer(serializers.ModelSerializer):
    class Meta:        
        model = tblSlides
        fields = ['id', 'SlideName', 'SlideImage','SlideDescription','Active']

class SubTopMenuSerializer(serializers.ModelSerializer):
    class Meta:        
        model = tblSubTopMenu
        fields = ['id', 'SubTopMenuName', 'SubTopMenuImage','TopMenuID']

class TopMenuSerializer(serializers.ModelSerializer):
    class Meta:        
        model = tblTopMenu
        fields = ['id', 'TopMenuName', 'TopMenuImage']