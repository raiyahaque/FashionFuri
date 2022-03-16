My final project is an online e-commerce clothing shop called Fashion FurI. I implemented the use of a Users, Categories, and Clothings model under myapp and the use of an Order and Item model under the orders app.

The views.py file under 'myapp' implements the login, registration, and logout. It also has a function for returning clothes in a specific category as well as another function for returning gender-specific clothes in general or in a specific category. Another function returns the clothing descriptions, and the last function in views.py implements the search for clothes through category, name, and color.

The html templates display all of the clothes, clothing descriptions, the homepage, the login page, registration page, and search results. There is also a layout.html file that contains the navigation bars and search bar, etc. I used JavaScript for some animation of the logo and for disabling the form buttons until the required fields were filled out.

I created the Cart class and added methods for adding, saving, retrieving, clearing, and removing products as well as getting the total price in cart.py.  
I created a forms.py file in order to have a form for adding products with a certain quantity into the cart. In the views.py file, I created functions to add, remove, and return products from the cart. The cart_details.html file displays all of the products in the cart and their details as well as the total price.

The views.py file in the 'order' app has a view to create the order using the personal details entered by the user. This view uses the order model to create each order object, and after creating the order, it clears the cart as well. The personalDetails.html file displays the form to submit all of the user's personal details and displays an order summary, and ordered.html is returned when the order is successfully placed.

My project satisfies the requirements as it implements numerous models (Users, Categories, Clothings, Order, Item) on the back-end and JavaScript on the front-end. I created three separate apps ('myapp', 'order', 'cart') in order for the web application to come together as a whole, and the online shop runs smoothly. I added a lot of styling throughout my navigation bars in order to make my online shop look as realistic as possible and responsive.   

I also attached the images I used for my online shop in the project directory.

Note: I also hosted this online shop on a public domain named fashionfuri.com, and I intend to continue working on it as a full phase e-commerce shop for clothing. 
