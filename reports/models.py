from django.db import models
from django.urls import reverse

from main.models import Proj

from phonenumber_field.modelfields import PhoneNumberField
from matplotlib.colors import CSS4_COLORS

class Report(models.Model):

    name = models.CharField(max_length=50, unique=True)
    media = models.FileField(upload_to='reports/', max_length=256)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    proj = models.ForeignKey('main.Proj', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.name


class ReportTemplate(models.Model):

    COVER_SECTION = (
        (0, 'cover'),
        (1, 'title'),
        (2, 'none'),
    )

    FONTS = (
        (0, 'AMATIC SC'),
        (1, 'Arial'),
        (2, 'Calibri'),
        (3, 'Cambria'),
        (4, 'Caveat'),
        (5, 'Comfortaa'),
        (6, 'Comics Sans MS'),
        (7, 'Consolas'),
        (8, 'Corsiva'),
        (9, 'Courier New'),
        (10, 'Droid Sans'),
        (11, 'Droid Serif'),
        (12, 'EB Garamond'),
        (13, 'Georgia'),
        (14, 'Impact'),
        (15, 'Lobster'),
        (16, 'Lora'),
        (17, 'Merri Weather'),
        (18, 'Monserrat'),
        (19, 'Noto Sans Symbols'),
        (20, 'Nunito'),
        (21, 'Oswald'),
        (22, 'Pacifico'),
        (23, 'Playfair Display'),
        (24, 'Roboto'),
        (25, 'Roboto Mono'),
        (26, 'Spectral'),
        (27, 'Syncopate'),
        (28, 'Times New Roman'),
        (29, 'Trebuchet MS'),
        (30, 'Ubuntu'),
        (31, 'Vardana'),
    )

    i = 0
    COLORS = []
    for color in CSS4_COLORS:
        COLORS.append((i, color))
        i = i + 1

    name = models.CharField(max_length=50)
    description = models.TextField()
    
    sec_cover = models.IntegerField('Cover', choices=COVER_SECTION, default=0)
    sec_toc = models.BooleanField('Table of Contents', default=True)
    sec_es = models.BooleanField('Executive Summary', default=True)
    sec_sor = models.BooleanField('Summary of Results', default=True)
    sec_method = models.BooleanField('Methodology', default=True)
    sec_find = models.BooleanField('Findings', default=True)
    sec_find_desc = models.BooleanField('Description', default=True)
    sec_find_evid = models.BooleanField('Evidence', default=True)
    sec_find_sol = models.BooleanField('Solution', default=True)
    sec_conc = models.BooleanField('Conclusion', default=True)

    cover_title = models.CharField('Title', max_length=50, blank=True)
    cover_company_name = models.CharField('Company Name', max_length=50, blank=True)
    cover_contact_name = models.CharField('Contact Name', max_length=50, blank=True)
    cover_contact_email = models.EmailField('Contact Email Address', max_length=254, blank=True)
    cover_contact_phone_number = PhoneNumberField('Contact Phone Number', blank=True)

    es_text = models.TextField('Executive Summary Text', blank=True)
    method_text = models.TextField('Methodology Text', blank=True)
    conc_text = models.TextField('Conclusion Text', blank=True)

    title_font = models.CharField(max_length=50, default='Droid Serif')
    title_size = models.IntegerField(default=26)
    title_bold = models.BooleanField(default=True)
    title_italic = models.BooleanField(default=False)
    title_color = models.IntegerField(choices=COLORS, default=37)

    heading_1_font = models.CharField(max_length=50, default='Droid Serif')
    heading_1_size = models.IntegerField(default=16)
    heading_1_bold = models.BooleanField(default=True)
    heading_1_italic = models.BooleanField(default=False)
    heading_1_color = models.IntegerField(choices=COLORS, default=37)

    heading_2_font = models.CharField(max_length=50, default='Droid Serif')
    heading_2_size = models.IntegerField(default=14)
    heading_2_bold = models.BooleanField(default=True)
    heading_2_italic = models.BooleanField(default=False)
    heading_2_color = models.IntegerField(choices=COLORS, default=37)

    heading_3_font = models.CharField(max_length=50, default='Droid Serif')
    heading_3_size = models.IntegerField(default=14)
    heading_3_bold = models.BooleanField(default=True)
    heading_3_italic = models.BooleanField(default=False)
    heading_3_color = models.IntegerField(choices=COLORS, default=37)

    normal_font = models.CharField(max_length=50, default='Roboto')
    normal_size = models.IntegerField(default=12)
    normal_bold = models.BooleanField(default=False)
    normal_italic = models.BooleanField(default=False)
    normal_color = models.IntegerField(choices=COLORS, default=7)

    caption_font = models.CharField(max_length=50, default='Roboto')
    caption_size = models.IntegerField(default=11)
    caption_bold = models.BooleanField(default=False)
    caption_italic = models.BooleanField(default=True)
    caption_color = models.IntegerField(choices=COLORS, default=7)

    risk_critical_color = models.IntegerField('Critical Color', choices=COLORS, default=45)
    risk_high_color = models.IntegerField('High Color', choices=COLORS, default=30)
    risk_medium_color = models.IntegerField('Medium Color', choices=COLORS, default=51)
    risk_low_color = models.IntegerField('Low Color', choices=COLORS, default=126)
    risk_info_color = models.IntegerField('Info Color', choices=COLORS, default=41)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name'] 
    