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