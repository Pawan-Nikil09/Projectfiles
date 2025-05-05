from flask import Flask, render_template, url_for, request, redirect, flash
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your_secure_random_key')  # Use environment variable for security

# Centralized data generation function
def get_sample_data():
    """Generate sample data for the application."""
    nav_items = [
        {'name': 'Home', 'url': '', 'dropdown': False},
        {
            'name': 'Shop', 'url': 'shop', 'dropdown': True, 'mega_menu': True,
            'categories': [
                {'name': 'Rings', 'subitems': ['Engagement', 'Gold rings', 'Casual rings', 'Silver rings', 'Platinum rings', 'Diamond rings']},
                {'name': 'Earrings', 'subitems': ['Jhumkas', 'Barbells', 'Hug hoops', 'Tear drop', 'Suidhaga', 'Gemstone']},
                {'name': 'Necklaces', 'subitems': ['Bib necklece', 'Collar necklece', 'Rope necklece', 'Locket necklece', 'Chain necklece', 'Opera nacklece']},
                {'name': 'Pendants', 'subitems': ['Alphabet', 'Mangalsutra', 'Religious', 'Diamond', 'Heart shaped', 'Gemstone']},
                {'name': 'Breslet', 'subitems': ['Caratlane chain', 'Oval bracelets', 'Pearl bracelets', 'Charm bracelets', 'Silver brcelets', 'Tennis bracelets']}
            ],
            'banners': [
                {'url': 'shop', 'image': 'https://placehold.co/580x160', 'alt': 'Shop Banner 1'},
                {'url': 'shop', 'image': 'https://placehold.co/580x160', 'alt': 'Shop Banner 2'}
            ]
        },
        {
            'name': 'Categories', 'url': 'categories', 'dropdown': True, 'categories_grid': True,
            'grid_categories': [
                {'name': 'Rings', 'image': 'https://placehold.co/190x140'},
                {'name': 'Bracelet', 'image': 'https://placehold.co/190x140'},
                {'name': 'Earrings', 'image': 'https://placehold.co/190x140'},
                {'name': 'Necklace', 'image': 'https://placehold.co/190x140'},
                {'name': 'Pendants', 'image': 'https://placehold.co/190x140'},
                {'name': 'Watches', 'image': 'https://placehold.co/190x140'},
                {'name': 'Necklace', 'image': 'https://placehold.co/190x140'},
                {'name': 'Chain', 'image': 'https://placehold.co/190x140'}
            ],
            'featured_image': 'https://placehold.co/290x380'
        },
        {
            'name': 'Pages', 'url': 'javascript:void(0);', 'dropdown': True,
            'subitems': [
                {'name': 'About', 'url': 'about'},
                {'name': 'Faq', 'url': 'faq'},
                {'name': 'Wishlist', 'url': 'wishlist'},
                {'name': 'Account', 'url': 'account'},
                {'name': 'Cart', 'url': 'cart'},
                {'name': 'Checkout', 'url': 'checkout'}
            ]
        },
        {'name': 'Blog', 'url': 'blog', 'dropdown': False},
        {'name': 'Contact', 'url': 'contact', 'dropdown': False}
    ]

    account_items = [
        {'name': 'Wishlist', 'url': 'wishlist'},
        {'name': 'Order history', 'url': 'order_history'},
        {'name': 'Account details', 'url': 'account_details'},
        {'name': 'Customer support', 'url': 'customer_support'},
        {'name': 'Logout', 'url': 'logout'}
    ]

    cart_items = [
        {'id': 1, 'name': 'Delica Omtantur', 'price': 100.00, 'image': 'https://placehold.co/600x765'},
        {'id': 2, 'name': 'Gianvito Rossi', 'price': 99.99, 'image': 'https://placehold.co/600x765'}
    ]

    slider_slides = [
        {
            'title': 'New arrival', 'subtitle': 'classic jewellery',
            'background_image': 'https://placehold.co/2000x2000',
            'product_image': 'https://placehold.co/2000x2000',
            'button_text': 'Shop this collection'
        }
    ] * 3

    features = [
        {'icon': 'ti-truck', 'title': 'Free shipping', 'description': 'On order over $199'},
        {'icon': 'ti-headphone', 'title': 'Online support', 'description': 'Customer service'},
        {'icon': 'ti-reload', 'title': '30 Days return', 'description': 'If goods have problems'},
        {'icon': 'ti-credit-card', 'title': 'Secure payment', 'description': '100% secure payment'}
    ]

    shop_categories = [
        {'name': 'Earrings', 'image': 'https://placehold.co/600x1003'},
        {'name': 'Rings', 'image': 'https://placehold.co/600x477'},
        {'name': 'Necklace', 'image': 'https://placehold.co/600x1003'},
        {'name': 'Bracelet', 'image': 'https://placehold.co/600x477'}
    ]

    product_tabs = [
        {
            'id': 'tab_five1', 'name': 'New arrivals',
            'products': [
                {'id': 1, 'name': 'Diamond earrings', 'price': 189.00, 'old_price': 200.00, 'image': 'https://placehold.co/600x765', 'label': 'New'},
                {'id': 2, 'name': 'Geometric gold ring', 'price': 159.00, 'old_price': 180.00, 'image': 'https://placehold.co/600x765'},
                {'id': 3, 'name': 'Gemstone earrings', 'price': 189.00, 'old_price': 200.00, 'image': 'https://placehold.co/600x765', 'label': 'Hot'},
                {'id': 4, 'name': 'Gold diamond ring', 'price': 289.00, 'old_price': None, 'image': 'https://placehold.co/600x765'}
            ]
        },
        {
            'id': 'tab_five2', 'name': 'Best sellers',
            'products': [
                {'id': 9, 'name': 'Geometric gold ring', 'price': 239.00, 'old_price': 250.00, 'image': 'https://placehold.co/600x765', 'label': 'Hot'},
                {'id': 10, 'name': 'Suserrer earring', 'price': 189.00, 'old_price': 200.00, 'image': 'https://placehold.co/600x765', 'label': 'Hot'},
                {'id': 11, 'name': 'The aphrodite band', 'price': 150.00, 'old_price': 200.00, 'image': 'https://placehold.co/600x765'},
                {'id': 12, 'name': 'Diamond earrings', 'price': 89.00, 'old_price': 100.00, 'image': 'https://placehold.co/600x765'}
            ]
        },
        {
            'id': 'tab_five3', 'name': 'Featured products',
            'products': [
                {'id': 13, 'name': 'Gold diamond ring', 'price': 289.00, 'old_price': None, 'image': 'https://placehold.co/600x765'},
                {'id': 14, 'name': 'Diamond earrings', 'price': 189.00, 'old_price': 200.00, 'image': 'https://placehold.co/600x765'},
                {'id': 15, 'name': 'Geometric gold ring', 'price': 129.00, 'old_price': 150.00, 'image': 'https://placehold.co/600x765', 'label': 'New'},
                {'id': 16, 'name': 'Diamond earrings', 'price': 168.00, 'old_price': 220.00, 'image': 'https://placehold.co/600x765', 'label': 'New'}
            ]
        }
    ]

    footer_columns = [
        {
            'title': 'Categories',
            'links': [
                {'name': 'Women collection', 'url': 'shop'},
                {'name': 'Men collection', 'url': 'shop'},
                {'name': 'Accessories', 'url': 'shop'},
                {'name': 'Diamond', 'url': 'shop'},
                {'name': 'Gold jewellery', 'url': 'shop'}
            ]
        },
        {
            'title': 'Account',
            'links': [
                {'name': 'My profile', 'url': 'profile'},
                {'name': 'My order history', 'url': 'order_history'},
                {'name': 'My wish list', 'url': 'wishlist'},
                {'name': 'Order tracking', 'url': 'order_tracking'},
                {'name': 'Shopping cart', 'url': 'cart'}
            ]
        },
        {
            'title': 'Information',
            'links': [
                {'name': 'About us', 'url': 'about'},
                {'name': 'Careers', 'url': 'careers'},
                {'name': 'Events', 'url': 'events'},
                {'name': 'Articles', 'url': 'articles'},
                {'name': 'Contact us', 'url': 'contact'}
            ]
        }
    ]

    social_links = [
        {'name': 'Facebook', 'icon': 'facebook-f', 'url': 'https://www.facebook.com/'},
        {'name': 'Instagram', 'icon': 'instagram', 'url': 'http://www.instagram.com'},
        {'name': 'Twitter', 'icon': 'twitter', 'url': 'http://www.twitter.com'},
        {'name': 'Dribbble', 'icon': 'dribbble', 'url': 'http://www.dribbble.com'}
    ]

    policy_links = [
        {'name': 'Terms and conditions', 'url': 'terms'},
        {'name': 'Privacy policy', 'url': 'privacy'}
    ]

    instagram = [
        {'image': 'https://placehold.co/445x445', 'link': 'https://www.instagram.com'},
        {'image': 'https://placehold.co/445x445', 'link': 'https://www.instagram.com'},
        {'image': 'https://placehold.co/445x445', 'link': 'https://www.instagram.com'},
        {'image': 'https://placehold.co/445x445', 'link': 'https://www.instagram.com'},
        {'image': 'https://placehold.co/445x445', 'link': 'https://www.instagram.com'},
        {'image': 'https://placehold.co/445x445', 'link': 'https://www.instagram.com'}
    ]

    return {
        'nav_items': nav_items,
        'account_items': account_items,
        'cart_items': cart_items,
        'cart_total': sum(item['price'] for item in cart_items),
        'slider_slides': slider_slides,
        'features': features,
        'shop_categories': shop_categories,
        'product_tabs': product_tabs,
        'footer_columns': footer_columns,
        'social_links': social_links,
        'policy_links': policy_links,
        'instagram': instagram,
        'current_year': datetime.now().year,
        'show_cookie_message': True,
        'show_subscription_popup': True,
        'subscription_popup_image': 'https://placehold.co/600x660',
        'site_title': 'Crafto - Jewelry Store',
        'site_description': 'Elegant jewelry store with a wide collection of rings, earrings, necklaces, and bracelets.'
    }

