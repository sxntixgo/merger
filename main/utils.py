from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin as SuccMessMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse

from .models import App, Port, Proj, Sys, Vuln, WebApp, WebPage

class AddParentToContextMixin():
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        proj = None
        sys = None
        vuln = None
        app = None
        port = None
        webapp = None
        webpage = None

        if 'proj_slug' in self.kwargs:
            proj = get_object_or_404(Proj, slug=self.kwargs['proj_slug'])
            if 'sys_pk' in self.kwargs:
                sys = get_object_or_404(Sys, proj=proj, pk=self.kwargs['sys_pk'])
                if 'port_pk' in self.kwargs:
                    port = get_object_or_404(Port, sys=sys, pk=self.kwargs['port_pk'])
                    if 'webapp_pk' in self.kwargs:
                        webapp = get_object_or_404(WebApp, port=port, pk=self.kwargs['webapp_pk'])
                        if 'webpage_pk' in self.kwargs:
                            webpage = get_object_or_404(WebPage, webapp=webapp, pk=self.kwargs['webpage_pk'])
                            if 'vuln_pk' in self.kwargs:
                                vuln = get_object_or_404(Vuln, webpage=webpage, pk=self.kwargs['vuln_pk'])
                        elif 'vuln_pk' in self.kwargs:
                            vuln = get_object_or_404(Vuln, webapp=webapp, pk=self.kwargs['vuln_pk'])
                    elif 'vuln_pk' in self.kwargs:
                        vuln = get_object_or_404(Vuln, port=port, pk=self.kwargs['vuln_pk'])
                elif 'app_pk' in self.kwargs:
                    app = get_object_or_404(App, sys=sys, pk=self.kwargs['app_pk'])
                    if 'vuln_pk' in self.kwargs:
                        vuln = get_object_or_404(Vuln, app=app, pk=self.kwargs['vuln_pk'])
                elif 'vuln_pk' in self.kwargs:
                    vuln = get_object_or_404(Vuln, sys=sys, pk=self.kwargs['vuln_pk'])

        if vuln:
            context['vuln'] = vuln
        elif webpage:
            context['webpage'] = webpage
        elif webapp:
            context['webapp'] = webapp
        elif port:
            context['port'] = port
        elif app:
            context['app'] = app
        elif sys:
            context['sys'] = sys
        elif proj:
            context['proj'] = proj

        return context


class SuccessUrlMixin():

    def get_success_url(self):
        next_ = self.request.GET.get('next', '')
        if next_:
            return next_
        elif 'proj_slug' in self.kwargs:
            return reverse('proj_detail', kwargs={'slug': self.kwargs['proj_slug']})
        else:
            return reverse('welcome')


# It seems SuccessMessageMixin is not implemented for DeleteView
# https://stackoverflow.com/a/42656041
class SuccessMessageMixin(SuccMessMixin):
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super().delete(request, *args, **kwargs)

