from django.urls import path

from .views import ReportList, ReportDelete, ReportTemplateCreate, ReportTemplateDelete, ReportTemplateUpdate

urlpatterns = [
    path('', ReportList.as_view(), name='report_list'),
    path('<int:pk>/delete', ReportDelete.as_view(), name='report_delete'),
    path('template/create', ReportTemplateCreate.as_view(), name='template_create'),
    path('template/<int:pk>/delete', ReportTemplateDelete.as_view(), name='template_delete'),
    path('template/<int:pk>/edit', ReportTemplateUpdate.as_view(), name='template_edit'), 
]