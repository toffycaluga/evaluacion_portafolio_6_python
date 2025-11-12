from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .models import Customer, Order, OrderItem
from .forms import CustomerForm, OrderForm, OrderItemForm

# ---- CUSTOMERS (CRUD) ----

class CustomerListView(LoginRequiredMixin, ListView):
    """
    Lista de clientes.
    """
    model = Customer
    template_name = "sales/customer_list.html"
    context_object_name = "customers"

class CustomerCreateView(LoginRequiredMixin, CreateView):
    """
    Crear nuevo cliente.
    """
    model = Customer
    form_class = CustomerForm
    template_name = "sales/customer_form.html"
    success_url = reverse_lazy("customer_list")

    def form_valid(self, form):
        messages.success(self.request, "Cliente creado correctamente.")
        return super().form_valid(form)

class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    """
    Editar cliente.
    """
    model = Customer
    form_class = CustomerForm
    template_name = "sales/customer_form.html"
    success_url = reverse_lazy("customer_list")

    def form_valid(self, form):
        messages.success(self.request, "Cliente actualizado.")
        return super().form_valid(form)

class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    """
    Eliminar cliente.
    """
    model = Customer
    template_name = "sales/customer_confirm_delete.html"
    success_url = reverse_lazy("customer_list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Cliente eliminado.")
        return super().delete(request, *args, **kwargs)

# ---- ORDERS ----

class OrderListView(LoginRequiredMixin, ListView):
    """
    Listado de pedidos con totales (usando propiedad total_amount).
    """
    model = Order
    template_name = "sales/order_list.html"
    context_object_name = "orders"
    queryset = Order.objects.select_related("customer").prefetch_related("items")

class OrderCreateView(LoginRequiredMixin, CreateView):
    """
    Crear pedido (sin items aún).
    """
    model = Order
    form_class = OrderForm
    template_name = "sales/order_form.html"

    def get_success_url(self):
        return reverse_lazy("order_detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        messages.success(self.request, "Pedido creado. Ahora agrega ítems.")
        return super().form_valid(form)

class OrderDetailView(LoginRequiredMixin, DetailView):
    """
    Ver pedido y sus items, con formulario para agregar uno nuevo.
    """
    model = Order
    template_name = "sales/order_detail.html"
    context_object_name = "order"

def add_item_to_order(request, pk):
    """
    Agrega un item a un pedido existente (N-N a través de tabla intermedia).
    """
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        form = OrderItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.order = order
            item.save()
            messages.success(request, "Ítem agregado.")
            return redirect("order_detail", pk=order.pk)
    else:
        form = OrderItemForm()
    return render(request, "sales/order_add_item.html", {"order": order, "form": form})
