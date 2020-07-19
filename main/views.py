from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, View

from .models import App, Attach, Domain, NetAddr, Proj, Poc, Port, Sys, Vuln, WebApp, WebPage
from .utils import AddParentToContextMixin, GetTreeMixin, SuccessMessageMixin, SuccessUrlMixin
from .forms import AppForm, AttachForm, DomainForm, NetAddrForm, PocForm, PortForm, ProjForm, SysForm, VulnForm, WebAppForm, WebPageForm

class Welcome(View):
    def get(self, request):
        return render(request, 'main/welcome.html')

# Projects
class ProjCreate(SuccessUrlMixin, SuccessMessageMixin, CreateView):
    model = Proj
    form_class = ProjForm
    success_message = 'Project %(name)s created.'


class ProjDelete(SuccessUrlMixin, SuccessMessageMixin, DeleteView):
    model = Proj
    success_message = 'Project %(name)s deleted.'


class ProjDetail(GetTreeMixin, DetailView):
    model = Proj


class ProjList(ListView):
    model = Proj


class ProjUpdate(SuccessUrlMixin, SuccessMessageMixin, UpdateView):
    model = Proj
    form_class = ProjForm
    success_message = 'Project %(name)s updated.'    
    

# Points of Contact
class PocCreate(AddParentToContextMixin, SuccessUrlMixin, SuccessMessageMixin, CreateView):
    model = Poc
    form_class = PocForm
    success_message = 'Point of contact %(name)s created.'
    template_name = 'main/poc_form.html'

    def post(self, request, proj_slug):
        proj = get_object_or_404(Proj, slug=proj_slug)
        form = PocForm(request.POST)

        if form.is_valid():
            poc = form.save(commit=False)
            poc.proj = proj
            poc.save()
            return redirect(self.get_success_url())
        else:
            return render(request, self.template_name, {'form': form})


class PocDelete(SuccessUrlMixin, SuccessMessageMixin, DeleteView):
    model = Poc
    success_message = 'Point of contact %(name)s deleted.'


class PocDetail(GetTreeMixin, DetailView):
    model = Poc

    def get_object(self):
        proj = get_object_or_404(Proj, slug=self.kwargs['proj_slug'])
        poc = get_object_or_404(Poc, proj=proj, pk=self.kwargs['pk'])
        return poc


class PocUpdate(SuccessUrlMixin, SuccessMessageMixin, UpdateView):
    model = Poc
    form_class = PocForm
    success_message = 'Point of contact %(name)s updated.'
    template_name = 'main/poc_form.html'

    def post(self, request, proj_slug, pk):
        proj = get_object_or_404(Proj, slug=proj_slug)
        poc = get_object_or_404(Poc, proj=proj, pk=pk)
        form = PocForm(request.POST, instance=poc)

        if form.is_valid():
            poc = form.save()
            return redirect(self.get_success_url())
        else:
            return render(request, self.template_name, {'form': form})


# Domains
class DomainCreate(AddParentToContextMixin, SuccessUrlMixin, SuccessMessageMixin, CreateView):
    model = Domain
    form_class = DomainForm
    success_message = 'Domain %(domain)s created.'
    template_name = 'main/domain_form.html'    

    def post(self, request, proj_slug):
        proj = get_object_or_404(Proj, slug=proj_slug)
        form = DomainForm(request.POST)

        if form.is_valid():
            domain = form.save(commit=False)
            domain.proj = proj
            domain.save()
            return redirect(self.get_success_url())
        else:
            return render(request, self.template_name, {'form': form})


class DomainDelete(SuccessUrlMixin, SuccessMessageMixin, DeleteView):
    model = Domain
    success_message = 'Domain %(domain)s deleted.'

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


# Network Addresses
class NetAddrCreate(AddParentToContextMixin, SuccessUrlMixin, SuccessMessageMixin, CreateView):
    model = NetAddr
    form_class = NetAddrForm
    success_message = 'Network Address %(net_address)s created.'
    template_name = 'main/netaddr_form.html'

    def post(self, request, proj_slug):
        proj = get_object_or_404(Proj, slug=proj_slug)
        form = NetAddrForm(request.POST)

        if form.is_valid():
            netaddr = form.save(commit=False)
            netaddr.proj = proj
            netaddr.save()
            return redirect(self.get_success_url())
        else:
            return render(request, self.template_name, {'form': form})


class NetAddrDelete(SuccessUrlMixin, SuccessMessageMixin, DeleteView):
    model = NetAddr
    success_message = 'Network Address %(net_address)s deleted.'

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


