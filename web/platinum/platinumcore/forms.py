from crispy_forms.bootstrap import StrictButton, FormActions
from crispy_forms.layout import Submit, Layout, Fieldset, Field
from django.forms import ModelForm, Form
from crispy_forms.helper import FormHelper
from models import Player, Team, Club


class ClubForm(ModelForm):
    class Meta:
        model = Club
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(ClubForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Field('name'),
            FormActions(
                Submit('save', 'Save')
            ),
        )


class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(TeamForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Field('name'),
            FormActions(
                Submit('save', 'Save')
            ),
        )


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'position', 'team']

    def __init__(self, *args, **kwargs):
        super(PlayerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-7'
        self.helper.layout = Layout(
            Field('first_name'),
            Field('last_name'),
            Field('position'),
            Field('team'),
            FormActions(
                Submit('save', 'Save')
            ),
        )


