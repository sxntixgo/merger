from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin as SuccMessMixin
from django.urls import reverse


class SuccessUrlMixin():
    def get_success_url(self):
        if self.request.session['vuln']:
            return reverse('vuln_detail', kwargs={'pk':self.request.session['vuln']['pk']})
        elif self.request.session['webpage']:
            return reverse('webpage_detail', kwargs={'pk':self.request.session['webpage']['pk']})
        elif self.request.session['webapp']:
            return reverse('webapp_detail', kwargs={'pk':self.request.session['webapp']['pk']})
        elif self.request.session['app']:
            return reverse('app_detail', kwargs={'pk':self.request.session['app']['pk']})
        elif self.request.session['port']:
            return reverse('port_detail', kwargs={'pk':self.request.session['port']['pk']})
        elif self.request.session['poc']:
            return reverse('poc_detail', kwargs={'pk':self.request.session['poc']['pk']})
        elif self.request.session['sys']:
            return reverse('sys_detail', kwargs={'pk':self.request.session['sys']['pk']})
        else:
            return reverse('proj_detail', kwargs={'pk':self.request.session['proj']['pk']})

# It seems SuccessMessageMixin is not implemented for DeleteView
# https://stackoverflow.com/a/42656041
class SuccessMessageMixin(SuccMessMixin):
    def delete(self, request, *args, **kwargs):
        print('delete')
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super().delete(request, *args, **kwargs)