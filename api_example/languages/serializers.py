from rest_framework import serializers

from .models import Language
from .models import *
from .models import PostFile
import random

from .analyse import main





class LanguageSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
          
          a =random.randint(1,101)
          return a
       

    class Meta:
            model = Language
            fields = ('id','name','paradigm')
        
    
class CM_OS_S(serializers.ModelSerializer):
    
    CM_OS = serializers.SerializerMethodField()
        
    def get_CM_OS(self, obj):
        data = []
        data=main()
        CM_OS1 = data["CM_OS"]
        return CM_OS1

    class Meta:
            model = CM_OS_MODEL
            fields = "__all__" 

class CLIENTS_OS_S(serializers.ModelSerializer):
    CLIENTS_OS = serializers.SerializerMethodField()
        
    def get_CLIENTS_OS(self, obj):
        data = []
        data=main()
        CLIENTS_OS1 = data["CLIENTS_OS"]
        return CLIENTS_OS1

    class Meta:
            model = CLIENTS_OS_MODEL
            fields = "__all__"

class CM_VERSION_S(serializers.ModelSerializer):
    CM_VERSION = serializers.SerializerMethodField()
        
    def get_CM_VERSION(self, obj):
        data = []
        data=main()
        CM_VERSION1 = data["CM_VER"]
        return CM_VERSION1

    class Meta:
            model = CM_VERSION_MODEL
            fields = "__all__"    

class CLIENT_VERSION_S(serializers.ModelSerializer):
    CLIENT_VERSION = serializers.SerializerMethodField()
        
    def get_CLIENT_VERSION(self, obj):
        data = []
        data=main()
        CLIENT_VERSION1 = data["CLIENTS_VER"]
        return CLIENT_VERSION1

    class Meta:
            model = CLIENT_VERSION_MODEL
            fields = "__all__"

class MEDIA_INFO_S(serializers.ModelSerializer):
    MEDIA_INFO = serializers.SerializerMethodField()
        
    def get_MEDIA_INFO(self, obj):
        data = []
        data=main()
        MEDIA_INFO1 = data["MEDIA_INFO"]
        return MEDIA_INFO1

    class Meta:
            model = MEDIA_INFO_MODEL
            fields = "__all__"  

class BACKUP_INFO_S(serializers.ModelSerializer):
    BACKUP_INFO = serializers.SerializerMethodField()
        
    def get_BACKUP_INFO(self, obj):
        data = []
        data=main()
        BACKUP_INFO1 = data["BACKUP_INFO"]
        return BACKUP_INFO1

    class Meta:
            model = BACKUP_INFO_MODEL
            fields = "__all__" 

class LIC_INFO_S(serializers.ModelSerializer):
    LIC_INFO = serializers.SerializerMethodField()
        
    def get_LIC_INFO(self, obj):
        data = []
        data=main()
        LIC_INFO1 = data["LIC_INFO"]
        return LIC_INFO1

    class Meta:
            model = LIC_INFO_MODEL
            fields = "__all__"        
                    

class TOTAL_S(serializers.ModelSerializer):
    
    CM_TOTAL = serializers.SerializerMethodField()
    CLIENTS_TOTAL = serializers.SerializerMethodField()
        
    def get_CM_TOTAL(self, obj):
        data = []
        data=main()
        CM_TOTAL1 = data["CLIENTS_TOTAL"]
        return CM_TOTAL1

    def get_CLIENTS_TOTAL(self, obj):
        data = []
        data=main()
        CLIENT_TOTAL1 = data["CLIENTS_TOTAL"]
        return CLIENT_TOTAL1    

    class Meta:
            model = TOTAL_MODEL
            fields = ('CM_TOTAL', 'CLIENTS_TOTAL')                                
        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
            model = PostFile
            fields = "__all__"         


