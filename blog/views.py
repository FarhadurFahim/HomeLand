from django.utils import timezone
from blog.models import Post, UserProfile
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
#from .forms import PostForm
from blog.forms import UserForm, UserProfileForm, PostForm
from django.contrib.auth import authenticate ,login, logout, get_user_model
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib.auth.models import User
from django.views.generic import DetailView, UpdateView 
from django.contrib import messages 


def home_land(request):
    #posts = Post.objects.filter()
    return render(request, 'blog/home_land.html', {})




def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})




# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.filter()
    return render(request, 'blog/post_list.html', {'posts':posts})




@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        #   author2 = request.user
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    images=Post.objects.all()
    return render(request, 'blog/post_edit.html', {'form': form, 'images':images})




@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid() and request.user == post.author:
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    images=Post.objects.all()
    return render(request, 'blog/post_edit.html', {'form': form, 'images':images})




@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog.views.post_list')





def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True

        else:
            user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'blog/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})





def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                return HttpResponseRedirect('/')

            else:
                return HttpResponseRedirect('Your account is disabled')

        else:
            form_invalid_message = "Username or password invalid"
            #print "Invalid login details: {0}, {1}".format(username, password)
            #return HttpResponse("Incorrect username or password.")
            #messages.error(request, "Error")


    return render(request, 'blog/login.html', {})




@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')



class UserProfileDetail(DetailView):
    model = UserProfile
    #model = get_user_model()
    #context_object_name = 'user_object'


class UserProfileUpdate(UpdateView):
    model = UserProfile
    fields = ('name', 'contactNo', 'address', 'bio')
    template_name_suffix = '_update'
