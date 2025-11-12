# Django Portfolio – Aplicación CRUD + Autenticación + Permisos + Bootstrap

Proyecto final de portafolio desarrollado con **Django 5.x**, demostrando el dominio de las principales funcionalidades del framework:  
configuración de proyecto, templates, formularios, autenticación, autorización, módulo admin y mejora visual con Bootstrap 5.

---

## 🚀 Características principales

✅ **Framework Django:** rápido, seguro y escalable.  
✅ **CRUD completo** para el modelo `Product` (crear, listar, editar, eliminar, marcar inactivo).  
✅ **Autenticación de usuarios:** registro, login y logout funcional con CSRF seguro.  
✅ **Autorización con permisos:** control de acceso a las vistas según roles.  
✅ **Grupos automáticos:** los nuevos usuarios se asignan al grupo `Readers` con permiso `view_product`.  
✅ **Panel de administración personalizado.**  
✅ **Interfaz moderna** con Bootstrap 5.  
✅ **Mensajes de éxito/error** integrados con `django.contrib.messages`.  
✅ **Templates organizados y reutilizables.**

---


## 👥 Roles y permisos

El proyecto crea 2 niveles principales:

| Rol / Grupo | Permisos principales | Acceso |
|--------------|----------------------|---------|
| **Readers**  | `view_product`       | Solo visualización |
| **Managers** | Todos + `can_mark_inactive` | Crear, editar, eliminar, marcar inactivo |

Los nuevos usuarios registrados se agregan automáticamente al grupo **Readers**.

---

## 🔒 Autenticación y flujo de usuarios

### Rutas principales:
| URL | Descripción |
|------|--------------|
| `/accounts/login/` | Iniciar sesión |
| `/accounts/logout/` | Cerrar sesión (POST seguro o redirección inmediata) |
| `/accounts/register/` | Crear una nueva cuenta |
| `/catalog/products/` | Ver productos (requiere login) |
| `/catalog/products/create/` | Crear producto (requiere permiso) |
| `/catalog/products/<id>/edit/` | Editar producto (requiere permiso) |
| `/catalog/products/<id>/delete/` | Eliminar producto (requiere permiso) |

> 🔁 Tras cerrar sesión, se redirige automáticamente a la página de login.

---

## 💅 Interfaz y experiencia de usuario (UX/UI)

- **Bootstrap 5** integrado desde CDN.  
- **Navbar adaptable** con botones claros de *Login*, *Registro* y *Salir*.  
- **Mensajes flash** para feedback inmediato al usuario.  
- **Tablas y formularios** con diseño limpio y responsivo.  
- **Cards** para formularios y alertas con sombras suaves.  

---

## 🧠 Sobre Django

**Ventajas para entornos empresariales:**
- Productividad alta con *admin*, *auth* y *ORM* integrados.  
- Seguridad (CSRF, XSS, SQL Injection) lista para usar.  
- Escalable con soporte para *caching*, *middlewares* y *signals*.  
- Comunidad grande y ecosistema maduro.

**Comparación breve con otros frameworks:**

| Framework | Enfoque | Ventajas | Desventajas |
|------------|----------|-----------|--------------|
| **Django** | Full-stack | Todo integrado, seguridad, ORM, admin | Más pesado para microservicios |
| **Flask** | Microframework | Ligero, flexible | Requiere configurar auth, ORM, admin manualmente |
| **FastAPI** | Asíncrono / APIs | Rápido, tipado, ideal para APIs REST | No trae templates ni admin integrado |

---

## 🧰 Comandos útiles

```bash
python manage.py makemigrations   # Crear migraciones
python manage.py migrate          # Aplicar migraciones
python manage.py createsuperuser  # Crear usuario admin
python manage.py runserver        # Ejecutar servidor
python manage.py loaddata products.json  # Cargar datos de ejemplo
python manage.py test             # Ejecutar tests (si los agregas)
```

---

# Django Portfolio – Módulo 7: Integración con Bases de Datos

Este proyecto corresponde a la **Evaluación de Portafolio del Módulo 7**, centrado en la **integración del framework Django con bases de datos**.  
Se desarrolla como una continuación del portafolio anterior, pero en una **rama independiente** llamada `feature/m7-db`.

---

## 🧭 Cambio de rama

Para revisar este módulo:
```bash
git fetch origin
git checkout feature/m7-db
python manage.py migrate
python manage.py runserver
```

Rutas principales:
- `/sales/customers/` — CRUD de clientes
- `/sales/orders/` — Pedidos con ítems relacionados a productos

---

## 🧩 Objetivos del módulo

1. **Describir la integración de Django con bases de datos.**
2. **Implementar modelos sin relaciones y con relaciones (1-1, 1-N, N-N).**
3. **Utilizar migraciones para reflejar cambios en la base de datos.**
4. **Realizar consultas ORM y SQL personalizadas.**
5. **Implementar una aplicación web CRUD completa.**
6. **Reconocer las aplicaciones preinstaladas del motor Django.**

---

## ⚙️ Configuración de Base de Datos

Por defecto se utiliza **SQLite** para desarrollo.

**`portfolio/settings.py`:**
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

