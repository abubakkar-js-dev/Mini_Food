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

    features = [
        {'icon': """<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
        <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 18.75a1.5 1.5 0 0 1-3 0m3 0a1.5 1.5 0 0 0-3 0m3 0h6m-9 0H3.375a1.125 1.125 0 0 1-1.125-1.125V14.25m17.25 4.5a1.5 1.5 0 0 1-3 0m3 0a1.5 1.5 0 0 0-3 0m3 0h1.125c.621 0 1.129-.504 1.09-1.124a17.902 17.902 0 0 0-3.213-9.193 2.056 2.056 0 0 0-1.58-.86H14.25M16.5 18.75h-2.25m0-11.177v-.958c0-.568-.422-1.048-.987-1.106a48.554 48.554 0 0 0-10.026 0 1.106 1.106 0 0 0-.987 1.106v7.635m12-6.677v6.677m0 4.5v-4.5m0 0h-12" />
        </svg>""", 
        'title': 'Fast Delivery', 'desc': 'Hot meals at your door in 30 minutes or free.'},
        {'icon': """<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
        <path stroke-linecap="round" stroke-linejoin="round" d="M9.813 15.904 9 18.75l-.813-2.846a4.5 4.5 0 0 0-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 0 0 3.09-3.09L9 5.25l.813 2.846a4.5 4.5 0 0 0 3.09 3.09L15.75 12l-2.846.813a4.5 4.5 0 0 0-3.09 3.09ZM18.259 8.715 18 9.75l-.259-1.035a3.375 3.375 0 0 0-2.455-2.456L14.25 6l1.036-.259a3.375 3.375 0 0 0 2.455-2.456L18 2.25l.259 1.035a3.375 3.375 0 0 0 2.456 2.456L21.75 6l-1.035.259a3.375 3.375 0 0 0-2.456 2.456ZM16.894 20.567 16.5 21.75l-.394-1.183a2.25 2.25 0 0 0-1.423-1.423L13.5 18.75l1.183-.394a2.25 2.25 0 0 0 1.423-1.423l.394-1.183.394 1.183a2.25 2.25 0 0 0 1.423 1.423l1.183.394-1.183.394a2.25 2.25 0 0 0-1.423 1.423Z" />
        </svg>""",
     'title': 'Fresh Ingredients', 'desc': 'Locally sourced, organic produce every day.'},
        {'icon': """<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
        <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6h4.5m4.5 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
        </svg>""", 'title': 'Easy Ordering', 'desc': 'Order in seconds with our seamless experience.'},
        {'icon': """<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
        <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z" />
        </svg>""", 
     'title': 'Made with Love', 'desc': 'Chef-crafted recipes bursting with flavor.'},
    ]

    testimonials=[
            {
            'name': 'Sarah M.',
            'text': 'The burger was insanely good! Best delivery food I\'ve ever had. Arrived hot and fresh.',
            'rating': 5,
            'avatar': '🧑‍🦰',
            },
            {
            'name': 'James R.',
            'text': 'Poke bowl was fresh and flavorful. Love the quick delivery — will definitely order again!',
            'rating': 5,
            'avatar': '👨‍💼',
            },
            {
            'name': 'Emily K.',
            'text': 'That lava cake is pure heaven. Perfect portion sizes and amazing value for money.',
            'rating': 5,
            'avatar': '👩‍🎨',
            },
    ]
    return render(req, 'core/home.html', context={'menuItems': menuItems, 'features': features, 'testimonials': testimonials})
