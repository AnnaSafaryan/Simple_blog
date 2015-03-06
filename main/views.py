from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from main.models import Post, Comment
from django.contrib.auth import authenticate, login, logout
# Create your views here.


class Posts(View):
    def get(self, request):
        posts = Post.objects.filter(publish=True).order_by('-when')
        return HttpResponse(render(request, 'posts.html', {'posts': posts}))


class Login(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('No such login/password')


class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


class AddPost(View):
    def get(self, request):
        if request.user.is_authenticated():
            return HttpResponse(render(request, 'edit_post.html', {}))
        else:
            return HttpResponseRedirect('/')

    def post(self, request):
        header = request.POST['header']
        content = request.POST['content']
        publish = 'publish' in request.POST
        Post.objects.create(header=header, text=content, publish=publish)
        return HttpResponseRedirect('/')


class SinglePost(View):
    def get(self, request, id):
        post = Post.objects.get(id=id)
        comments = Comment.objects.all().filter(post=post).order_by('when')
        return HttpResponse(render(request, 'single_post.html', {'post': post, 'comments': comments}))


class EditPost(View):
    def get(self, request, id):
        post = Post.objects.get(id=id)
        return HttpResponse(render(request, 'edit_post.html', {'post': post}))

    def post(self, request, id):
        post = Post.objects.get(id=id)
        header = request.POST['header']
        content = request.POST['content']
        publish = 'publish' in request.POST
        post.header = header
        post.text = content
        post.publish = publish
        post.save()
        return HttpResponseRedirect('/posts/{}/'.format(id))


class AddComment(View):
    def post(self, request, id):
        post = Post.objects.get(id=id)
        header = request.POST['header']
        text = request.POST['text']
        user = request.user
        Comment.objects.create(post=post, header=header, text=text, who=user)
        return HttpResponseRedirect('/posts/{}/'.format(id))