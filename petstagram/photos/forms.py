from django import forms

from petstagram.common.models import PhotoLike
from petstagram.core.form_mixin import DisabledFormMixin
from petstagram.photos.models import Photo


class PhotoCreateForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'


class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['photo']

class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('publication_date',)


class PhotoDeleteForm(DisabledFormMixin, PhotoBaseForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            self.instance.tagged_pets.clear()  # many-to-many

            Photo.objects.all() \
                .first().tagged_pets.clear()
            PhotoLike.objects.filter(photo_id=self.instance.id) \
                .delete()  # one-to-many
            PhotoComment.objects.filter(photo_id=self.instance.id) \
                .delete()  # one-to-many
            self.instance.delete()

        return self.instance