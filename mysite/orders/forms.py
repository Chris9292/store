from django import forms
import pandas as pd
from .models import Product

df = pd.DataFrame(Product.objects.all().values())
df.set_index("id", inplace=True)

distinct_colors = df["color"].dropna().unique()
distinct_mentese_type = df[df["group"] == 11]["type"].dropna().unique()
distinct_spanoleta_type = df[df["group"] == 4]["type"].dropna().unique()

#print(distinct_colors)
#print(distinct_mentese_type)
#print(distinct_spanoleta_type)

choices_colors = [(color, color) for color in distinct_colors]
choices_mentese_type = [(_type, _type) for _type in distinct_mentese_type]
choices_spanoleta_type = [(_type, _type) for _type in distinct_spanoleta_type]
choices_direction = [(_type, _type) for _type in ["left", "right"]]

print(choices_colors)
print(choices_mentese_type)
print(choices_spanoleta_type)

class OrderForm(forms.Form):
    amount = forms.IntegerField(initial=1)
    height = forms.IntegerField()
    width = forms.IntegerField()
    direction = forms.ChoiceField(choices=choices_direction)
    color = forms.ChoiceField(choices=choices_colors)
    type_men = forms.ChoiceField(choices=choices_mentese_type)
    type_span = forms.ChoiceField(choices=choices_spanoleta_type)
    anaklisi = forms.BooleanField(required=False)
