from django import forms


class InputForm(forms.Form):
    input = forms.CharField(widget=forms.Textarea, label="", required=False)

