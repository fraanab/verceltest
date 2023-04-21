from django.shortcuts import render

from .models import Notes


# Create your views here.
def main(request):
	allnotes = Notes.objects.all()
	return render(request, 'main.html', {'allnotes':allnotes})
