from django import forms

class ProdcutoFormulario(forms.Form):
    Producto = forms.CharField(max_length=50)

    Descripcion = forms.CharField(max_length=200, widget=forms.TextInput({}))
    
    Precio = forms.IntegerField()
    
    
class ProductoBusquedaFormulario(forms.Form):
    Producto = forms.CharField(max_length=50, required=False)