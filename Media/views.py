from django.http import Http404, HttpRequest
from django.shortcuts import render, get_object_or_404
import datetime as dt
from Media.models import Image
import pyperclip
from PIL import ImageGrab

# Create your views here.
def index(request):
    display = Image.display_images()
    return render(request,'index.html', {"display": display[:]}) # [:] the whole array
    
    
def search_results(request):
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        searched_image = Image.search_image(search_term) 
        message = f'{search_term}'
        
        return render(request, 'post/search.html', {'message': message, 'images': searched_image})
    else:
        message = "You have not searched for any image name"
        print(search_term)
    return render(request, 'post/search.html', {'message': message})

def show_single_image(request, image_id):
    display = get_object_or_404(Image, pk = image_id)
    # display = Image.get_image_by_id(id = image_id)
    return render (request, 'post/show_post.html', {"display": display})

# def post_location(request, location):
#     show_location = Image.filter_by_location(location = location)
#     print('he')
#     return render (request, 'post/location.html', {'location': location[location]})

def post_location(request, location_id):
    try:
        location = Image.objects.get(id = location_id)
    except Image.DoesNotExist:
        raise Http404()
    return render(request, 'post/location.html', {"location": location})

# def copy(request, method = ['GET']):
#     copy_image = ImageGrab.grabclipboard()
#     copy_image.save('clipboard.jpg', 'JPG')
#     return HttpRequest (request, copy_image)