# Systems
class SysCreate(AddParentToContextMixin, SuccessUrlMixin, SuccessMessageMixin, CreateView):
    model = Sys
    form_class = SysForm
    success_message = 'System %(ip_address)s created.'
    template_name = 'main/sys_form.html'

    def post(self, request, proj_slug):
        proj = get_object_or_404(Proj, slug=proj_slug)
        form = SysForm(request.POST)

        if form.is_valid():
            sys = form.save(commit=False)
            sys.proj = proj
            sys.save()
            return redirect(self.get_success_url())
        else:
            return render(request, self.template_name, {'form': form})


class SysDelete(SuccessUrlMixin, SuccessMessageMixin, DeleteView):
    model = Sys
    success_message = 'System %(ip_address)s deleted.'
    

class SysDetail(GetTreeMixin, DetailView):
    model = Sys

    def get_object(self):
        proj = get_object_or_404(Proj, slug=self.kwargs['proj_slug'])
        sys = get_object_or_404(Sys, proj=proj, pk=self.kwargs['pk'])
        return sys


class SysUpdate(SuccessUrlMixin, SuccessMessageMixin, UpdateView):
    model = Sys
    form_class = SysForm
    success_message = 'System %(ip_address)s updated.'
    template_name = 'main/sys_form.html'

    def post(self, request, proj_slug, pk):
        proj = get_object_or_404(Proj, slug=proj_slug)
        sys = get_object_or_404(Sys, proj=proj, pk=pk)
        form = SysForm(request.POST, instance=sys)

        if form.is_valid():
            sys = form.save()
            return redirect(self.get_success_url())
        else:
            return render(request, self.template_name, {'form': form})


# Ports
class PortCreate(AddParentToContextMixin, SuccessUrlMixin, SuccessMessageMixin, CreateView):
    model = Port
    form_class = PortForm
    success_message = 'Port %(protocol)s/%(number)s created.'
    template_name = 'main/port_form.html'

    def post(self, request, proj_slug, sys_pk):
        proj = get_object_or_404(Proj, slug=proj_slug)
        sys = get_object_or_404(Sys, proj=proj, pk=sys_pk)
        form = PortForm(request.POST)

        if form.is_valid():
            port = form.save(commit=False)
            port.sys = sys
            port.save()
            return redirect(self.get_success_url())
        else:
            return render(request, self.template_name, {'form': form})


class PortDelete(SuccessUrlMixin, SuccessMessageMixin, DeleteView):
    model = Port
    success_message = 'Port %(protocol)s/%(number)s deleted.'


class PortDetail(GetTreeMixin, DetailView):
    model = Port

    def get_object(self):
        proj = get_object_or_404(Proj, slug=self.kwargs['proj_slug'])
        sys = get_object_or_404(Sys, proj=proj, pk=self.kwargs['sys_pk'])
        port = get_object_or_404(Port, sys=sys, pk=self.kwargs['pk'])
        return port


class PortUpdate(SuccessUrlMixin, SuccessMessageMixin, UpdateView):
    model = Port
    form_class = PortForm
    success_message = 'Port %(protocol)s/%(number)s updated.'
    template_name = 'main/port_form.html'

    def post(self, request, proj_slug, sys_pk, pk):
        sys = get_object_or_404(Sys, pk=sys_pk)
        port = get_object_or_404(Port, sys=sys, pk=pk)
        form = PortForm(request.POST, instance=port)

        if form.is_valid():
            port = form.save()
            return redirect(self.get_success_url())
        else:
            return render(request, self.template_name, {'form': form})


# WebApps
class WebAppCreate(AddParentToContextMixin, SuccessUrlMixin, SuccessMessageMixin, CreateView):
    model = WebApp
    form_class = WebAppForm
    success_message = 'Webapp %(name)s created.'
    template_name = 'main/webapp_form.html'

    def post(self, request, proj_slug, sys_pk, port_pk):
        proj = get_object_or_404(Proj, slug=proj_slug)
        sys = get_object_or_404(Sys, proj=proj, pk=sys_pk)
        port = get_object_or_404(Port, sys=sys, pk=port_pk)
        form = WebAppForm(request.POST)

        if form.is_valid():
            if port.is_web_app:
                webapp = form.save(commit=False)
                webapp.port = port
                webapp.save()
                return redirect(self.get_success_url())
            else:
                messages.error(self.request, 'The port is not a web application.')
                return redirect('port_detail', proj_slug=proj.slug, sys_pk=sys.pk, pk=port.pk)
        else:
            return render(request, self.template_name, {'form': form})


