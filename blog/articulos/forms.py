from django import forms
from articulos import models

class NewPost_form(forms.ModelForm):
    class Meta:
        model = models.Publicacion
        fields = ['titulo', 'texto', 'tipo']

    tipo = models.Tipo.objects.all()
    titulo = forms.CharField(max_length=100)
    texto = forms.CharField(label='Articulo', widget=forms.Textarea(attrs={'id': '_editor',}))
    tipo = forms.ModelChoiceField(label='Tipo', queryset = tipo)

class NewPortfolio_form(forms.ModelForm):
    class Meta:
        model = models.Portfolio
        fields = ['title', 'description', 'url', 'img']

    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea(attrs={'id':'_editor',}))
    url = forms.URLField()
    img = forms.FileField()

class Media_Form(forms.ModelForm):
    class Meta:
        model = models.Media
        fields = ['file']