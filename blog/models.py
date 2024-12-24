from django.db import models
from django.conf import settings
from django.db import models
from PIL import Image



class Photo(models.Model):
    image = models.ImageField()
    caption = models.CharField(max_length=128, blank=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    IMAGE_MAX_SIZE = (800, 800)
    
    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        # sauvegarde de l’image redimensionnée dans le système de fichiers
        # ce n’est pas la méthode save() du modèle !
        image.save(self.image.path)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()

class Blog(models.Model):
    picture = models.ImageField(upload_to='blog_pictures/', null=True, blank=True)
    title = models.CharField(max_length=128)
    lead = models.CharField(max_length=5000)
    content = models.CharField(max_length=5000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    IMAGE_MAX_SIZE = (800, 800)
    
    def resize_picture(self):
        picture = Image.open(self.picture)
        picture.thumbnail(self.IMAGE_MAX_SIZE)
        # sauvegarde de l’image redimensionnée dans le système de fichiers
        # ce n’est pas la méthode save() du modèle !
        picture.save(self.picture.path)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) 
        self.resize_picture() 


    
