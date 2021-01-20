from django import forms

class inputForm (forms.Form):
    cacheAccessTime = forms.NumberInput()
    memAccessTime = forms.NumberInput()
    sets = forms.NumberInput()
    blockPerSet = forms.NumberInput()
    wordsPerBlock = forms.NumberInput()
    numbers = forms.Textarea()