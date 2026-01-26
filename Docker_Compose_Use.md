### Run with Docker
```bash
# Docker Image Build
docker build -t django-stripe .
docker run -p 8000:8000 django-stripe

# Docker Compose file Run
docker compose up --build
docker compose down -v
```

Now open in browser
Go to:
```bash
http://localhost:8000
```

If home page expects products and DB is empty, So wait and execute Below Commands
Add sample products
Run this 
```bash
docker compose exec web python manage.py shell
```
```bash
from shop.models import Product

Product.objects.create(name="T-Shirt", price=50000)
Product.objects.create(name="Shoes", price=120000)
Product.objects.create(name="Cap", price=30000)

exit()
```
Refresh browser — products should appear.
