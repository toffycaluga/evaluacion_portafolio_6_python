from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from .models import Product
from .forms import ProductForm

class HomeView(TemplateView):
    template_name = "home.html"

class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Product
    template_name = "catalog/product_list.html"
    context_object_name = "products"
    permission_required = "catalog.view_product"

class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("product_list")
    permission_required = "catalog.add_product"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, "Producto creado correctamente.")
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("product_list")
    permission_required = "catalog.change_product"

    def form_valid(self, form):
        messages.success(self.request, "Producto actualizado.")
        return super().form_valid(form)

class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("product_list")
    permission_required = "catalog.delete_product"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Producto eliminado.")
        return super().delete(request, *args, **kwargs)

@login_required
@permission_required("catalog.can_mark_inactive", raise_exception=True)
def product_mark_inactive(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.is_active = False
    product.save()
    messages.info(request, f"{product.name} marcado como inactivo.")
    return redirect("product_list")
