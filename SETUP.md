# 🏠 Mi Vivienda - Guía de Instalación y Ejecución

## Requisitos Previos
- Python 3.10+
- pip (gestor de paquetes de Python)
- PostgreSQL 12+ instalado y corriendo
- CMD (Símbolo del Sistema)
- pgAdmin (opcional, para administrar la BD)

---

## Paso 1: Preparar el Ambiente Virtual

Abre CMD en la carpeta del proyecto y ejecuta:

```cmd
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
venv\Scripts\activate.bat
```

---

## Paso 2: Instalar Dependencias

```cmd
# Actualizar pip
python -m pip install --upgrade pip

# Instalar dependencias del proyecto
pip install -r requirements.txt
```

---

## Paso 3: Verificar Conexión a PostgreSQL

Asegúrate de que PostgreSQL esté corriendo y que la base de datos `mivivienda_db` exista:

```cmd
# Verificar credenciales en .env
type .env

# Las credenciales deben ser:
# DB_NAME=mivivienda_db
# DB_USER=postgres
# DB_PASSWORD=B@ldeon18
# DB_HOST=localhost
# DB_PORT=5432
```

Si la BD no existe, créala en pgAdmin o con psql:

```sql
CREATE DATABASE mivivienda_db;
```

---

## Paso 4: Aplicar Migraciones

```cmd

# Aplicar todas las migraciones
python manage.py migrate
```

---

## Paso 5: Generar Datos Iniciales

```cmd
# Ejecutar script para poblar la base de datos
python seed_data.py
```

**Datos que se crean automáticamente:**
- Grupos de usuarios (Admin, Vendedor, Cliente)
- 4 usuarios de prueba (admin + 3 vendedores)
- 6 entidades financieras (bancos y cajas)
- 24 tasas de interés por plazo
- 4 bonos del buen pagador
- 4 proyectos inmobiliarios
- 11 inmuebles de ejemplo

### Credenciales de Prueba

| Email | Rol | Contraseña |
|-------|-----|-----------|
| admin@mivivienda.com | Administrador | Admin123456 |
| juan.perez@mivivienda.com | Vendedor | Juan123456 |
| maria.garcia@mivivienda.com | Vendedor | Maria123456 |
| carlos.lopez@mivivienda.com | Vendedor | Carlos123456 |

---

## Paso 6: Ejecutar el Servidor

```cmd
# Iniciar servidor Django
python manage.py runserver

# O especificar puerto personalizado
python manage.py runserver 0.0.0.0:8000
```

El servidor estará disponible en: http://localhost:8000

---

## Paso 7: Acceder a la Aplicación

1. Abre el navegador en http://localhost:8000
2. Ingresa con cualquiera de las credenciales de prueba
3. ¡Listo para usar el simulador!

---

## 📋 Estructura del Proyecto

```
mi-vivieda-v3/
├── mivivienda_project/
│   ├── apps/
│   │   ├── auth_app/
│   │   ├── business/
│   │   ├── financial/
│   │   ├── security/
│   │   └── simulation/
│   ├── config/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── manage.py
├── templates/
├── static/
├── seed_data.py
├── .env
├── requirements.txt
└── venv/
```

---

## 🔍 Solución de Problemas

### Error: "Conexión rechazada a PostgreSQL"
- Verifica que PostgreSQL esté corriendo
- En Windows: Abre Services.msc y verifica que PostgreSQL está iniciado

### Error: "database mivivienda_db does not exist"
- Crea la base de datos en PostgreSQL:
  ```sql
  CREATE DATABASE mivivienda_db;
  ```

### Error: "ModuleNotFoundError"
- Verifica que el entorno virtual esté activado (debe mostrar `(venv)` al inicio)
- Reinstala: `pip install -r requirements.txt`

### Puerto 8000 ya está en uso
- Usa otro puerto: `python manage.py runserver 8001`

---

## 📌 Comandos Útiles

```cmd
# Desactivar entorno virtual
deactivate

# Acceder a la consola Django
python manage.py shell

# Limpiar y regenerar datos
python manage.py flush --no-input
python seed_data.py

# Compilar recursos estáticos
python manage.py collectstatic --noinput

# Ver migraciones pendientes
python manage.py showmigrations
```

---

## 🚀 Resumen Rápido (Primera Vez)

```cmd
# 1. Activar entorno
venv\Scripts\activate.bat

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Aplicar migraciones
python manage.py migrate

# 4. Generar datos iniciales
python seed_data.py

# 5. Ejecutar servidor
python manage.py runserver

# 6. Abrir en navegador
# http://localhost:8000
```

---

**¡Listo!** 🎉 El proyecto está configurado y listo para usar con PostgreSQL.


