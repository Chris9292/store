from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .forms import OrderForm
from .models import Product
import pandas as pd

df = pd.DataFrame(Product.objects.all().values())

#print(df)
def index(request):


    form = OrderForm()
    if request.method == "POST":
        
        form = OrderForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

            # isStandard
            isStandard_df = df[df["isStandard"] == True]
            
            #print(df.columns)
            #df[(df["dimensionMin"] < form.cleaned_data["height"]) & (df["dimensionMax"] > form.cleaned_data["height"])][["code", "factoryCode", "description"]])

            # width
            # if anaklisi --> tyflo
            if form.cleaned_data["anaklisi"]:
                width_df = df[df["code"]=="365-358"]
            else:
                width_df = df[(df["dimensionMin"] <= form.cleaned_data["width"]) & (df["dimensionMax"] >= form.cleaned_data["width"]) & (df["group"]==1)]
            
            # height
            height_df = df[(df["group"] == 4) & (df["dimensionMin"] <= form.cleaned_data["height"]) & (df["dimensionMax"] >= form.cleaned_data["height"]) & (df["type"] == form.cleaned_data["type_span"])]
            print(height_df)
            #frames = [isStandard_df, height_df]
            #print(pd.concat[frames])

            # color TBD
            color_df = df[df["color"] == form.cleaned_data["color"]]

            # xerouli
            xerouli_df = df[(df["group"] == 9) & (df["color"]==form.cleaned_data["color"])]



            final_df = pd.concat([isStandard_df, width_df, color_df, height_df, xerouli_df])
            final_df["amount"] = form.cleaned_data["amount"]
            return HttpResponse(final_df.to_html())

        

    context = {"form": form}

    return render(request, template_name="index.html", context=context)
