from django import forms


class TextField(forms.Form):
    color = (
        ('yellow', 'Желтый'),
        ('red', 'Красный'),
        ('blue', 'Синий'),
        ('black', 'Черный'),
        ('white', 'Белый'),
    )
    font = (
        ('Arial', 'Arial'),
        ('Calibri', 'Calibri'),
        ('Candara', 'Candara'),
        ('Georgia', 'Georgia'),
        ('Times-New-Roman', 'Times New Roman'),
    )

    text = forms.CharField(label="Текст бегущей строки",)
    color = forms.ChoiceField(choices=color, label="Цвет")
    font = forms.ChoiceField(choices=font, label='Шрифт')
