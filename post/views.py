from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
from django.template.response import TemplateResponse
from .models import Post

# Create your views here.

#def index(request):
    #print(request)
    #print(request.scheme)
    #print(request.path)
    #print(request.encoding)
   # return HttpResponse('<h1>Hello World!</h1>')

#def index_2(request):
   # return HttpResponse('<h1>Hello World! index_2</h1>')

#def about(request):
    #print('http://127.0.0.1:8000'+request.get_full_path())
   # return HttpResponse('<a href="#"> About page! </a>')

#def contacts(request):
   # print(request.path)
    #return HttpResponse('<h2> Contacts page </h2>')

#def ggg(request):
   # return HttpResponse('<h2> GGG page </h2>')

#def archive(request):
   # return HttpResponse('Archive page')

#def archive_2(request):
   # return HttpResponse('Archive page 2')

#def group(request):
   # group_number = request.path
   # return HttpResponse('group #{group_number}')

#def home_1(request):
   # header = 
   # return HttpResponse(page_content)

def posts(request):
    posts = Post.objects.all()
    data = {
        'title': 'All posts',
        'message': 'hello guys',
        'posts': posts,
    }
    return render(request, 'posts.html', context=data)

def post_detail(request, post_id):
    return HttpResponse(f'detail: {post_id}')

def post_archive(request, year):
    if int(year) > 2024 or int(year) < 1995:
        raise Http404
    return HttpResponse(f'archive for: {year}')

def get_post_handler(request):
    if request.POST:
        return HttpResponse('POST request')
    return HttpResponse('GET request')

def template_test(request):
    return TemplateResponse(request, 'template_test.html')

def get_post_by_id(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    data = {
        'id': post.id,
        'title': post.title_name,
        'content': post.content,
    }
    return JsonResponse(data)

def delete_post(request,post_id=None):
    post_to_delete=Post.objects.get(id=post_id)
    post_to_delete.delete()
    return HttpResponseRedirect(<h1> ALL posts deleted </h1>)
        
def error_404(request, exception):
    return HttpResponseNotFound('''
        <h3> Page not found :^(</h3>
        <img class='fit-picture' 
                                src="https://w.forfun.com/fetch/91/91ab23cdc35b6b44d15f1f5ebeb1cfdf.jpeg" 
                                alt='Imagination' />
    ''')

def page_404(request, exception):
    return HttpResponseNotFound('<h3>Page not found :^</h3>')

#def error_404(request, exception):
   #context = {}
   #return render(request,'admin/404.html', context)