### Ejemplo para PostgreSQL:
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("PGDATABASE", "django_portfolio"),
        "USER": os.getenv("PGUSER", "postgres"),
        "PASSWORD": os.getenv("PGPASSWORD", ""),
        "HOST": os.getenv("PGHOST", "127.0.0.1"),
        "PORT": os.getenv("PGPORT", "5432"),
    }
}
```

### Ejemplo para MySQL:
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("MYSQL_DATABASE", "django_portfolio"),
        "USER": os.getenv("MYSQL_USER", "root"),
        "PASSWORD": os.getenv("MYSQL_PASSWORD", ""),
        "HOST": os.getenv("MYSQL_HOST", "127.0.0.1"),
        "PORT": os.getenv("MYSQL_PORT", "3306"),
        "OPTIONS": {"charset": "utf8mb4"},
    }
}
```

---

## 🧱 Modelos implementados

### App `catalog` (sin relaciones)
- `Product`: nombre, sku, precio, activo, creador.

### App `sales` (con relaciones)
| Modelo | Tipo de relación | Descripción |
|---------|------------------|--------------|
| `Customer` | — | Entidad principal (cliente). |
| `CustomerProfile` | OneToOne | Datos adicionales del cliente. |
| `Order` | ForeignKey (1-N con `Customer`) | Pedido del cliente. |
| `OrderItem` | ManyToMany (Order–Product) | Ítems con cantidad y precio unitario. |
| `Tag` | ManyToMany (con `Product`) | Etiquetas de productos. |

---

## 🧩 Migraciones

Creación y aplicación de migraciones:
```bash
python manage.py makemigrations
python manage.py migrate
```

> Cada cambio en los modelos genera migraciones que Django traduce en operaciones SQL para crear/modificar tablas.

---

## 🧮 Consultas ORM

### Ejemplos:
```python
from sales.models import Customer, Order, OrderItem
from django.db.models import Sum, F

# Filtrar pedidos por cliente
Order.objects.filter(customer__email="demo@example.com")

# Excluir pedidos cancelados
Order.objects.exclude(notes__icontains="cancelado")

# Obtener un cliente específico
Customer.objects.get(email="demo@example.com")

# Calcular total gastado por un cliente
OrderItem.objects.filter(order__customer__email="demo@example.com").aggregate(
    total=Sum(F("quantity") * F("unit_price"))
)
```

### Consulta con `annotate()` (agrupación)
```python
from django.db.models import Count
OrderItem.objects.values("order__customer__full_name").annotate(
    total=Sum(F("quantity") * F("unit_price")),
    pedidos=Count("order", distinct=True)
).order_by("-total")
```

---

## 🧾 Consulta SQL pura (raw)

```python
from django.db import connection

with connection.cursor() as cur:
    cur.execute("""
        SELECT c.full_name, SUM(oi.quantity * oi.unit_price) AS total_spent
        FROM sales_customer c
        JOIN sales_order o ON o.customer_id = c.id
        JOIN sales_orderitem oi ON oi.order_id = o.id
        GROUP BY c.full_name
        ORDER BY total_spent DESC;
    """)
    print(cur.fetchall())
```

---

## 💻 CRUD implementado

### Rutas principales:

| URL | Descripción |
|------|--------------|
| `/sales/customers/` | Listar clientes |
| `/sales/customers/create/` | Crear cliente |
| `/sales/customers/<id>/edit/` | Editar cliente |
| `/sales/customers/<id>/delete/` | Eliminar cliente |
| `/sales/orders/` | Listar pedidos |
| `/sales/orders/create/` | Crear pedido |
| `/sales/orders/<id>/` | Ver detalle (agregar ítems) |

---

## 🧰 Aplicaciones preinstaladas utilizadas

| App | Propósito |
|------|------------|
| `django.contrib.admin` | Panel de administración. |
| `django.contrib.auth` | Sistema de usuarios y permisos. |
| `django.contrib.contenttypes` | Tipos de contenido y relaciones genéricas. |
| `django.contrib.sessions` | Manejo de sesiones. |
| `django.contrib.messages` | Sistema de mensajes flash. |
| `django.contrib.staticfiles` | Gestión de archivos estáticos. |

---

## 🧾 Estructura del proyecto

```
django-portfolio/
├── catalog/                # App previa (modelo sin relaciones)
├── sales/                  # App del módulo 7
│   ├── models.py           # Relaciones 1-1, 1-N, N-N
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/sales/
│       ├── customer_list.html
│       ├── customer_form.html
│       ├── order_list.html
│       ├── order_detail.html
│       └── ...
├── portfolio/
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── templates/
    └── base.html
```

---

## 🧪 Ejecución local

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Accede a:
- http://127.0.0.1:8000/sales/customers/
- http://127.0.0.1:8000/sales/orders/
- http://127.0.0.1:8000/admin/

---

## 📚 Requerimientos del módulo cumplidos

✅ **Integración Django–BD documentada** en `settings.py`  
✅ **Modelos sin relaciones** (`catalog.Product`)  
✅ **Modelos con relaciones 1-1, 1-N, N-N** (`sales` app)  
✅ **Migraciones aplicadas y explicadas**  
✅ **Consultas ORM y SQL personalizadas**  
✅ **CRUD web MVC completo**  
✅ **Reconocimiento de apps preinstaladas**

---

⌨️ con ❤️ por [Abraham Lillo](https://github.com/toffycaluga)