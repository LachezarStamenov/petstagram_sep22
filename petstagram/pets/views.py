from django.shortcuts import render, redirect

from petstagram.core.photo_utils import apply_likes_count, apply_user_liked_photo
from petstagram.pets.forms import PetForm, PetDeleteForm
from petstagram.pets.models import Pet
from petstagram.pets.utils import get_pet_by_name_and_username


def add_pet(request):
    form = PetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('details user', pk=1)
    context = {'form': form}
    return render(request, 'pets/pet-add-page.html', context)


def delete_pet(request, username, pet_slug):
    pet = get_pet_by_name_and_username(pet_slug, username)
    if request.method == "POST":
        pet.delete()
        return redirect('details user', pk=1)
    form = PetDeleteForm(initial=pet.__dict__)
    context = {'form': form}
    return render(request, 'pets/pet-delete-page.html', context)


def details_pet(request, username, pet_slug):
    pet = get_pet_by_name_and_username(pet_slug, username)
    photos = [apply_likes_count(photo) for photo in pet.photo_set.all()]
    photos = [apply_user_liked_photo(photo) for photo in photos]

    context = {
        'pet': pet,
        'photos_count': pet.photo_set.count(),
        'pet_photos': photos,
    }
    return render(request, 'pets/pet-details-page.html', context)


def edit_pet(request, username, pet_slug):
    pet = get_pet_by_name_and_username(pet_slug, username)
    if request.method == "GET":
        form = PetForm(instance=pet, initial=pet.__dict__)
    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('details pet', username, pet_slug)
    context = {'form': form}
    return render(request, 'pets/pet-edit-page.html', context)

