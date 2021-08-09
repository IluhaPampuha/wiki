from django.forms import ModelForm
from .models import Company, Messages


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name']
        labels = {'name': 'Название компании'}


class IncomingForm(ModelForm):
    class Meta:
        model = Messages
        fields = ['id_company', 'incoming_number', 'incoming_date', 'number_sign', 'date_sign', 'information']
        labels = {'incoming_number': 'Входящий номер', 'incoming_date': 'Дата входящего',
                  'number_sign': 'Подписной номер', 'date_sign': 'Дата подписи', 'information': 'Информация'}


class OutgoingForm(ModelForm):
    class Meta:
        model = Messages
        fields = ['id_company', 'outgoing_number', 'outgoing_date', 'information']
        labels = {'outgoing_number': 'Исходящий номер', 'outgoing_date': 'Дата исходящего', 'information': 'Информация'}
