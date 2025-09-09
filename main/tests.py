from django.test import TestCase
from .models import Product

class ProductModelTest(TestCase):
    def test_create_product(self):
        product = Product.objects.create(
            name="Messi FunkoPop",
            price=350000,
            description="Messi dengan seragam Argentina",
            thumbnail="https://i.imgur.com/messi.jpg",
            category="Football Player",
            is_featured=True
        )
        self.assertEqual(product.name, "Messi FunkoPop")
        self.assertEqual(product.price, 350000)