# Helper function for static URLs
def get_static_url(filename):
    """Generate static URLs for assets."""
    return f"/static/{filename}"

# Common data for all routes
def get_common_data():
    """Return common data for all routes."""
    data = get_sample_data()
    data['static_url'] = get_static_url
    data['payment_methods'] = [
        {'name': 'Visa', 'image': 'images/visa.svg', 'url': '#'},
        {'name': 'Mastercard', 'image': 'images/mastercard.svg', 'url': '#'},
        {'name': 'American Express', 'image': 'images/american-express.svg', 'url': '#'},
        {'name': 'Discover', 'image': 'images/discover.svg', 'url': '#'},
        {'name': 'Diners Club', 'image': 'images/diners-club.svg', 'url': '#'}
    ]
    return data

# Routes
@app.route('/index')
def index_redirect():
    """Redirect /index to home page."""
    return redirect(url_for('index'))

@app.route('/')
def index():
    """Render the home page."""
    data = get_common_data()
    return render_template('demo-jewellery-store.html', **data)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Render the contact page and handle form submissions."""
    data = get_common_data()
    data['map_options'] = {
        "lat": -37.805688,
        "lng": 144.962312,
        "style": "night",
        "marker": {"type": "HTML", "class": "marker04", "color": "#f4decf"},
        "popup": {
            "defaultOpen": False,
            "html": '<div class="infowindow"><strong class="mb-3 d-inline-block alt-font">Crafto Jewellery Store</strong><p class="alt-font">16122 Collins street, Melbourne, Australia</p></div><div class="google-maps-link alt-font"><a aria-label="View larger map" target="_blank" href="https://maps.google.com/maps?ll=-37.805688,144.962312&z=17&t=m&hl=en-US&gl=IN&mapclient=embed&cid=13153204942596594449">VIEW LARGER MAP</a></div>'
        }
    }

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        comment = request.form.get('comment')

        if not name or not email:
            flash('Name and email are required', 'error')
        else:
            # Placeholder for saving to database or sending email
            flash('Your message has been sent successfully', 'success')
            return redirect(url_for('contact'))

    return render_template('demo-jewellery-store-contact.html', **data)

@app.route('/shop')
@app.route('/shop/<category>')
@app.route('/shop/<category>/<item>')
def shop(category=None, item=None):
    """Render the shop page with optional category and item filters."""
    data = get_common_data()
    shop_data = {
        'nav_categories': [
            {'title': 'Rings', 'subitems': ['Engagement', 'Gold rings', 'Casual rings', 'Silver rings', 'Platinum rings', 'Diamond rings']},
            {'title': 'Earrings', 'subitems': ['Jhumkas', 'Barbells', 'Hug hoops', 'Tear drop', 'Suidhaga', 'Gemstone']},
            {'title': 'Necklaces', 'subitems': ['Bib necklece', 'Collar necklece', 'Rope necklece', 'Locket necklece', 'Chain necklece', 'Opera nacklece']},
            {'title': 'Pendants', 'subitems': ['Alphabet', 'Mangalsutra', 'Religious', 'Diamond', 'Heart shaped', 'Gemstone']},
            {'title': 'Breslet', 'subitems': ['Caratlane chain', 'Oval bracelets', 'Pearl bracelets', 'Charm bracelets', 'Silver brcelets', 'Tennis bracelets']}
        ],
        'category_menu': ['Rings', 'Bracelet', 'Earrings', 'Necklace', 'Pendants', 'Watches', 'Chain'],
        'products': [
            {'id': 1, 'name': 'Diamond earrings', 'price': 189.00, 'original_price': 200.00, 'image': 'https://placehold.co/600x765', 'label': 'New'},
            {'id': 2, 'name': 'Geometric gold ring', 'price': 159.00, 'original_price': 180.00, 'image': 'https://placehold.co/600x765'},
            {'id': 3, 'name': 'Gemstone earrings', 'price': 189.00, 'original_price': 200.00, 'image': 'https://placehold.co/600x765', 'label': 'Hot'},
            {'id': 4, 'name': 'Gold diamond ring', 'price': 289.00, 'image': 'https://placehold.co/600x765'},
            {'id': 5, 'name': 'Pearl necklace', 'price': 129.00, 'original_price': 150.00, 'image': 'https://placehold.co/600x765'},
            {'id': 6, 'name': 'Silver bracelet', 'price': 99.00, 'original_price': 120.00, 'image': 'https://placehold.co/600x765', 'label': 'Sale'},
            {'id': 7, 'name': 'Gold pendant', 'price': 179.00, 'image': 'https://placehold.co/600x765'},
            {'id': 8, 'name': 'Diamond necklace', 'price': 349.00, 'original_price': 400.00, 'image': 'https://placehold.co/600x765', 'label': 'Hot'},
            {'id': 9, 'name': 'Platinum ring', 'price': 259.00, 'image': 'https://placehold.co/600x765'},
            {'id': 10, 'name': 'Hoop earrings', 'price': 89.00, 'original_price': 110.00, 'image': 'https://placehold.co/600x765'},
            {'id': 11, 'name': 'Tennis bracelet', 'price': 199.00, 'original_price': 230.00, 'image': 'https://placehold.co/600x765', 'label': 'New'},
            {'id': 12, 'name': 'Charm bracelet', 'price': 149.00, 'image': 'https://placehold.co/600x765'},
            {'id': 13, 'name': 'Charm bracelet', 'price': 149.00, 'image': 'https://placehold.co/600x765'},
            {'id': 14, 'name': 'Charm bracelet', 'price': 149.00, 'image': 'https://placehold.co/600x765'},
            {'id': 15, 'name': 'Charm bracelet', 'price': 149.00, 'image': 'https://placehold.co/600x765'},
            {'id': 16, 'name': 'Charm bracelet', 'price': 149.00, 'image': 'https://placehold.co/600x765'},
            
        ],
        'sidebar_categories': [
            {'name': 'Rings', 'qty': 25},
            {'name': 'Earrings', 'qty': 18},
            {'name': 'Necklaces', 'qty': 12},
            {'name': 'Bracelets', 'qty': 15},
            {'name': 'Pendants', 'qty': 10},
            {'name': 'Watches', 'qty': 8}
        ],
        'colors': [
            {'name': 'Gold', 'hex': '#FFD700', 'qty': 32},
            {'name': 'Silver', 'hex': '#C0C0C0', 'qty': 28},
            {'name': 'Rose Gold', 'hex': '#B76E79', 'qty': 15},
            {'name': 'Platinum', 'hex': '#E5E4E2', 'qty': 10},
            {'name': 'Black', 'hex': '#000000', 'qty': 8}
        ],
        'price_ranges': [
            {'range': '$0 - $100', 'qty': 15},
            {'range': '$100 - $200', 'qty': 25},
            {'range': '$200 - $300', 'qty': 18},
            {'range': '$300 - $400', 'qty': 12},
            {'range': '$400+', 'qty': 8}
        ],
        'metals': [
            {'name': 'Gold','hex': '#FFD700' ,'image': 'images/gold-texture.jpg', 'qty': 32},
            {'name': 'Silver','hex': '#C0C0C0', 'image': 'images/silver-texture.jpg', 'qty': 28},
            {'name': 'Platinum','hex': '#E5E4E2' ,'image': 'images/platinum-texture.jpg', 'qty': 10},
            {'name': 'Diamond', 'hex': '#FFD700','image': 'images/diamond-texture.jpg', 'qty': 22},
            {'name': 'Pearl', 'hex': '#FFD700','image': 'images/pearl-texture.jpg', 'qty': 15}
        ],
        'new_arrivals': [
            [
                {'id': 1, 'name': 'Diamond earrings', 'price': 189.00, 'original_price': 200.00, 'image': 'https://placehold.co/600x765'},
                {'id': 2, 'name': 'Geometric gold ring', 'price': 159.00, 'original_price': 180.00, 'image': 'https://placehold.co/600x765'},
                {'id': 3, 'name': 'Gemstone earrings', 'price': 189.00, 'original_price': 200.00, 'image': 'https://placehold.co/600x765'}
            ],
            [
                {'id': 4, 'name': 'Gold diamond ring', 'price': 289.00, 'image': 'https://placehold.co/600x765'},
                {'id': 5, 'name': 'Pearl necklace', 'price': 129.00, 'original_price': 150.00, 'image': 'https://placehold.co/600x765'},
                {'id': 6, 'name': 'Silver bracelet', 'price': 99.00, 'original_price': 120.00, 'image': 'https://placehold.co/600x765'}
            ],
            
        ],
        'tags': ['Gold', 'Silver', 'Diamond', 'Pearl', 'Platinum', 'Gemstone', 'Necklace', 'Bracelet', 'Ring', 'Earring'],
        'cart_count': 2,
        'products_per_page': 12,
        'total_pages': 4,
        'current_page': 1
    }
    data.update(shop_data)
    return render_template('demo-jewellery-store-shop.html', category=category, item=item, **data)

@app.route('/product/<int:product_id>')
def product(product_id):
    """Render a single product page."""
    data = get_common_data()
    product = None
    for tab in data['product_tabs']:
        for p in tab['products']:
            if p['id'] == product_id:
                product = p
                break
        if product:
            break
    if not product:
        flash('Product not found', 'error')
        return redirect(url_for('index'))
    data['product'] = product
    return render_template('demo-jewellery-store-single-product.html', **data)

@app.route('/offers')
def offers():
    """Render the offers page."""
    data = get_common_data()
    offers_data = {
        'page_title': 'Special Offers',
        'offers': [
            {'title': 'Summer Sale', 'description': 'Get up to 30% off on selected items', 'image': 'https://placehold.co/800x400', 'expiry_date': '2024-08-31'},
            {'title': 'New Customer Discount', 'description': '15% off on your first purchase', 'image': 'https://placehold.co/800x400', 'expiry_date': '2024-12-31'},
            {'title': 'Free Shipping', 'description': 'Free shipping on orders over $50', 'image': 'https://placehold.co/800x400', 'expiry_date': 'Ongoing'}
        ]
    }
    data.update(offers_data)
    return render_template('offers.html', **data)

@app.route('/categories')
def categories():
    """Render the categories page."""
    data = get_common_data()
    categories_data = {
        'page_title': 'Categories',
        'jewelry_categories': [
            {'name': 'Bangles', 'image': 'https://placehold.co/600x477', 'letter': 'B', 'url': 'bangles'},
            {'name': 'Pendants', 'image': 'https://placehold.co/600x477', 'letter': 'P', 'url': 'pendants'},
            {'name': 'Chain', 'image': 'https://placehold.co/600x477', 'letter': 'C', 'url': 'chain'},
            {'name': 'Earrings', 'image': 'https://placehold.co/600x1003', 'letter': 'E', 'url': 'earrings'},
            {'name': 'Rings', 'image': 'https://placehold.co/600x477', 'letter': 'R', 'url': 'rings'},
            {'name': 'Necklace', 'image': 'https://placehold.co/600x1003', 'letter': 'N', 'url': 'necklace'},
            {'name': 'Bracelet', 'image': 'https://placehold.co/600x477', 'letter': 'B', 'url': 'bracelet'}
        ]
    }
    data.update(categories_data)
    return render_template('demo-jewellery-store-categories.html', **data)

# Static page routes
@app.route('/about')
def about():
    """Render the about page."""
    return render_template('demo-jewellery-store-about.html', **get_common_data())

@app.route('/faq')
def faq():
    """Render the FAQ page."""
    return render_template('demo-jewellery-store-faq.html', **get_common_data())

@app.route('/wishlist')
def wishlist():
    """Render the wishlist page."""
    return render_template('demo-jewellery-store-wishlist.html', **get_common_data())

@app.route('/account')
def account():
    """Render the account page."""
    return render_template('demo-jewellery-store-account.html', **get_common_data())

@app.route('/cart')
def cart():
    """Render the cart page."""
    return render_template('demo-jewellery-store-cart.html', **get_common_data())

@app.route('/checkout')
def checkout():
    """Render the checkout page."""
    return render_template('demo-jewellery-store-checkout.html', **get_common_data())

@app.route('/blog')
def blog():
    """Render the blog page."""
    return render_template('demo-jewellery-store-blog.html', **get_common_data())

@app.route('/blog/<slug>')
def blog_single(slug):
    """Render a single blog post."""
    return render_template('demo-jewellery-store-blog-single-clean.html', **get_common_data())

@app.route('/no-sidebar')
def no_sidebar():
    """Render the no-sidebar shop page."""
    return render_template('demo-jewellery-store-no-sidebar.html', **get_common_data())

@app.route('/right-sidebar')
def right_sidebar():
    """Render the right-sidebar shop page."""
    return render_template('demo-jewellery-store-right-sidebar.html', **get_common_data())

@app.route('/search')
def search():
    """Render the search results page."""
    data = get_common_data()
    data['query'] = request.args.get('s', '')
    return render_template('search.html', **data)

@app.route('/order_history')
def order_history():
    """Render the order history page."""
    return render_template('order_history.html', **get_common_data())

@app.route('/account_details')
def account_details():
    """Render the account details page."""
    return render_template('account_details.html', **get_common_data())

@app.route('/customer_support')
def customer_support():
    """Render the customer support page."""
    return render_template('customer_support.html', **get_common_data())

@app.route('/logout')
def logout():
    """Handle user logout."""
    flash('You have been logged out', 'success')
    return redirect(url_for('index'))

@app.route('/profile')
def profile():
    """Render the user profile page."""
    return render_template('profile.html', **get_common_data())

@app.route('/order_tracking')
def order_tracking():
    """Render the order tracking page."""
    return render_template('order_tracking.html', **get_common_data())

@app.route('/careers')
def careers():
    """Render the careers page."""
    return render_template('careers.html', **get_common_data())

@app.route('/events')
def events():
    """Render the events page."""
    return render_template('events.html', **get_common_data())

@app.route('/articles')
def articles():
    """Render the articles page."""
    return render_template('articles.html', **get_common_data())

@app.route('/terms')
def terms():
    """Render the terms and conditions page."""
    return render_template('terms.html', **get_common_data())

@app.route('/privacy')
def privacy():
    """Render the privacy policy page."""
    return render_template('privacy.html', **get_common_data())

@app.route('/cookie_policy')
def cookie_policy():
    """Render the cookie policy page."""
    return render_template('cookie_policy.html', **get_common_data())

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    """Add a product to the cart."""
    flash('Product added to cart', 'success')
    return redirect(url_for('product', product_id=product_id))

@app.route('/add_to_wishlist/<int:product_id>')
def add_to_wishlist(product_id):
    """Add a product to the wishlist."""
    flash('Product added to wishlist', 'success')
    return redirect(url_for('product', product_id=product_id))

@app.route('/quick_view/<int:product_id>')
def quick_view(product_id):
    """Redirect to product page for quick view."""
    return redirect(url_for('product', product_id=product_id))

if __name__ == '__main__':
    app.run(debug=True)