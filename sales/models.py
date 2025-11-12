from django.db import models
from django.utils import timezone

# ENTIDAD SIN RELACIONES (ya la tenemos en 'catalog.Product').
# Aquí creamos ENTIDADES RELACIONADAS para M7.

class Customer(models.Model):
    """
    Cliente de la tienda.
    Relación: será el lado 'uno' en una relación 1-N con Order.
    """
    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"{self.full_name} <{self.email}>"

class CustomerProfile(models.Model):
    """
    Ejemplo de relación 1-1 (OneToOneField).
    Un Customer tiene exactamente un perfil con datos adicionales.
    """
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name="profile")
    document_id = models.CharField("Documento", max_length=50, unique=True)
    phone = models.CharField(max_length=30, blank=True)

    def __str__(self) -> str:
        return f"Perfil de {self.customer.full_name}"

class Order(models.Model):
    """
    Pedido: relación 1-N con Customer (muchos pedidos de un cliente).
    Además se relaciona N-N con Product a través de OrderItem (tabla intermedia explícita).
    """
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name="orders")
    created_at = models.DateTimeField(default=timezone.now)
    notes = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"Order #{self.pk} - {self.customer.full_name}"

    @property
    def total_amount(self) -> float:
        # Suma de subtotales de sus items
        return sum(item.subtotal for item in self.items.all())

class OrderItem(models.Model):
    """
    Item de pedido: tabla intermedia entre Order y Product (N-N).
    - order: FK a Order
    - product: FK a catalog.Product (referencia por 'app.Model')
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("catalog.Product", on_delete=models.PROTECT, related_name="order_items")
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = [("order", "product")]  # Un producto por pedido (simplificación)

    def __str__(self) -> str:
        return f"{self.product.name} x {self.quantity} (Order #{self.order_id})"

    @property
    def subtotal(self) -> float:
        return float(self.unit_price) * self.quantity

class Tag(models.Model):
    """
    Etiquetas N-N vinculadas a productos del catálogo.
    Demuestra ManyToMany sin tocar el modelo Product directamente.
    """
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(unique=True)
    products = models.ManyToManyField("catalog.Product", related_name="tags", blank=True)

    def __str__(self) -> str:
        return self.name
