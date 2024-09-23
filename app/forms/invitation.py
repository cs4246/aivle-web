from app.models import Invitation
from django import forms
from app.forms.utils import SubmitHelperFormMixin, DisabledFieldsFormMixin


class InvitationCreateForm(SubmitHelperFormMixin, forms.ModelForm):
    class Meta:
        model = Invitation
        fields = ('key', 'group', 'valid')


class InvitationUpdateForm(DisabledFieldsFormMixin, InvitationCreateForm):
    disabled_fields = ['key', 'group']