class WebAppDelete(SuccessUrlMixin, SuccessMessageMixin, DeleteView):
    model = WebApp
    success_message = 'Webapp %(name)s deleted.'


class WebAppDetail(GetTreeMixin, DetailView):
    model = WebApp

    def get_object(self):
        proj = get_object_or_404(Proj, slug=self.kwargs['proj_slug'])
        sys = get_object_or_404(Sys, proj=proj, pk=self.kwargs['sys_pk'])
        port = get_object_or_404(Port, sys=sys, pk=self.kwargs['port_pk'])
        webapp = get_object_or_404(WebApp, port=port, pk=self.kwargs['pk'])
        return webapp


class WebAppUpdate(SuccessUrlMixin, SuccessMessageMixin, UpdateView):
    model = WebApp
    form_class = WebAppForm
    success_message = 'Webapp %(name)s updated.'
    template_name = 'main/webapp_form.html'

    def post(self, request, proj_slug, sys_pk, port_pk, pk):
        proj = get_object_or_404(Proj, slug=self.kwargs['proj_slug'])
        sys = get_object_or_404(Sys, proj=proj, pk=self.kwargs['sys_pk'])
        port = get_object_or_404(Port, sys=sys, pk=port_pk)
        webapp = get_object_or_404(WebApp, port=port, pk=pk)
        form = WebAppForm(request.POST, instance=webapp)

        if form.is_valid():
            webapp = form.save()
            webapp.save()
            return redirect(self.get_success_url())
        else:
            return render(request, self.template_name, {'form': form})


# WebPages
class WebPageCreate(AddParentToContextMixin, SuccessUrlMixin, SuccessMessageMixin, CreateView):
    model = WebPage
    form_class = WebPageForm
    success_message = 'Webpage %(path)s created.'
    template_name = 'main/webpage_form.html'

    def post(self, request, proj_slug, sys_pk, port_pk, webapp_pk):
        proj = get_object_or_404(Proj, slug=proj_slug)
        sys = get_object_or_404(Sys, proj=proj, pk=sys_pk)
        port = get_object_or_404(Port, sys=sys, pk=port_pk)
        webapp = get_object_or_404(WebApp, port=port, pk=webapp_pk)
        form = WebPageForm(request.POST)

        if form.is_valid():
            webpage = form.save(commit=False)
            webpage.webapp = webapp
            webpage.save()
            return redirect(self.get_success_url())
        else:
            return render(request, self.template_name, {'form': form})


class WebPageDelete(SuccessUrlMixin, SuccessMessageMixin, DeleteView):
    model = WebPage
    success_message = 'Webpage %(path)s deleted.'


class WebPageDetail(GetTreeMixin, DetailView):
    model = WebPage

    def get_object(self):
        proj = get_object_or_404(Proj, slug=self.kwargs['proj_slug'])
        sys = get_object_or_404(Sys, proj=proj, pk=self.kwargs['sys_pk'])
        port = get_object_or_404(Port, sys=sys, pk=self.kwargs['port_pk'])
        webapp = get_object_or_404(WebApp, port=port, pk=self.kwargs['webapp_pk'])
        webpage = get_object_or_404(WebPage, webapp=webapp, pk=self.kwargs['pk'])
        return webpage


class WebPageUpdate(SuccessUrlMixin, SuccessMessageMixin, UpdateView):
    model = WebPage
    form_class = WebPageForm
    success_message = 'Webpage %(path)s updated.'
    template_name = 'main/webpage_form.html'

    def post(self, request, proj_slug, sys_pk, port_pk, webapp_pk, pk):
        proj = get_object_or_404(Proj, slug=proj_slug)
        sys = get_object_or_404(Sys, proj=proj, pk=sys_pk)
        port = get_object_or_404(Port, sys=sys, pk=port_pk)
        webapp = get_object_or_404(WebApp, port=port, pk=webapp_pk)
        webpage = get_object_or_404(WebPage, webapp=webapp, pk=pk)
        form = WebPageForm(request.POST, instance=webpage)

        if form.is_valid():
            webpage = form.save()
            return redirect(self.get_success_url())
        else:
            return render(request, self.template_name, {'form': form})

