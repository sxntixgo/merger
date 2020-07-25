from django.contrib import messages
from main.views import SuccessMessageMixin
from django.core.files import File
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views import View
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import ReportTemplateForm
from .models import Report, ReportTemplate
from .utils import generate_document
from main.models import Attach, Proj, Vuln
from main.utils import SuccessMessageMixin

from os import remove

from django.conf import settings

# Reports
class ReportList(ListView):
    model = Report

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projs'] = Proj.objects.all()
        context['templates'] = ReportTemplate.objects.all()
        self.request.session['proj'] = None
        self.request.session['sys'] = None
        self.request.session['poc'] = None
        self.request.session['app'] = None
        self.request.session['port'] = None
        self.request.session['webapp'] = None
        self.request.session['webpage'] = None
        self.request.session['vuln'] = None
        return context

    def post(self, request):
        path = f'{settings.MEDIA_ROOT}/'
        proj_name = request.POST.get('proj_name')
        
        report = Report()
        report.name = generate_document(request, path)
        with open(path + report.name, 'rb') as f:
            report.media.save(report.name, File(f))
        remove(path + report.name)
        report.proj = Proj.objects.filter(name=proj_name).first()
        report.save()

        return redirect('report_list')
 
class ReportDelete(SuccessMessageMixin, DeleteView):
    model = Report
    success_url = reverse_lazy('report_list')
    success_message = 'Report %(media)s deleted.'



# Report Templates
class ReportTemplateCreate(SuccessMessageMixin, CreateView):
    model = ReportTemplate
    form_class = ReportTemplateForm
    success_message = 'Report Template %(name)s created.'
    success_url = reverse_lazy('report_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

class ReportTemplateDelete(SuccessMessageMixin, DeleteView):
    model = ReportTemplate
    success_url = reverse_lazy('report_list')
    success_message = 'Report Template %(name)s deleted.'


class ReportTemplateUpdate(SuccessMessageMixin, UpdateView):

    model = ReportTemplate
    form_class = ReportTemplateForm
    success_message = 'Report Template %(name)s updated.'
    success_url = reverse_lazy('report_list')