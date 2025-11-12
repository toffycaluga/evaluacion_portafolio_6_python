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

⌨️ con ❤️ por [Abraham Lillo](https://github.com/toffycaluga)