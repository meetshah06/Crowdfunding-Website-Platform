from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django.template import loader
from project.models import Post

# Create your views here.

class PostListView(ListView):
    model=Post
    template_name='project/home.html'
    context_object_name='posts'
    ordering=['-date_posted']
'''
def search_list(request):
if 'q' in request.GET and request.GET['q']:
    q = request.GET['q']
    posts = Post.objects.filter(title__icontains=q)
    return render(request, 'search_results.html', {'posts': posts, 'query': q})
else:
    return render(request, 'search_results.html', {'posts': posts, 'query': q})'''

class UserPostListView(ListView):
    model = Post
    template_name = 'project/my_projects.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
	model=Post
	fields=['title','img','content','goal','current']
	template_name='project/post_detail.html'

class PostCreateView(LoginRequiredMixin,CreateView):
	model=Post
	##template_name='project/post_create.html'
	fields= ['title','content','img','goal']
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model=Post
	fields=['title','content','img']

	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)

	def test_func(self):
		post=self.get_object()
		if self.request.user==post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model =Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class MyPostListView(ListView):
    model=Post
    template_name='project/my_projects.html'
    context_object_name='posts'
    ordering=['-date_posted']

	
		
def donate(request):
	name = request.POST.get('name','')
	amount = request.POST.get('amount',0)
	a = Post.objects.filter(id=22).first()
	a.current = a.current + int(amount) 
	a.save() 
	template = loader.get_template('project/donate.html')
	return HttpResponse(template.render({},request))