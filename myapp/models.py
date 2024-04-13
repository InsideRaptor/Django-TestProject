from django.db import models
from django import forms

class FirstCat(models.Model):
    catId = models.AutoField(primary_key=True)
    catName = models.CharField(max_length=100)

    def __str__(self):
        return str(self.catId)
    
    class Meta:
        app_label = 'myapp'

class SecondCat(models.Model):
    subcatId = models.AutoField(primary_key=True)
    cat = models.ForeignKey(FirstCat, on_delete=models.CASCADE)
    subcatName = models.CharField(max_length=100)

    def __str__(self):
        return str(self.subcatId)
    
    class Meta:
        app_label = 'myapp'

class Adds(models.Model):
    listingId = models.AutoField(primary_key=True)
    subcat = models.ForeignKey(SecondCat, on_delete=models.CASCADE)
    listingName = models.CharField(max_length=100)

    def __str__(self):
        return str(self.listingId)
    
    class Meta:
        app_label = 'myapp'

class FirstCatForm(forms.ModelForm):
    catName = forms.CharField(label='Category name')
    class Meta:
        model = FirstCat
        fields = ['catName']

class SecondCatForm(forms.ModelForm):
    cat = forms.ModelChoiceField(
        queryset=FirstCat.objects.all(),
        label='Category ID',
        to_field_name='catId'
    )
    subcatName = forms.CharField(label='Subcategory name')
    class Meta:
        model = SecondCat
        fields = ['cat', 'subcatName']

class AddsForm(forms.ModelForm):
    subcat = forms.ModelChoiceField(
        queryset=SecondCat.objects.all(),
        label='Subcategory ID',
        to_field_name='subcatId'
    )
    listingName = forms.CharField(label='Listing name')
    class Meta:
        model = Adds
        fields = ['subcat', 'listingName']