from django.shortcuts import render

from .models import Restaurant, MenuItem, MenuCategory


def fat_locations(request):
    restaurants = Restaurant.objects.all()
    context = {"x": restaurants}

    return render(request, "restaurants.html", context)


def res_cat(request, restaurant_id):
    context = {}
    restaurant = Restaurant.objects.get(id=restaurant_id)
    categories = MenuCategory.objects.filter(res=restaurant)

    context["restaurant"] = restaurant
    context["categories"] = categories

    # context{"restaurant":restaurant, "categories":categories}
    return render(request, "categories.html", context)


def items(request, cat_id):
    context = {}

    category = MenuCategory.objects.get(id=cat_id)
    foods = MenuItem.objects.filter(cat=category)

    context["foods"] = foods
    return render(request, "items.html", context)
