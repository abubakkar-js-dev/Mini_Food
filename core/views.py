from django.shortcuts import render

# Create your views here.

def home(req):
    menuItems = [
        {'name': 'Classic Burger', 'price': '$12.99', 'rating': 4.9, 'image': 'heroImg', 'tag': 'Bestseller'},
        {'name': 'Pepperoni Pizza', 'price': '$14.99', 'rating': 4.8, 'image': 'pizzaImg', 'tag': 'Popular'},
        {'name': 'Salmon Poke Bowl', 'price': '$16.99', 'rating': 4.7, 'image': 'bowlImg', 'tag': None},
        {'name': 'Crispy Chicken', 'price': '$11.99', 'rating': 4.6, 'image': 'chickenImg', 'tag': 'New'},
        {'name': 'Garden Salad', 'price': '$9.99', 'rating': 4.5, 'image': 'saladImg', 'tag': None},
        {'name': 'Lava Cake', 'price': '$8.99', 'rating': 4.9, 'image': 'dessertImg', 'tag': 'Must Try'},
    ]
    return render(req, 'core/home.html',context={'menuItems': menuItems})
