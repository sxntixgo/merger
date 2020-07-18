from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

from phonenumber_field.modelfields import PhoneNumberField
from random import randint


RISK = (
    (0, 'Info'),  
    (1, 'Low'),
    (2, 'Medium'),
    (3, 'High'),
    (4, 'Critical'),
)

class App(models.Model):

    name = models.CharField(max_length=50)
    version = models.CharField(max_length=50, blank=True)
    sys = models.ForeignKey('Sys', on_delete=models.SET_NULL, null=True, blank=True)
    comments = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Attach(models.Model):

    media = models.FileField(upload_to='uploads/', max_length=256)
    name = models.CharField(max_length=50)
    caption = models.CharField(max_length=200, blank=True)
    vuln = models.ForeignKey('Vuln', on_delete=models.SET_NULL, null=True, blank=True)
    webpage = models.ForeignKey('WebPage', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Domain(models.Model):
    domain = models.CharField(max_length=50)
    proj = models.ForeignKey('Proj', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.domain


class NetAddr(models.Model):

    net_address = models.CharField('Network Address', max_length=50)
    proj = models.ForeignKey('Proj', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.net_address


class Poc(models.Model):

    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    phone = PhoneNumberField('Phone Number', blank=True)
    proj = models.ForeignKey('Proj', on_delete=models.SET_NULL, null=True, blank=True)
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Port(models.Model):

    PROTOCOL = (
        (6, 'TCP'),
        (17, 'UDP')
    )

    number = models.IntegerField()
    service_name = models.CharField(max_length=50, blank=True)
    version = models.CharField(max_length=50, blank=True)
    protocol = models.IntegerField(choices=PROTOCOL, default=6)
    is_web_app = models.BooleanField()
    comments = models.TextField(blank=True)
    sys = models.ForeignKey('Sys', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['protocol', 'number']

    def __str__(self):

        return_text = f'{self.get_protocol_text()}:{self.number}'
        if self.is_web_app:
            return_text = f'{return_text} (Webapp)'
        return return_text

    def get_protocol_text(self):
        for protocol in self.PROTOCOL:
            if self.protocol == protocol[0]:
                return protocol[1]
        return 'N/A'


class Proj(models.Model):

    name = models.CharField('Project Name', max_length=50)
    org_name = models.CharField('Organization Name', max_length=50, blank=True)
    init_date = models.DateField('Start date', auto_now=False, auto_now_add=False, blank=True, null=True)
    end_date = models.DateField('End date', auto_now=False, auto_now_add=False, blank=True, null=True)
    slug = models.SlugField(max_length=63, unique=True, null=False)
    comments = models.TextField(blank=True)

    class Meta:
        ordering = ['-init_date', 'name']
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            old_slug = Proj.objects.filter(slug=self.slug)
            while old_slug:
                self.slug = slugify(f'{self.name}-{randint(0, 10000)}')
                old_slug = Proj.objects.filter(slug=self.slug)
        return super().save(*args, **kwargs)
    

class Sys(models.Model):

    ip_address = models.CharField('IP Address', max_length=50, blank=True)
    fqdn = models.CharField('FQDN', max_length=50, blank=True)
    os = models.CharField('OS', max_length=50, blank=True)
    version = models.CharField(max_length=50, blank=True)
    comments = models.TextField(blank=True)
    proj = models.ForeignKey('Proj', on_delete=models.SET_NULL, null=True, blank=True)


    class Meta:
        ordering = ['ip_address', 'fqdn']

    def __str__(self):
        if self.fqdn:
            return '%s (%s)' % (self.ip_address, self.fqdn)
        else:
            return self.ip_address


class Vuln(models.Model):

    title = models.CharField(max_length=50)
    cve = models.CharField(max_length=20, null=True)
    score = models.FloatField()
    risk = models.IntegerField(choices=RISK, default=0)
    description = models.TextField(blank=True)
    evidence = models.TextField(blank=True)
    solution = models.TextField(blank=True)
    sys = models.ForeignKey('Sys', on_delete=models.SET_NULL, null=True, blank=True)
    port = models.ForeignKey('Port', on_delete=models.SET_NULL, null=True, blank=True)
    webapp = models.ForeignKey('WebApp', on_delete=models.SET_NULL, null=True, blank=True)
    webpage = models.ForeignKey('WebPage', on_delete=models.SET_NULL, null=True, blank=True)
    app = models.ForeignKey('App', on_delete=models.SET_NULL, null=True, blank=True)
    comments = models.TextField(blank=True)

    class Meta:
        ordering = ['-risk']

    def __str__(self):
        return self.title


class WebApp(models.Model):

    name = models.CharField(max_length=50)
    version = models.CharField(max_length=50, blank=True)
    programing_lang = models.CharField('Programing Language', max_length=50, blank=True)
    programing_framework = models.CharField(max_length=50, blank=True)
    root_url = models.CharField('Root URL', max_length=50)
    port = models.ForeignKey('Port', on_delete=models.SET_NULL, null=True, blank=True)
    comments = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class WebPage(models.Model):

    title = models.CharField(max_length=50, blank=True)
    path = models.CharField(max_length=50)
    webapp = models.ForeignKey('WebApp', on_delete=models.SET_NULL, null=True, blank=True)
    comments = models.TextField(blank=True)

    def __str__(self):
        if self.title:
            return self.title 
        else:
            return self.path