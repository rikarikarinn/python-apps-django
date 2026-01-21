from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'stock']  # 名前と初期在庫
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
        }

# --- 入庫用フォーム ---
class StockForm(forms.Form):
    quantity = forms.IntegerField(
        label="入庫数",
        min_value=1,
        widget=forms.NumberInput(attrs={'placeholder': '数量を入力', 'class': 'form-control'})
    )


class StockOutForm(forms.Form):
    quantity = forms.IntegerField(
        label="出庫数",
        min_value=1,
        widget=forms.NumberInput(attrs={'placeholder': '数量を入力', 'class': 'form-control'})
    )
