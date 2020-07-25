from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    AppCreate, AppDelete, AppDetail, AppUpdate,
    AttachCreate, AttachDelete,
    DomainCreate, DomainDelete,
    ProjCreate, ProjDelete, ProjDetail, ProjList, ProjUpdate,
    PocCreate, PocDelete, PocDetail, PocUpdate,
    NetAddrCreate, NetAddrDelete,
    PortCreate, PortDelete, PortDetail, PortUpdate,
    SysCreate, SysDelete, SysDetail, SysUpdate,
    VulnCreate, VulnDelete, VulnDetail, VulnUpdate,
    WebAppCreate, WebAppDelete, WebAppDetail, WebAppUpdate,
    WebPageCreate, WebPageDelete, WebPageDetail, WebPageUpdate,
)
from .views import Welcome


attach_patterns = [
    path('create/', AttachCreate.as_view(), name='attach_create'),
    path('<int:pk>/delete/', AttachDelete.as_view(), name='attach_delete'), 
]

domain_patterns = [
    path('create/', DomainCreate.as_view(), name='domain_create'),
    path('<int:pk>/delete/', DomainDelete.as_view(), name='domain_delete'), 
]

netaddress_patterns = [
    path('create/', NetAddrCreate.as_view(), name='netaddr_create'),
    path('<int:pk>/delete/', NetAddrDelete.as_view(), name='netaddr_delete'), 
]

poc_patterns = [
    path('create/', PocCreate.as_view(), name='poc_create'),
    path('<int:pk>/edit/', PocUpdate.as_view(), name='poc_edit'),
    path('<int:pk>/delete/', PocDelete.as_view(), name='poc_delete'),
    path('<int:pk>/', PocDetail.as_view(), name='poc_detail'),
]

vuln_patterns = [
    path('create/', VulnCreate.as_view(), name='vuln_create'),
    path('<int:pk>/edit/', VulnUpdate.as_view(), name='vuln_edit'),
    path('<int:pk>/delete/', VulnDelete.as_view(), name='vuln_delete'), 
    path('<int:pk>/', VulnDetail.as_view(), name='vuln_detail'),
    path('<int:vuln_pk>/attach/', include(attach_patterns)),
]

webpage_patterns = [
    path('create/', WebPageCreate.as_view(), name='webpage_create'),
    path('<int:pk>/edit/', WebPageUpdate.as_view(), name='webpage_edit'),
    path('<int:pk>/delete/', WebPageDelete.as_view(), name='webpage_delete'), 
    path('<int:pk>/', WebPageDetail.as_view(), name='webpage_detail'),
    path('<int:webpage_pk>/vuln/', include(vuln_patterns)),
    path('<int:webpage_pk>/attach/', include(attach_patterns)),
]

webapp_patterns = [
    path('create/', WebAppCreate.as_view(), name='webapp_create'),
    path('<int:pk>/edit/', WebAppUpdate.as_view(), name='webapp_edit'),
    path('<int:pk>/delete/', WebAppDelete.as_view(), name='webapp_delete'), 
    path('<int:pk>/', WebAppDetail.as_view(), name='webapp_detail'),
    path('<int:webapp_pk>/webpage/', include(webpage_patterns)),
    path('<int:webapp_pk>/vuln/', include(vuln_patterns)),
]

port_patterns = [
    path('create/', PortCreate.as_view(), name='port_create'),
    path('<int:pk>/edit/', PortUpdate.as_view(), name='port_edit'),
    path('<int:pk>/delete/', PortDelete.as_view(), name='port_delete'), 
    path('<int:pk>/', PortDetail.as_view(), name='port_detail'),
    path('<int:port_pk>/webapp/', include(webapp_patterns)),
    path('<int:port_pk>/vuln/', include(vuln_patterns)),
]

app_patterns = [
    path('create/', AppCreate.as_view(), name='app_create'),
    path('<int:pk>/edit/', AppUpdate.as_view(), name='app_edit'),
    path('<int:pk>/delete/', AppDelete.as_view(), name='app_delete'), 
    path('<int:pk>/', AppDetail.as_view(), name='app_detail'),
    path('<int:app_pk>/vuln/', include(vuln_patterns)),
]

system_patterns = [
    path('create/', SysCreate.as_view(), name='sys_create'),
    path('<int:pk>/edit/', SysUpdate.as_view(), name='sys_edit'),
    path('<int:pk>/delete/', SysDelete.as_view(), name='sys_delete'), 
    path('<int:pk>/', SysDetail.as_view(), name='sys_detail'),
    path('<int:sys_pk>/app/', include(app_patterns)),
    path('<int:sys_pk>/port/', include(port_patterns)),
    path('<int:sys_pk>/vuln/', include(vuln_patterns)),
]

proj_patterns = [
    path('', ProjList.as_view(), name='proj_list'),
    path('create/', ProjCreate.as_view(), name='proj_create'),
    path('<slug:slug>/edit/', ProjUpdate.as_view(), name='proj_edit'),
    path('<slug:slug>/delete/', ProjDelete.as_view(), name='proj_delete'),
    path('<slug:slug>/', ProjDetail.as_view(), name='proj_detail'),
    path('<slug:proj_slug>/sys/', include(system_patterns)),
    path('<slug:proj_slug>/domain/', include(domain_patterns)),
    path('<slug:proj_slug>/netaddress/', include(netaddress_patterns)),
    path('<slug:proj_slug>/poc/', include(poc_patterns)),
]

urlpatterns = [
    path('proj/', include(proj_patterns)),
    path('', Welcome.as_view(), name='welcome'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)