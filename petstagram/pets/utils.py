from petstagram.common.models import PhotoLike
from petstagram.pets.models import Pet


def get_pet_by_name_and_username(pet_slug, username):
    # TODO: fix username with auth
    return Pet.objects.get(slug=pet_slug)


def get_user_liked_photos(photo_id):
    return PhotoLike.objects.filter(photo_id=photo_id)