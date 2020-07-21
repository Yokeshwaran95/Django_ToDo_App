from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest
from .models import Todo
from django.contrib.auth.forms import UserCreationForm
from todos.forms import CreateUserForm ,AddTodos
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

# Create your views here.

def registration_site(request):
	if request.user.is_authenticated:
		return redirect('/todos/list/')
	else:
		form=UserCreationForm()
		if request.method == 'POST':
			form=CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user=form.cleaned_data.get('username')
				messages.success(request,"Account was created for "+user)
				return redirect('login')
		context={'form':form}
		return render(request, 'todos/registration.html',context)

def login_site(request):
	if request.user.is_authenticated:
		return redirect('/todos/list/')
	else:
		if request.method == 'POST':
			username=request.POST.get('username')
			password=request.POST.get('password')
			user=authenticate(request,username=username,password=password)

			if user is not None:
				login(request,user)
				return redirect('/todos/list/')
			else:
				messages.info(request, 'Username or password is incorrect')
				context={}
				return render(request, 'todos/login.html',context)

		context={}
		return render(request, 'todos/login.html',context)

def logoutUser(request):
	logout(request)
	return redirect('login')

# @login_required(login_url='login')
# def list_todo_item(request):
# 	context={'todo_list':Todo.objects.all()}
# 	return render(request,"todos/todo_list.html", context)

class ListTodoItem(LoginRequiredMixin,ListView):
	template_name="todos/todo_list.html"
	login_url="/login/"
	def get_queryset(self):
		return Todo.objects.filter(user=self.request.user)

# @login_required(login_url='login')
# def insert_todo_item(request:HttpRequest):
# 	todo=Todo(content=request.POST['content'])
# 	todo.save()
# 	return redirect('/todos/list/')

class InsertTodoItem(LoginRequiredMixin,CreateView):
	# form_class=RLCreateForm
	# template_name="form.html"
	success_url="/todos/list/"
	login_url="/login/"
	form_class=AddTodos
	def form_valid(self,form):
		instance=form.save(commit=False)
		instance.user=self.request.user
		return super(InsertTodoItem, self).form_valid(form)
	def get_queryset(self):
		return Todo.objects.filter(user=self.request.user)

	# def get_context_data(self,*args,**kwargs):
	# 	context=super(InsertTodoItem,self).get_context_data(*args,**kwargs)
	# 	# context["title"]='Add Restaurant'
	# 	return context

@login_required(login_url='login')
def delete_todo_item(request,todo_id):
	todo_to_delete=Todo.objects.get(id=todo_id)
	todo_to_delete.delete()
	return redirect('/todos/list/')

