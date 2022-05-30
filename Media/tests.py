from unicodedata import category
from django.test import TestCase
from Media.models import User, Category, Location, Image

# Create your tests here.
class UserTestClass(TestCase):
    
    def setUp(self):
        self.doe = User(first_name = 'John', last_name = 'Doe', email = 'jd@gmail.com')
    
    def test_instance(self):
        self.assertTrue(self.doe, User)
        
    def test_save_user(self):
        self.doe.save_user()
        users = User.objects.all()
        self.assertTrue(len(users) > 0)
    
class CategoryTestClass(TestCase):
    
    def setUp(self):
        self.travel = Category(category = 'Travel')
        
    def test_instance(self):
        self.assertTrue(self.travel, Category)
        
    def test_save_category(self):
        self.travel.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0 )
    
class LocationTestClass(TestCase):
    
    def setUp(self):
        self.nairobi = Location(location = 'Nairobi')
        
    def test_instance(self):
        self.assertTrue(self.nairobi, Location)
        
    def test_save_location(self):
        self.nairobi.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0 )

class ImageTestClass(TestCase):
    
    def setUp(self):
        self.doe = User(first_name = 'John', last_name = 'Doe', email = 'jd@gmail.com')
        self.doe.save_user()
        
        self.new_location = Location(location = 'Nairobi')
        self.new_location.save()
        
        self.new_category = Category(category = 'Travel')
        self.new_category.save()
        
        self.new_image = Image(image = 'pic', image_name = 'pic pic', image_description = 'img desc', image_location = self.new_location, image_category = self.new_category, user = self.doe)
        self.new_image.save()
        
        # self.new_location.location.add(self.new_category)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_location, Location))
        self.assertTrue(isinstance(self.new_category, Category))
    
    def test_save_image(self) :
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
        
    def tearDown(self):
        User.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()