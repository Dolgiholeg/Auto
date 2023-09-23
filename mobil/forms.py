from django import forms

class Avtomotor(forms.Form):
    marka1 = forms.CharField(label='Марка', max_length=20)
    zavod1 = forms.CharField(label='Производитель',max_length=20)
    yaer1 = forms.IntegerField(label='Возраст',max_value=120, min_value=1)
    nomer1 = forms.CharField(label='Гос.номер',max_length=9)