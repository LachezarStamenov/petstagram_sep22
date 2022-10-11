import pyperclip
from django.shortcuts import render, redirect
from django.urls import reverse
from pyperclip import copy

from petstagram.common.models import PhotoLike
from petstagram.common.utils import get_user_liked_photo, get_photo_url
from petstagram.core.photo_utils import apply_likes_count, apply_user_liked_photo
from petstagram.photos.models import Photo





def index(request):
    photos = [apply_likes_count(photo) for photo in Photo.objects.all()]
    photos = [apply_user_liked_photo(photo) for photo in photos]
    context = {
        'photos': photos,
    }

    return render(request, 'common/home-page.html', context)



def like_photo(request, photo_id):

    user_liked_photos = get_user_liked_photo(photo_id)
    if user_liked_photos:
        user_liked_photos.delete()
    else:
        PhotoLike.objects.create(photo_id=photo_id, )
    return redirect(get_photo_url(request, photo_id))
    # photo_like = PhotoLike(
    #     photo_id=photo_id,
    # )
    # photo_like.save()\

def share_photo(request, photo_id):
    photo_details_url = reverse('detail photo', kwargs={'pk': photo_id})
    pyperclip.copy(photo_details_url)
    return redirect(get_photo_url(request, photo_id))

