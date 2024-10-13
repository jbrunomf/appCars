from django import forms

from app.models import Brand, Car


class CarForm(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(queryset=Brand.objects.all(), empty_label='Selecione a Marca')
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10, required=False)
    value = forms.FloatField()
    photo = forms.ImageField()

    def save(self):
        car = Car(
            model=self.cleaned_data['model'],
            brand=self.cleaned_data['brand'],
            factory_year=self.cleaned_data['factory_year'],
            model_year=self.cleaned_data['model_year'],
            plate=self.cleaned_data['plate'],
            value=self.cleaned_data['value'],
            photo=self.cleaned_data['photo']
        )
        car.save()
        return car

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = (
            'model',
            'brand',
            'factory_year',
            'model_year',
            'plate',
            'value',
            'photo'
        )

    def clean_model(self):
        model = self.cleaned_data['model']
        return model.upper()

    def clean_value(self):
        value = self.cleaned_data['value']

        if value < 5000:
            self.add_error('value', 'Vehicle price below the minimum value')
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data['factory_year']
        if factory_year < 1950:
            self.add_error('factory_year', 'Vehicle factory year below the minimum value')
        return factory_year