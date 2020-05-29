from django.forms import ModelForm, CheckboxInput, RadioSelect

from .models import ReportTemplate

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, HTML, Layout, Field, Submit

class ReportTemplateForm(ModelForm):
    
    class Meta:
        model = ReportTemplate
        fields = '__all__'

        widgets = {
            'sec_cover': RadioSelect(attrs={'onclick' : "coverSelected();",}),
            'sec_es': CheckboxInput(attrs={'onclick' : "esClicked();",}),
            'sec_method': CheckboxInput(attrs={'onclick' : "methodClicked();",}),
            'sec_conc': CheckboxInput(attrs={'onclick' : "concClicked();",}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div('name', css_class='col-sm-6'),
                Div(Field('description', style='height: 38px;'), css_class='col-sm-6'),
                css_class='row',
            ),
            Div(Div(HTML('<h3>Cover Type Options</h3>'), css_class='col-sm-12'),
                css_class='row',
            ),
            Div(
                Div('sec_cover', css_class='col-sm-3',),
                Div('cover_title', 'cover_company_name', css_class='col-sm-3'),
                Div('cover_contact_name', 'cover_contact_email', css_class='col-sm-3'), 
                Div('cover_contact_phone_number', css_class='col-sm-3'), 
                css_class='row',
            ),
            Div(
                Div(HTML('<h3>Section Options</h3>'), css_class='col-sm-12'),
                css_class='row',
            ),
            Div(
                Div('sec_toc', 'sec_es', 'sec_sor', 'sec_method', 'sec_method', 'sec_find', 
                    Div(Div(css_class='col-sm-1'), Div('sec_find_desc', 'sec_find_evid', 'sec_find_sol'), css_class='row'), 
                    'sec_conc', css_class='col-sm-3',),
                Div(Field('es_text', rows='3'), Field('method_text', rows='3'), Field('conc_text', rows='3'), css_class='col-sm-9'),
                css_class='row', 
            ),
            Div(
                Div(HTML('<h3>Heading Options</h3>'), css_class='col-sm-12'),
                css_class='row',
            ),
            Div(
                Div('title_font', css_class='col-sm-3'),
                Div('title_size', css_class='col-sm-2'),
                Div('title_bold', css_class='col-sm-2'),
                Div('title_italic', css_class='col-sm-2'),
                Div('title_color', css_class='col-sm-3'),
                css_class='row', 
            ),
            Div(
                Div('heading_1_font', css_class='col-sm-3'),
                Div('heading_1_size', css_class='col-sm-2'),
                Div('heading_1_bold', css_class='col-sm-2'),
                Div('heading_1_italic', css_class='col-sm-2'),
                Div('heading_1_color', css_class='col-sm-3'),
                css_class='row', 
            ),
            Div(
                Div('heading_2_font', css_class='col-sm-3'),
                Div('heading_2_size', css_class='col-sm-2'),
                Div('heading_2_bold', css_class='col-sm-2'),
                Div('heading_2_italic', css_class='col-sm-2'),
                Div('heading_2_color', css_class='col-sm-3'),
                css_class='row', 
            ),
            Div(
                Div('heading_3_font', css_class='col-sm-3'),
                Div('heading_3_size', css_class='col-sm-2'),
                Div('heading_3_bold', css_class='col-sm-2'),
                Div('heading_3_italic', css_class='col-sm-2'),
                Div('heading_3_color', css_class='col-sm-3'),
                css_class='row', 
            ),
            Div(
                Div('normal_font', css_class='col-sm-3'),
                Div('normal_size', css_class='col-sm-2'),
                Div('normal_bold', css_class='col-sm-2'),
                Div('normal_italic', css_class='col-sm-2'),
                Div('normal_color', css_class='col-sm-3'),
                css_class='row', 
            ),
            Div(
                Div('caption_font', css_class='col-sm-3'),
                Div('caption_size', css_class='col-sm-2'),
                Div('caption_bold', css_class='col-sm-2'),
                Div('caption_italic', css_class='col-sm-2'),
                Div('caption_color', css_class='col-sm-3'),
                css_class='row', 
            ),
            Div(
                Div(HTML('<h3>Risk Options</h3>'), css_class='col-sm-12'),
                css_class='row',
            ),
            Div(
                Div('risk_critical_color', css_class='col-sm-2'),
                Div('risk_high_color', css_class='col-sm-2'),
                Div('risk_medium_color', css_class='col-sm-2'),
                Div('risk_low_color', css_class='col-sm-2'),
                Div('risk_info_color', css_class='col-sm-2'),
                css_class='row', 
            ),
                Submit('save', 'Submit', css_class='btn-success'),
                HTML('<a name="cancel" class="btn btn-danger" id="button-id-cancel" href="{{ view.success_url }}">Cancel</a>'), 
        )