from django.forms import ModelForm, HiddenInput
from .models import App, Attach, Domain, NetAddr, Poc, Port, Sys, Vuln, WebApp, WebPage


class AppForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(AppForm, self).__init__(*args, **kwargs)
        self.fields['sys'].widget = HiddenInput()

    class Meta:
        model = App
        fields = '__all__'


class AttachForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(AttachForm, self).__init__(*args, **kwargs)
        self.fields['vuln'].widget = HiddenInput()
        self.fields['webpage'].widget = HiddenInput()

    class Meta:
        model = Attach
        fields = '__all__'


class DomainForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(DomainForm, self).__init__(*args, **kwargs)
        self.fields['proj'].widget = HiddenInput()

    class Meta:
        model = Domain
        fields = '__all__'


class NetAddrForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(NetAddrForm, self).__init__(*args, **kwargs)
        self.fields['proj'].widget = HiddenInput()

    class Meta:
        model = NetAddr
        fields = '__all__'


class PocForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(PocForm, self).__init__(*args, **kwargs)
        self.fields['proj'].widget = HiddenInput()

    class Meta:
        model = Poc
        fields = '__all__'


class PortForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(PortForm, self).__init__(*args, **kwargs)
        self.fields['sys'].widget = HiddenInput()
    
    class Meta:
        model = Port
        fields = '__all__'


class SysForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(SysForm, self).__init__(*args, **kwargs)
        self.fields['proj'].widget = HiddenInput()

    class Meta:
        model = Sys
        fields = '__all__'


class VulnForm(ModelForm):
    
    class Meta:
        model = Vuln
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(VulnForm, self).__init__(*args, **kwargs)
        self.fields['sys'].widget = HiddenInput()
        self.fields['app'].widget = HiddenInput()
        self.fields['port'].widget = HiddenInput()
        self.fields['webapp'].widget = HiddenInput()
        self.fields['webpage'].widget = HiddenInput()
        self.fields['proj'].widget = HiddenInput()


class WebAppForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(WebAppForm, self).__init__(*args, **kwargs)
        self.fields['port'].widget = HiddenInput()
    
    class Meta:
        model = WebApp
        fields = '__all__'


class WebPageForm(ModelForm):
    
    class Meta:
        model = WebPage
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(WebPageForm, self).__init__(*args, **kwargs)
        self.fields['webapp'].widget = HiddenInput()