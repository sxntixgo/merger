from django.db import models
from django.urls import reverse

from phonenumber_field.modelfields import PhoneNumberField


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
    sys = models.ForeignKey('Sys', on_delete=models.SET_NULL, null=True)
    comments = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('app_detail', kwargs={'pk': self.pk})


class Attach(models.Model):

    media = models.FileField(upload_to='uploads/', max_length=256)
    name = models.CharField(max_length=50)
    caption = models.CharField(max_length=200, blank=True)
    vuln = models.ForeignKey('Vuln', on_delete=models.SET_NULL, null=True, blank=True)
    webpage = models.ForeignKey('WebPage', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('attach_detail', kwargs={'pk': self.pk})


class Domain(models.Model):
    domain = models.CharField(max_length=50)
    proj = models.ForeignKey('Proj', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.domain

    def get_absolute_url(self):
        return reverse('domain_detail', kwargs={'pk': self.pk})


class NetAddr(models.Model):

    net_address = models.CharField('Network Address', max_length=50)
    proj = models.ForeignKey('Proj', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.net_address

    def get_absolute_url(self):
        return reverse('netaddress_detail', kwargs={'pk': self.pk})


class Poc(models.Model):

    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    phone = PhoneNumberField('Phone Number', blank=True)
    proj = models.ForeignKey('Proj', on_delete=models.SET_NULL, null=True, blank=True)
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('poc_detail', kwargs={'pk': self.pk})


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
    sys = models.ForeignKey('Sys', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['protocol', 'number']

    def __str__(self):

        return_text = '%s/%i' % (self.get_protocol_text(), self.number)
        if self.is_web_app:
            return_text = f'{return_text} (Webapp)'
        return return_text

    def get_absolute_url(self):
        return reverse('port_detail', kwargs={'pk': self.pk})

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
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('proj_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-init_date', 'name']


class Sys(models.Model):

    ip_address = models.CharField('IP Address', max_length=50, blank=True)
    fqdn = models.CharField('FQDN', max_length=50, blank=True)
    os = models.CharField('OS', max_length=50, blank=True)
    version = models.CharField(max_length=50, blank=True)
    comments = models.TextField(blank=True)
    proj = models.ForeignKey('Proj', on_delete=models.SET_NULL, null=True)


    class Meta:
        ordering = ['ip_address', 'fqdn']

    def __str__(self):
        return '%s (%s)' % (self.ip_address, self.fqdn)

    def get_absolute_url(self):
        return reverse('sys_detail', kwargs={'pk': self.pk})


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
    proj = models.ForeignKey('Proj', on_delete=models.SET_NULL, null=True, blank=True)
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('vuln_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-risk']


class WebApp(models.Model):

    name = models.CharField(max_length=50)
    version = models.CharField(max_length=50, blank=True)
    programing_lang = models.CharField('programing_language', max_length=50, blank=True)
    programing_framework = models.CharField(max_length=50, blank=True)
    root_url = models.CharField('Root URL', max_length=50)
    port = models.ForeignKey('Port', on_delete=models.SET_NULL, null=True)
    comments = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('webapp_detail', kwargs={'pk': self.pk})


class WebPage(models.Model):

    title = models.CharField(max_length=50, blank=True)
    path = models.CharField(max_length=50)
    webapp = models.ForeignKey('WebApp', on_delete=models.SET_NULL, null=True)
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.title if self.title else self.path

    def get_absolute_url(self):
        return reverse('webpage_detail', kwargs={'pk': self.pk})