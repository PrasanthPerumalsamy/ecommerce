<!-- Admin panel details -->
username: admin
password: admin

The same API path for all actions like Search, Filter & Ordering

For List view --> http://localhost:8000/

<!-- Search Query Parameter -->
http://localhost:8000/?search=

ex: 
    http://localhost:8000/?search=mobile
    http://localhost:8000/?search=lap


<!-- Filter Query Parameter -->
ex: http://localhost:8000/?producttype=&category=&active=

By product type --> http://localhost:8000/?producttype=3 (Electronics, Gadgets, Storage) As many-to-many relationship

By category --> http://localhost:8000/?category=1 (Mobile, laptops, pendrives)
Active & Inactive --> http://localhost:8000/?active=false


<!-- Sorting Query Parameter -->
By Popularity --> http://localhost:8000/?ordering=-rating
Price Low to High --> http://localhost:8000/?ordering=price
PRice Hight to Low --> http://localhost:8000/?ordering=-price
Newest First --> http://localhost:8000/?ordering=-id

