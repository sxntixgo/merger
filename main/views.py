from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, View

from .models import App, Attach, Domain, NetAddr, Proj, Poc, Port, Sys, Vuln, WebApp, WebPage
from .utils import SuccessUrlMixin
from .forms import AppForm, AttachForm, DomainForm, NetAddrForm, PocForm, PortForm, SysForm, VulnForm, WebAppForm, WebPageForm

class Welcome(View):
    def get(self, request):
        request.session['proj'] = None
        request.session['sys'] = None
        request.session['poc'] = None
        request.session['app'] = None
        request.session['port'] = None
        request.session['webapp'] = None
        request.session['webpage'] = None
        request.session['vuln'] = None
        return render(request, 'main/welcome.html')

# Projects
class ProjCreate(SuccessMessageMixin, CreateView):
    model = Proj
    fields = '__all__'
    success_message = 'Project %(name)s created.'


class ProjDelete(SuccessMessageMixin, DeleteView):
    model = Proj
    success_url = reverse_lazy('proj_list')
    success_message = 'Project %(name)s deleted.'

# It seems SuccessMessageMixin is not implemented for DeleteView
# https://stackoverflow.com/a/42656041
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(ProjDelete, self).delete(request, *args, **kwargs)


class ProjDetail(DetailView):
    model = Proj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        proj = self.get_object()
        self.request.session['proj'] = {}
        self.request.session['proj']['pk'] = proj.pk
        self.request.session['proj']['str'] = str(proj)
        self.request.session['sys'] = None
        self.request.session['poc'] = None
        self.request.session['app'] = None
        self.request.session['port'] = None
        self.request.session['webapp'] = None
        self.request.session['webpage'] = None
        self.request.session['vuln'] = None
        return context


class ProjList(ListView):
    model = Proj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.request.session['proj'] = None
        self.request.session['sys'] = None
        self.request.session['poc'] = None
        self.request.session['app'] = None
        self.request.session['port'] = None
        self.request.session['webapp'] = None
        self.request.session['webpage'] = None
        self.request.session['vuln'] = None
        return context


class ProjUpdate(SuccessMessageMixin, UpdateView):
    model = Proj
    fields = '__all__'
    success_message = 'Project %(name)s updated.'


# Points of Contact
class PocCreate(SuccessUrlMixin, SuccessMessageMixin, CreateView):
    model = Poc
    form_class = PocForm
    success_message = 'Point of contact %(name)s created.'

    def get_initial(self):
        initial = super(PocCreate, self).get_initial()
        initial['proj'] = self.request.session['proj']['pk']
        return initial


class PocDelete(SuccessUrlMixin, SuccessMessageMixin, DeleteView):
    model = Poc
    success_message = 'Point of contact %(name)s deleted.'

# It seems SuccessMessageMixin is not implemented for DeleteView
# https://stackoverflow.com/a/42656041
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(PocDelete, self).delete(request, *args, **kwargs)


class PocDetail(DetailView):
    model = Poc

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        poc = self.get_object()
        self.request.session['poc'] = {}
        self.request.session['poc']['pk'] = poc.pk
        self.request.session['poc']['str'] = str(poc)
        self.request.session['sys'] = None
        self.request.session['app'] = None
        self.request.session['port'] = None
        self.request.session['webapp'] = None
        self.request.session['webpage'] = None
        self.request.session['vuln'] = None
        return context 


class PocUpdate(SuccessUrlMixin, SuccessMessageMixin, UpdateView):
    model = Poc
    form_class = PocForm
    success_message = 'Point of contact %(name)s updated.'


# Domains
class DomainCreate(SuccessUrlMixin, SuccessMessageMixin, CreateView):
    model = Domain
    form_class = DomainForm
    success_message = 'Domain %(domain)s created.'
    

    def get_initial(self):
        initial = super(DomainCreate, self).get_initial()
        initial['proj'] = self.request.session['proj']['pk']
        return initial


class DomainDelete(SuccessUrlMixin, SuccessMessageMixin, DeleteView):
    model = Domain
    success_message = 'Domain %(domain)s deleted.'

# It seems SuccessMessageMixin is not implemented for DeleteView
# https://stackoverflow.com/a/42656041
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(DomainDelete, self).delete(request, *args, **kwargs)

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


# Network Addresses
class NetAddrCreate(SuccessUrlMixin, SuccessMessageMixin, CreateView):
    model = NetAddr
    form_class = NetAddrForm
    success_message = 'Network Address %(net_address)s created.'
    

    def get_initial(self):
        initial = super(NetAddrCreate, self).get_initial()
        initial['proj'] = self.request.session['proj']['pk']
        return initial


