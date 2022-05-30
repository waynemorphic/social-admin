import datetime as dt
from django.db import models

# Create your models here.

# user class
class User (models.Model):
    '''
    user model
    Args
        first_name, last_name, email
    '''
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    email = models.EmailField()
    
    def __str__(self):
        return self.first_name
    
    def save_user(self):
        self.save()

class Meta:
    ordering = ['first_name']


# location class
class Location (models.Model):
    '''
    location image was taken
    Args:
        image_location
    '''
    location = models.CharField(max_length= 30, blank = True)
    # user = models.ForeignKey(User, on_delete = models.CASCADE)
    # category = models.ForeignKey(Category, on_delete = models.CASCADE)
    # image_location = models.ManyToManyField(User, through="Image", through_fields=('image_location', 'user'))
    
    def __str__(self):
        return self.location
    
    def save_location(self):
        self.save()

# category class  
class Category (models.Model):
    '''
    image category
    Args:
        image_category
    '''
    category = models.CharField(max_length=20, blank = True)
    # user = models.ForeignKey(User, on_delete = models.CASCADE)
    # location = models.ForeignKey(Location, on_delete = models.CASCADE)
    # image_category = models.ManyToManyField(User, through = 'Image', through_fields=('image_category', 'user'))
  
    def __str__(self):
        return self.category
    
    def save_category(self):
        self.save()
  
# image model class 
class Image (models.Model):
    '''
    image model
    Args:
        image, image_name, image_description, image_location, image_category, user, post_date
    '''

    image = models.ImageField(upload_to = 'static/images', default = '')
    image_name = models.CharField(max_length = 50)
    image_description = models.TextField()
    image_location = models.ForeignKey(Location, null = True, on_delete = models.CASCADE)
    image_category = models.ForeignKey(Category, null = True, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post_date = models.DateTimeField(auto_now = True)
    
    
    def save_image(self):
        self.save()
        
    def delete_image(self, id):
        self.objects.filter(id = id).delete()
        
    def update_image(self, id):
        self.objects.filter(id = id).update(id)
        
    def get_image_by_id(self, id):
        self.objects.get(id = id)
    
    @classmethod
    def search_image(cls, search_name):
        image_find = cls.objects.filter(image_name__icontains = search_name)
        
        return image_find
        
    @classmethod   
    def filter_by_location(cls, location):
        find_location = cls.objects.filter(location__image_location__contains = location).all()
        return find_location        
    
    @classmethod
    def display_images(cls):
        return cls.objects.all()
    
        # today = dt.date.today()
        # display = cls.objects.filter(post_date__date = today)
        # return display
    
class Meta:
    ordering = ['image_name']

    