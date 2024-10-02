from django import forms

from .models import Membership


class MembershipForm(forms.ModelForm):

    class Meta:
        model = Membership
        exclude = ('payment_reference', 'paid_at',
                   'payment_updated_by')

