from django.forms import ModelForm, HiddenInput

from .models import App, Attach, Domain, NetAddr, Poc, Port, Proj, Sys, Vuln, WebApp, WebPage

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, HTML, Layout, Field, Submit


class AppForm(ModelForm):

    class Meta:
        model = App
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div(
                    'name',
                    'version',
                    css_class='col-sm-6'
                ),
                Div(Field('comments', style='height: 124px;'), css_class='col-sm-6'),
                Field('sys', type='hidden'),
                css_class='row',
            ),
                Submit('save', 'Submit', css_class='btn-success'),
                HTML('<a name="cancel" class="btn btn-danger" id="button-id-cancel" href="{{ view.get_success_url }}">Cancel</a>'), 
        )


class AttachForm(ModelForm):

    class Meta:
        model = Attach
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.include_media = False
        self.helper.layout = Layout(
            Div(
                Div(
                    'media',
                    'name',
                    'caption',
                    css_class='col-sm-6'
                ),
                Field('vuln', type='hidden'),
                Field('webpage', type='hidden'),
                css_class='row',
            ),
                Submit('save', 'Submit', css_class='btn-success'),
                HTML('<a name="cancel" class="btn btn-danger" id="button-id-cancel" href="{{ view.get_success_url }}">Cancel</a>'), 
        )


class DomainForm(ModelForm):

    class Meta:
        model = Domain
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div('domain', css_class='col-sm-6'),
                Field('proj', type='hidden'),
                css_class='row',
            ),
                Submit('save', 'Submit', css_class='btn-success'),
                HTML('<a name="cancel" class="btn btn-danger" id="button-id-cancel" href="{{ view.get_success_url }}">Cancel</a>'), 
        )


class NetAddrForm(ModelForm):

    class Meta:
        model = NetAddr
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div('net_address', css_class='col-sm-6'),
                Field('proj', type='hidden'),
                css_class='row',
            ),
                Submit('save', 'Submit', css_class='btn-success'),
                HTML('<a name="cancel" class="btn btn-danger" id="button-id-cancel" href="{{ view.get_success_url }}">Cancel</a>'), 
        )


class PocForm(ModelForm):

    class Meta:
        model = Poc
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div('name', 'role', Div(
                        Div(Field('email', placeholder='user@domain.com'), css_class='col-sm-6'),
                        Div(Field('phone', placeholder='+1 111 111 1111'), css_class='col-sm-6'),
                        css_class='row'), 
                    css_class='col-sm-6'),
                Div(Field('comments', style='height: 210px;'), css_class='col-sm-6'),
                Field('proj', type='hidden'),
                css_class='row',
            ),
                Submit('save', 'Submit', css_class='btn-success'),
                HTML('<a name="cancel" class="btn btn-danger" id="button-id-cancel" href="{{ view.get_success_url }}">Cancel</a>'), 
        )


class PortForm(ModelForm):
    
    class Meta:
        model = Port
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div(
                    Div(
                        Div('protocol', css_class='col-sm-6'),
                        Div('number', css_class='col-sm-6'),
                        css_class='row'
                    ),
                    Div(
                        Div('service_name', css_class='col-sm-6'),
                        Div('version', css_class='col-sm-6'),
                        css_class='row'
                    ),
                    'is_web_app',
                    css_class='col-sm-6'
                ),
                Div(Field('comments', style='height: 175px;'), css_class='col-sm-6'),
                Field('sys', type='hidden'),
                css_class='row',
            ),
                Submit('save', 'Submit', css_class='btn-success'),
                HTML('<a name="cancel" class="btn btn-danger" id="button-id-cancel" href="{{ view.get_success_url }}">Cancel</a>'), 
        )


class ProjForm(ModelForm):

    class Meta:
        model = Proj
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div('name', 'org_name', Div(
                        Div(Field('init_date', placeholder='yyyy-mm-dd'), css_class='col-sm-6'),
                        Div(Field('end_date', placeholder='yyyy-mm-dd'), css_class='col-sm-6'),
                        css_class='row'), 
                    css_class='col-sm-6'),
                Div(Field('comments', style='height: 210px;'), css_class='col-sm-6'),
                css_class='row',
            ),
                Submit('save', 'Submit', css_class='btn-success'),
                HTML('<a name="cancel" class="btn btn-danger" id="button-id-cancel" href="{{ view.get_success_url }}">Cancel</a>'), 
        )


class SysForm(ModelForm):

    class Meta:
        model = Sys
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div('ip_address', 'fqdn', Div(
                        Div('os', css_class='col-sm-6'),
                        Div('version', css_class='col-sm-6'),
                        css_class='row'), 
                    css_class='col-sm-6'),
                Div(Field('comments', style='height: 210px;'), css_class='col-sm-6'),
                Field('proj', type='hidden'),
                css_class='row',
            ),
                Submit('save', 'Submit', css_class='btn-success'),
                HTML('<a name="cancel" class="btn btn-danger" id="button-id-cancel" href="{{ view.get_success_url }}">Cancel</a>'), 
        )


class VulnForm(ModelForm):
    
    class Meta:
        model = Vuln
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div('title', css_class='col-sm-6'),
                Div('cve', css_class='col-sm-2'),
                Div('score', css_class='col-sm-2'),
                Div('risk', css_class='col-sm-2'),
                css_class='row'
            ),
            Div(
                Div(Field('description', style='height: 210px;'), css_class='col-sm-6'),
                Div(Field('evidence', style='height: 210px;'), css_class='col-sm-6'), 
                css_class='row'
            ),
            Div(
                Div(Field('solution', style='height: 210px;'), css_class='col-sm-6'),
                Div(Field('comments', style='height: 210px;'), css_class='col-sm-6'), 
                css_class='row'
            ),
            Div(
            Field('sys', type='hidden'),
            Field('app', type='hidden'),
            Field('port', type='hidden'),
            Field('webapp', type='hidden'),
            Field('webpage', type='hidden'),
            Field('proj', type='hidden'),
            css_class='row'
            ),
            Submit('save', 'Submit', css_class='btn-success'),
            HTML('<a name="cancel" class="btn btn-danger" id="button-id-cancel" href="{{ view.get_success_url }}">Cancel</a>'), 
        )    


class WebAppForm(ModelForm):
    
    class Meta:
        model = WebApp
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div(
                    'name',
                    Div(
                        Div('version', css_class='col-sm-6'),
                        Div('root_url', css_class='col-sm-6'),
                        css_class='row'
                    ),
                    Div(
                        Div('programing_lang', css_class='col-sm-6'),
                        Div('programing_framework', css_class='col-sm-6'),
                        css_class='row'
                    ),
                    css_class='col-sm-6'
                ),
                Div(Field('comments', style='height: 210px;'), css_class='col-sm-6'),
                Field('port', type='hidden'),
                css_class='row',
            ),
                Submit('save', 'Submit', css_class='btn-success'),
                HTML('<a name="cancel" class="btn btn-danger" id="button-id-cancel" href="{{ view.get_success_url }}">Cancel</a>'), 
        )


class WebPageForm(ModelForm):
    
    class Meta:
        model = WebPage
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div('path', 'title', css_class='col-sm-6'),
                Div(Field('comments', style='height: 124px;'), css_class='col-sm-6'),
                Field('webapp', type='hidden'),
                css_class='row',
            ),
                Submit('save', 'Submit', css_class='btn-success'),
                HTML('<a name="cancel" class="btn btn-danger" id="button-id-cancel" href="{{ view.get_success_url }}">Cancel</a>'), 
        )