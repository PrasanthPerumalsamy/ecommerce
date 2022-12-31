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
http://localhost:8000/?category=

ex:
    http://localhost:8000/?category=3
    http://localhost:8000/?category=1&active=true


<!-- Sorting Query Parameter -->
http://localhost:8000/?ordering=-id

ex:
    http://localhost:8000/?ordering=-id
    http://localhost:8000/?active=true&category=1&ordering=id