class GetTreeMixin():

    def append_vulns(self, _object, nodes):

        if isinstance(_object, Sys):
            reverse_args = {'proj_slug': _object.proj.slug, 'sys_pk': _object.pk}
        elif isinstance(_object, App):
            reverse_args = {'proj_slug': _object.sys.proj.slug, 'sys_pk': _object.sys.pk, 'app_pk': _object.pk}
        elif isinstance(_object, Port):
            reverse_args = {'proj_slug': _object.sys.proj.slug, 'sys_pk': _object.sys.pk, 'port_pk': _object.pk}
        elif isinstance(_object, WebApp):
            reverse_args = {'proj_slug': _object.port.sys.proj.slug, 'sys_pk': _object.port.sys.pk, 'port_pk': _object.port.pk, 'webapp_pk': _object.pk}
        elif isinstance(_object, WebPage):
            reverse_args = {'proj_slug': _object.webapp.port.sys.proj.slug, 'sys_pk': _object.webapp.port.sys.pk, 'port_pk': _object.webapp.port.pk, 'webapp_pk': _object.webapp.pk, 'webpage_pk': _object.pk}
        else:
            reverse_args = {}

        for vuln in _object.vuln_set.all():
            
            vuln_node = {
                'text': str(vuln),
                'icon': 'feather crosshair',
            }

            if reverse_args:
                reverse_args['pk'] = vuln.pk
                vuln_node['href'] = reverse('vuln_detail', kwargs=reverse_args)

            if vuln.attach_set.all():
                vuln_node['nodes'] = []

                for attach in vuln.attach_set.all():
                    attach_node = {
                        'text': attach.name,
                        'icon': 'feather image',
                        'href': attach.media.url,
                    }

                    vuln_node['nodes'].append(attach_node)

            nodes.append(vuln_node)

        return nodes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tree = []

        if 'slug' in self.kwargs:
            slug = self.kwargs['slug']
        elif 'proj_slug' in self.kwargs:
            slug = self.kwargs['proj_slug']
        else:
            slug = None
        
        proj = get_object_or_404(Proj, slug=slug)

        for sys in proj.sys_set.all():
            sys_node = {
                'text': str(sys),
                'icon': 'feather monitor',
                'href': reverse('sys_detail', kwargs={'proj_slug': slug, 'pk': sys.pk}),
            }

            if sys.port_set.all() or sys.app_set.all() or sys.vuln_set.all():
                sys_node['nodes'] = []

                for port in sys.port_set.all():
                    port_node = {
                        'text': str(port),
                        'icon': 'feather hash',
                        'href': reverse('port_detail', kwargs={'proj_slug': slug, 'sys_pk': sys.pk, 'pk': port.pk}),
                    }

                    if port.webapp_set.all() or port.vuln_set.all():
                        port_node['nodes'] = []

                        for webapp in port.webapp_set.all():
                            webapp_node = {
                                'text': str(webapp),
                                'icon': 'feather globe',
                                'href': reverse('webapp_detail', kwargs={'proj_slug': slug, 'sys_pk': sys.pk, 'port_pk': port.pk, 'pk': webapp.pk}),
                            }

                            if webapp.webpage_set.all() or webapp.vuln_set.all():
                                webapp_node['nodes'] = []

                                for webpage in webapp.webpage_set.all():
                                    webpage_node = {
                                        'text': str(webpage),
                                        'icon': 'feather file-text',
                                        'href': reverse('webpage_detail', kwargs={'proj_slug': slug, 'sys_pk': sys.pk, 'port_pk': port.pk, 'webapp_pk': webapp.pk, 'pk': webpage.pk}),
                                    }

                                    if webpage.attach_set.all() or webpage.vuln_set.all():
                                        webpage_node['nodes'] = []

                                        for attach in webpage.attach_set.all():
                                            attach_node = {
                                                'text': attach.name,
                                                'icon': 'feather image',
                                                'href': attach.media.url,
                                            }
                                            webpage_node['nodes'].append(attach_node)

                                        webpage_node['nodes'] = self.append_vulns(webpage, webpage_node['nodes'])

                                    webapp_node['nodes'].append(webpage_node)

                                webapp_node['nodes'] = self.append_vulns(webapp, webapp_node['nodes'])

                            port_node['nodes'].append(webapp_node)

                        port_node['nodes'] = self.append_vulns(port, port_node['nodes'])

                    sys_node['nodes'].append(port_node)

                for app in sys.app_set.all():
                    app_node = {
                        'text': str(app),
                        'icon': 'feather layout',
                        'href': reverse('app_detail', kwargs={'proj_slug': slug, 'sys_pk': sys.pk, 'pk': app.pk}),
                    }

                    if app.vuln_set.all():
                        app_node['nodes'] = []
                        app_node['nodes'] = self.append_vulns(app, app_node['nodes'])
                    
                    sys_node['nodes'].append(app_node) 

                sys_node['nodes'] = self.append_vulns(sys, sys_node['nodes'])
            
            tree.append(sys_node)

        for poc in proj.poc_set.all():
            poc_node = {
                'text': poc.name,
                'icon': 'feather user',
                'href': reverse('poc_detail', kwargs={'proj_slug': slug, 'pk': poc.pk}),
            }
            tree.append(poc_node)

        context['tree'] = tree
        return context