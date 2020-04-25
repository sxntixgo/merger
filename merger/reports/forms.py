from django.forms import ModelForm, CheckboxInput, RadioSelect

from .models import ReportTemplate

class ReportTemplateForm(ModelForm):
    
    class Meta:
        model = ReportTemplate
        fields = [
            'name', 'description', 'sec_cover', 'cover_title', 'cover_company_name', 'cover_contact_name', 'cover_contact_email', 'cover_contact_phone_number',
            'sec_toc', 'sec_es', 'es_text', 'sec_sor', 'sec_method', 'sec_method', 'method_text', 'sec_find', 'sec_find_desc', 'sec_find_evid', 
            'sec_find_sol', 'sec_conc', 'conc_text', 'title_font', 'title_size', 'title_bold', 'title_italic', 'title_color', 'heading_1_font', 
            'heading_1_size', 'heading_1_bold', 'heading_1_italic', 'heading_1_color', 'heading_2_font', 'heading_2_size', 'heading_2_bold', 
            'heading_2_italic', 'heading_2_color', 'heading_3_font', 'heading_3_size', 'heading_3_bold', 'heading_3_italic', 'heading_3_color', 
            'normal_font', 'normal_size', 'normal_bold', 'normal_italic', 'normal_color', 'caption_font', 'caption_size', 'caption_bold', 
            'caption_italic', 'caption_color', 'risk_critical_color', 'risk_high_color', 'risk_medium_color', 'risk_low_color','risk_info_color'
        ]

        labels = {
            'sec_cover': 'Cover',
            'sec_toc': 'Table of Contents',
            'sec_es': 'Executive Summary',
            'sec_sor': 'Summary of Results',
            'sec_method': 'Methodology',
            'sec_find': 'Findings',
            'sec_find_desc': 'Description',
            'sec_find_evid': 'Evidence',
            'sec_find_sol': 'Solution',
            'sec_conc': 'Conclusion',

            'cover_title': 'Title',
            'cover_company_name': 'Company Name',
            'cover_contact_name': 'Contact Name',
            'cover_contact_email': 'Contact Email Address',
            'cover_contact_phone_number': 'Contact Phone Number',
        
            'es_text': 'Executive Summary Text',
            'method_text': 'Methodology Text',
            'conc_text': 'Conclusion Text',

            'risk_critical_color': 'Critical Color',
            'risk_high_color': 'High Color',
            'risk_medium_color': 'Medium Color',
            'risk_low_color': 'Low Color',
            'risk_info_color': 'Info Color',
        }

        widgets = {
            'sec_cover': RadioSelect(attrs={'onclick' : "coverSelected();",}),
            'sec_es': CheckboxInput(attrs={'onclick' : "esClicked();",}),
            'sec_method': CheckboxInput(attrs={'onclick' : "methodClicked();",}),
            'sec_conc': CheckboxInput(attrs={'onclick' : "concClicked();",}),
        }