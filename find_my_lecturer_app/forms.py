# find_my_lecturer_app/forms.py

from django import forms
from .models import Lecturer

class LecturerUpdateForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = ['full_name', 'office', 'notes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            widget = field.widget
            if not isinstance(widget, forms.CheckboxInput):
                widget.attrs.update({'class': 'form-control'})