# Vulnerabilities
class VulnCreate(AddParentToContextMixin, SuccessUrlMixin, SuccessMessageMixin, CreateView):
    model = Vuln
    form_class = VulnForm
    success_message = 'Vulnerability %(title)s created.'
    template_name = 'main/vuln_form.html'

    def post(self, request, proj_slug, sys_pk, port_pk=None, app_pk=None, webapp_pk=None, webpage_pk=None):
        proj = get_object_or_404(Proj, slug=proj_slug)
        sys = get_object_or_404(Sys, proj=proj, pk=sys_pk)

        if port_pk:
            port = get_object_or_404(Port, sys=sys, pk=port_pk)
        else:
            port = None

        if app_pk:
            app = get_object_or_404(App, sys=sys, pk=app_pk)
        else:
            app = None

        if webapp_pk:
            webapp = get_object_or_404(WebApp, port=port, pk=webapp_pk)
        else:
            webapp = None

        if webpage_pk:
            webpage = get_object_or_404(WebPage, webapp=webapp, pk=webpage_pk)
        else:
            webpage = None

        form = VulnForm(request.POST)

        if form.is_valid():
            vuln = form.save(commit=False)
            if webpage:
                vuln.webpage = webpage
            elif webapp:
                vuln.webapp = webapp
            elif app:
                vuln.app = app
            elif port:
                vuln.port = port
            elif sys:
                vuln.sys = sys
            vuln.save()
            return redirect(self.get_success_url())
        else:
            return render(request, self.template_name, {'form': form})    


class VulnDelete(AddParentToContextMixin, SuccessUrlMixin, SuccessMessageMixin, DeleteView):
    model = Vuln
    success_message = 'Vulnerability %(title)s deleted.'


class VulnDetail(GetTreeMixin, DetailView):
    model = Vuln

    def get_object(self):
        proj = get_object_or_404(Proj, slug=self.kwargs['proj_slug'])

        if 'sys_pk' in self.kwargs:
            sys = get_object_or_404(Sys, proj=proj, pk=self.kwargs['sys_pk'])
        else:
            sys = None

        if 'port_pk' in self.kwargs:
            port = get_object_or_404(Port, sys=sys, pk=self.kwargs['port_pk'])
        else:
            port = None

        if 'app_pk' in self.kwargs:
            app = get_object_or_404(App, sys=sys, pk=self.kwargs['app_pk'])
        else:
            app = None

        if 'webapp_pk' in self.kwargs:
            webapp = get_object_or_404(WebApp, port=port, pk=self.kwargs['webapp_pk'])
        else:
            webapp = None

        if 'webpage_pk' in self.kwargs:
            webpage = get_object_or_404(WebPage, webapp=webapp, pk=self.kwargs['webpage_pk'])
        else:
            webpage = None
        
        if webpage:
            vuln = get_object_or_404(Vuln, webpage=webpage, pk=self.kwargs['pk'])
        elif webapp:
            vuln = get_object_or_404(Vuln, webapp=webapp, pk=self.kwargs['pk'])
        elif app:
            vuln = get_object_or_404(Vuln, app=app, pk=self.kwargs['pk'])
        elif port:
            vuln = get_object_or_404(Vuln, port=port, pk=self.kwargs['pk'])
        elif sys:
            vuln = get_object_or_404(Vuln, sys=sys, pk=self.kwargs['pk'])

        return vuln

class VulnUpdate(SuccessUrlMixin, SuccessMessageMixin, UpdateView):
    model = Vuln
    form_class = VulnForm
    success_message = 'Vulnerability %(title)s updated.'
    template_name = 'main/vuln_form.html'

    def post(self, request, proj_slug, sys_pk, pk, port_pk=None, app_pk=None, webapp_pk=None, webpage_pk=None):
        proj = get_object_or_404(Proj, slug=proj_slug)
        sys = get_object_or_404(Sys, proj=proj, pk=sys_pk)

        if port_pk:
            port = get_object_or_404(Port, sys=sys, pk=port_pk)
        else:
            port = None

        if app_pk:
            app = get_object_or_404(App, sys=sys, pk=app_pk)
        else:
            app = None

        if webapp_pk:
            webapp = get_object_or_404(WebApp, port=port, pk=webapp_pk)
        else:
            webapp = None

        if webpage_pk:
            webpage = get_object_or_404(WebPage, webapp=webapp, pk=webpage_pk)
        else:
            webpage = None

        if webpage:
            vuln = get_object_or_404(Vuln, webpage=webpage, pk=pk)
        elif webapp:
            vuln = get_object_or_404(Vuln, webapp=webapp, pk=pk)
        elif app:
            vuln = get_object_or_404(Vuln, app=app, pk=pk)
        elif port:
            vuln = get_object_or_404(Vuln, port=port, pk=pk)
        elif sys:
            vuln = get_object_or_404(Vuln, sys=sys, pk=pk)

        form = VulnForm(request.POST, instance=vuln)

        if form.is_valid():
            vuln = form.save()
            vuln.save()
            return redirect(self.get_success_url())
        else:
            return render(request, self.template_name, {'form': form})   


