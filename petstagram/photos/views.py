from django.shortcuts import render, redirect

from petstagram.photos.forms import PhotoCreateForm
from petstagram.photos.models import Photo


def add_photo(request):
    if request.method == "GET":
        form = PhotoCreateForm()
    else:

        form = PhotoCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'photos/photo-add-page.html', context)


def details_photo(request, pk):
    return render(request, 'photos/photo-details-page.html')


def edit_photo(request, pk):
    return render(request, 'photos/photo-edit-page.html')


def delete_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo.delete()
    return redirect('home')
