from django.shortcuts import render

# Create your views here.

def home(req):
    menuItems = [
        {'name': 'Classic Burger', 'price': '$12.99', 'rating': 4.9, 'image': 'core/images/hero-food.jpg', 'tag': 'Bestseller'},
        {'name': 'Pepperoni Pizza', 'price': '$14.99', 'rating': 4.8, 'image': 'core/images/food-pizza.jpg', 'tag': 'Popular'},
        {'name': 'Salmon Poke Bowl', 'price': '$16.99', 'rating': 4.7, 'image': 'core/images/food-bowl.jpg', 'tag': None},
        {'name': 'Crispy Chicken', 'price': '$11.99', 'rating': 4.6, 'image': 'core/images/food-chicken.jpg', 'tag': 'New'},
        {'name': 'Garden Salad', 'price': '$9.99', 'rating': 4.5, 'image': 'core/images/food-salad.jpg', 'tag': None},
        {'name': 'Lava Cake', 'price': '$8.99', 'rating': 4.9, 'image': 'core/images/food-dessert.jpg', 'tag': 'Must Try'},
    ]
    return render(req, 'core/home.html',context={'menuItems': menuItems})
