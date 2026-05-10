from django.db import models
import uuid

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    imagePath = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"""
            '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
            Product: id={self.id}
            name: {self.name}
            description: {self.description}
            price: {self.price}
            created_at: {self.created_at}
            updated_at: {self.updated_at}
            imagePath: {self.imagePath}
            '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
            """

    class Meta:
        db_table = 'store_products'

class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=17)
    additional = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"""
            '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
            Person: id={self.id}
            name: {self.name}
            surname: {self.surname}
            email: {self.email}
            phone: {self.phone}
            additional: {self.additional}
            '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
            """

    class Meta:
        db_table = 'Persons'