# Attachment
class AttachCreate(AddParentToContextMixin, SuccessUrlMixin, SuccessMessageMixin, CreateView):
    model = Attach
    form_class = AttachForm
    success_message = 'Attachment %(name)s created.'
    template_name = 'main/attach_form.html'

    def post(self, request, proj_slug, sys_pk, port_pk=None, app_pk=None, webapp_pk=None, webpage_pk=None, vuln_pk=None):
        
        proj = get_object_or_404(Proj, slug=proj_slug)
        sys = get_object_or_404(Sys, proj=proj, pk=sys_pk)

        if port_pk:
            port = get_object_or_404(Port, sys=sys, pk=port_pk)
        else:
            port = None

        if app_pk:
            app = get_object_or_404(App, sys=sys, pk=app_pk)
        else:
            app = None

        if webapp_pk:
            webapp = get_object_or_404(WebApp, port=port, pk=webapp_pk)
        else:
            webapp = None

        if webpage_pk:
            webpage = get_object_or_404(WebPage, webapp=webapp, pk=webpage_pk)
        else:
            webpage = None

        if vuln_pk:
            if webpage:
                vuln = get_object_or_404(Vuln, webpage=webpage, pk=vuln_pk)
            elif webapp:
                vuln = get_object_or_404(Vuln, webapp=webapp, pk=vuln_pk)
            elif port:
                vuln = get_object_or_404(Vuln, port=port, pk=vuln_pk)
            elif app:
                vuln = get_object_or_404(Vuln, app=app, pk=vuln_pk)
            elif sys:
                vuln = get_object_or_404(Vuln, sys=sys, pk=vuln_pk)
        else:
            vuln = None

        form = AttachForm(request.POST, request.FILES)

        if form.is_valid():
            attach = form.save(commit=False)
            if vuln:
                attach.vuln = vuln
                attach.save()
            else:
                attach.webpage = webpage
                attach.save()
            return redirect(self.get_success_url())
        else:
            return render(request, self.template_name, {'form': form})


class AttachDelete(SuccessUrlMixin, SuccessMessageMixin, DeleteView):
    model = Attach
    success_message = 'Attachment %(name)s deleted.'

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


# Apps
class AppCreate(AddParentToContextMixin, SuccessUrlMixin, SuccessMessageMixin, CreateView):
    model = App
    form_class = AppForm
    success_message = 'App %(name)s created.'
    template_name = 'main/app_form.html'

    def post(self, request, proj_slug, sys_pk):
        proj = get_object_or_404(Proj, slug=proj_slug)
        sys = get_object_or_404(Sys, proj=proj, pk=sys_pk)
        form = AppForm(request.POST)

        if form.is_valid():
            app = form.save(commit=False)
            app.sys = sys
            app.save()
            return redirect(self.get_success_url())
        else:
            return render(request, self.template_name, {'form': form})


class AppDelete(SuccessUrlMixin, SuccessMessageMixin, DeleteView):
    model = App
    success_message = 'App %(name)s deleted.'


class AppDetail(GetTreeMixin, DetailView):
    model = App

    def get_object(self):
        proj = get_object_or_404(Proj, slug=self.kwargs['proj_slug'])
        sys = get_object_or_404(Sys, proj=proj, pk=self.kwargs['sys_pk'])
        app = get_object_or_404(App, sys=sys, pk=self.kwargs['pk'])
        return app


class AppUpdate(SuccessUrlMixin, SuccessMessageMixin, UpdateView):
    model = App
    form_class = AppForm
    success_message = 'App %(name)s updated.'
    template_name = 'main/app_form.html'

    def post(self, request, proj_slug, sys_pk, pk):
        proj = get_object_or_404(Proj, slug=proj_slug)
        sys = get_object_or_404(Sys, proj=proj, pk=sys_pk)
        app = get_object_or_404(App, sys=sys, pk=pk)
        form = AppForm(request.POST, instance=app)

        if form.is_valid():
            app = form.save()
            app.save()
            return redirect(self.get_success_url())
        else:
            return render(request, self.template_name, {'form': form})