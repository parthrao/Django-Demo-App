from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import File
from django.views.generic.edit import CreateView
from django.views import generic

# Create your views here.
def index(request):
	all_files = File.objects.all()
	# template = loader.get_template('music/index.html')
	context = {
		'all_files': all_files,
	}
	# return HttpResponse(template.render(context, request))
	return render(request, 'uploadfile/index.html', context)

class FileFormCreate(CreateView):
	model = File
	fields = ['name','company','file_type','file_url', 'file_title']