class NetAddrDelete(SuccessUrlMixin, SuccessMessageMixin, DeleteView):
    model = NetAddr
    success_message = 'Network Address %(net_address)s deleted.'

# It seems SuccessMessageMixin is not implemented for DeleteView
# https://stackoverflow.com/a/42656041
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(NetAddrDelete, self).delete(request, *args, **kwargs)

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

# Systems
class SysCreate(SuccessUrlMixin, SuccessMessageMixin, CreateView):
    model = Sys
    form_class = SysForm
    success_message = 'System %(ip_address)s created.'

    def get_initial(self):
        initial = super(SysCreate, self).get_initial()
        initial['proj'] = self.request.session['proj']['pk']
        return initial


class SysDelete(SuccessUrlMixin, DeleteView):
    model = Sys
    success_message = 'System %(ip_address)s deleted.'

# It seems SuccessMessageMixin is not implemented for DeleteView
# https://stackoverflow.com/a/42656041
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(SysDelete, self).delete(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.request.session['sys'] = None 
        return context
    

class SysDetail(DetailView):
    model = Sys

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sys = self.get_object()
        self.request.session['sys'] = {}
        self.request.session['sys']['pk'] = sys.pk
        self.request.session['sys']['str'] = str(sys)
        self.request.session['app'] = None
        self.request.session['port'] = None
        self.request.session['webapp'] = None
        self.request.session['webpage'] = None
        self.request.session['vuln'] = None
        return context


class SysUpdate(SuccessUrlMixin, SuccessMessageMixin, UpdateView):
    model = Sys
    form_class = SysForm
    success_message = 'System %(ip_address)s updated.'


# Ports
class PortCreate(SuccessUrlMixin, SuccessMessageMixin, CreateView):
    model = Port
    form_class = PortForm
    success_message = 'Port %(protocol)s/%(number)s created.'
    
    def get_initial(self):
        initial = super(PortCreate, self).get_initial()
        initial['sys'] = self.request.session['sys']['pk']
        return initial


class PortDelete(SuccessUrlMixin, DeleteView):
    model = Port
    success_message = 'Port %(protocol)s/%(number)s deleted.'

# It seems SuccessMessageMixin is not implemented for DeleteView
# https://stackoverflow.com/a/42656041
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(PortDelete, self).delete(request, *args, **kwargs)

class PortDetail(DetailView):
    model = Port

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        port = self.get_object()
        self.request.session['port'] = {}
        self.request.session['port']['pk'] = port.pk
        self.request.session['port']['str'] = str(port)
        self.request.session['app'] = None
        self.request.session['webapp'] = None
        self.request.session['webpage'] = None
        self.request.session['vuln'] = None
        return context


class PortUpdate(SuccessUrlMixin, SuccessMessageMixin, UpdateView):
    model = Port
    form_class = PortForm
    success_message = 'Port %(protocol)s/%(number)s updated.'


# WebApps
class WebAppCreate(SuccessUrlMixin, SuccessMessageMixin, CreateView):
    model = WebApp
    form_class = WebAppForm
    success_message = 'Webapp %(name)s created.'
    
    def get_initial(self):
        initial = super(WebAppCreate, self).get_initial()
        initial['port'] = self.request.session['port']['pk']
        return initial


class WebAppDelete(SuccessUrlMixin, DeleteView):
    model = WebApp
    success_message = 'Webapp %(name)s deleted.'

# It seems SuccessMessageMixin is not implemented for DeleteView
# https://stackoverflow.com/a/42656041
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(WebAppDelete, self).delete(request, *args, **kwargs)

class WebAppDetail(DetailView):
    model = WebApp

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        webapp = self.get_object()
        self.request.session['webapp'] = {}
        self.request.session['webapp']['pk'] = webapp.pk
        self.request.session['webapp']['str'] = str(webapp)
        self.request.session['webpage'] = None
        self.request.session['vuln'] = None
        return context


class WebAppUpdate(SuccessUrlMixin, SuccessMessageMixin, UpdateView):
    model = WebApp
    form_class = WebAppForm
    success_message = 'Webapp %(name)s updated.'



# WebPages
class WebPageCreate(SuccessUrlMixin, SuccessMessageMixin, CreateView):
    model = WebPage
    form_class = WebPageForm
    success_message = 'Webpage %(path)s created.'
    
    def get_initial(self):
        initial = super(WebPageCreate, self).get_initial()
        initial['webapp'] = self.request.session['webapp']['pk']
        return initial


class WebPageDelete(SuccessUrlMixin,  DeleteView):
    model = WebPage
    success_message = 'Webpage %(path)s deleted.'

# It seems SuccessMessageMixin is not implemented for DeleteView
# https://stackoverflow.com/a/42656041
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(WebPageDelete, self).delete(request, *args, **kwargs)

class WebPageDetail(DetailView):
    model = WebPage

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        webpage = self.get_object()
        self.request.session['webpage'] = {}
        self.request.session['webpage']['pk'] = webpage.pk
        self.request.session['webpage']['str'] = str(webpage)
        self.request.session['vuln'] = None
        return context


class WebPageUpdate(SuccessUrlMixin, SuccessMessageMixin, UpdateView):
    model = WebPage
    form_class = WebPageForm
    success_message = 'Webpage %(path)s updated.'

# Vulnerabilities
class VulnCreate(SuccessUrlMixin, SuccessMessageMixin, CreateView):
    model = Vuln
    form_class = VulnForm
    success_message = 'Vulnerability %(title)s created.'
    
    def get_initial(self):
        initial = super(VulnCreate, self).get_initial()
        if self.request.session['webpage']:
            initial['webpage'] = self.request.session['webpage']['pk']
        elif self.request.session['webapp']:
            initial['webapp'] = self.request.session['webapp']['pk']
        elif self.request.session['port']:
            initial['port'] = self.request.session['port']['pk']
        elif self.request.session['app']:
            initial['app'] = self.request.session['app']['pk']
        elif self.request.session['sys']:
            initial['sys'] = self.request.session['sys']['pk']
        initial['proj'] = self.request.session['proj']['pk']
        return initial


class VulnDelete(SuccessUrlMixin, DeleteView):
    model = Vuln
    success_message = 'Vulnerability %(title)s deleted.'
    
# It seems SuccessMessageMixin is not implemented for DeleteView
# https://stackoverflow.com/a/42656041
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(VulnDelete, self).delete(request, *args, **kwargs)


class VulnDetail(DetailView):
    model = Vuln

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vuln = self.get_object()
        self.request.session['vuln'] = {}
        self.request.session['vuln']['pk'] = vuln.pk
        self.request.session['vuln']['str'] = str(vuln)
        return context

class VulnUpdate(SuccessUrlMixin, SuccessMessageMixin, UpdateView):
    model = Vuln
    form_class = VulnForm
    success_message = 'Vulnerability %(title)s updated.'


# Attachment
class AttachCreate(SuccessUrlMixin, SuccessMessageMixin, CreateView):
    model = Attach
    form_class = AttachForm
    success_message = 'Attachment %(name)s created.'
    
    def get_initial(self):
        initial = super(AttachCreate, self).get_initial()
        if self.request.session['vuln']:
            initial['vuln'] = self.request.session['vuln']['pk']
        elif self.request.session['webpage']:
            initial['webpage'] = self.request.session['webpage']['pk']
        return initial


class AttachDelete(SuccessUrlMixin, DeleteView):
    model = Attach
    success_message = 'Attachment %(name)s deleted.'
    

# It seems SuccessMessageMixin is not implemented for DeleteView
# https://stackoverflow.com/a/42656041
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(AttachDelete, self).delete(request, *args, **kwargs)


# Apps
class AppCreate(SuccessUrlMixin, SuccessMessageMixin, CreateView):
    model = App
    form_class = AppForm
    success_message = 'App %(name)s created.'
    
    def get_initial(self):
        initial = super(AppCreate, self).get_initial()
        initial['sys'] = self.request.session['sys']['pk']
        return initial


class AppDelete(SuccessUrlMixin, DeleteView):
    model = App
    success_message = 'App %(name)s deleted.'

# It seems SuccessMessageMixin is not implemented for DeleteView
# https://stackoverflow.com/a/42656041
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(AppDelete, self).delete(request, *args, **kwargs)

class AppDetail(DetailView):
    model = App

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        app = self.get_object()
        self.request.session['app'] = {}
        self.request.session['app']['pk'] = app.pk
        self.request.session['app']['str'] = str(app)
        self.request.session['port'] = None
        self.request.session['webapp'] = None
        self.request.session['webpage'] = None
        self.request.session['vuln'] = None
        return context


class AppUpdate(SuccessUrlMixin, SuccessMessageMixin, UpdateView):
    model = App
    form_class = AppForm
    success_message = 'App %(name)s updated.'