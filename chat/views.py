from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .serializers import GroupSerializer
from .models import Group

from rest_framework import generics



def home(request):
	groups = Group.objects.all()
	return render(request, 'home.html', {'groups':groups})


@login_required
def new_group(request):
	chatname = request.POST['chatname']		
	u = request.user
	if request.method == 'POST':
		new = Group.objects.create(chatname=chatname)
		new.members.add(u)
		new.save()
		return redirect('home')
	else:
		messages.error(request, 'Here is error.')
		return render(request, 'home.html')


@login_required
def join_group(request, uuid):
	u = request.user
	gp = Group.objects.get(uuid=uuid)
	gp.members.add(u)
	gp.save()
	return redirect('home')


@login_required
def leave_group(request, uuid):
	u = request.user
	gp = Group.objects.get(uuid=uuid)
	gp.members.remove(u)
	gp.save()
	return redirect('home')


@login_required
def open_chat(request, uuid):
	group = Group.objects.get(uuid=uuid)
	if request.user not in group.members.all():
		return HttpResponseForbidden('Not a member. Try another group.')
	messages = group.message_set.all()
	sorted_messages = sorted(messages, key=lambda x: x.timestamp)
	return render(request, 'chat.html', context={'messages':sorted_messages, 'uuid': uuid})


@login_required
def remove_group(request, uuid):
	u = request.user
	Group.objects.get(uuid=uuid).delete()
	return redirect('home')


class GroupAPIList(generics.ListAPIView):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer
	

class GroupCreateAPIView(generics.ListCreateAPIView):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer


class GroupAPIDetailVeiw(generics.RetrieveUpdateDestroyAPIView):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer

