# Proyecto Django REST Framework - API de Bitácoras Geolocalizadas

Este proyecto está desarrollado en **Python** utilizando **Django REST Framework** y ofrece una API para la gestión de usuarios, perfiles y un sistema de bitácoras con soporte de entradas geolocalizadas.

---

## 🚀 Funcionalidades Implementadas

✅ **Registro de Usuarios**

-   Los usuarios pueden registrarse exitosamente.
-   El registro crea automáticamente:
    -   Un objeto `User` estándar de Django.
    -   Un objeto `Profile` asociado mediante una relación uno a uno (`1:1`).

✅ **Perfil de Usuario (`Profile`)**

-   El perfil se inicializa con valores por defecto a partir de los datos del usuario (nombre de usuario, siglas).
-   Puede editarse a través de la API para actualizar información personal.
-   Incluye un campo `addresses`, que contiene datos estructurados para direcciones.
-   Las direcciones están integradas con la **API de Google Maps** para obtener coordenadas precisas y geolocalización.

✅ **Relaciones entre Modelos**

-   **Perfil a Bitácoras (`LogBook`)**
    -   Relación **uno a muchos (`1:N`)**: un perfil puede tener múltiples libros de bitácoras asociados.
-   **Bitácora a Entrada de Bitácora (`LogEntry`)**
    -   Relación **muchos a muchos (`M:N`)**:
        -   Un `LogBook` puede contener múltiples `LogEntry`.
        -   Una `LogEntry` puede estar asociada a múltiples `LogBook`.

✅ **Entradas con Geolocalización**

-   Cada entrada (`LogEntry`) contiene datos de ubicación:
    -   País, estado, ciudad, calle y código postal.
    -   Coordenadas geoespaciales almacenadas en un campo `PointField` de **Django GIS**.
-   Esto permite realizar consultas espaciales y mostrar las entradas en mapas.

---

## 🗃️ Base de Datos

🔹 **PostgreSQL + PostGIS**

-   La base de datos utilizada es **PostgreSQL** con la extensión **PostGIS** habilitada.
-   Esto es fundamental para que los campos geoespaciales (`PointField`) y las consultas espaciales funcionen correctamente.

---

## 🔗 Relaciones entre Modelos

| Modelo    | Relación                    | Modelo Relacionado | Tipo de Relación |
| --------- | --------------------------- | ------------------ | ---------------- |
| `User`    | 1:1                         | `Profile`          | Uno a uno        |
| `Profile` | 1:N                         | `LogBook`          | Uno a muchos     |
| `LogBook` | Muchos a muchos (`entries`) | `LogEntry`         | Muchos a muchos  |

---

## 🔄 Flujo de Datos

1. El usuario se registra.
2. Automáticamente se crea un `Profile` vinculado al usuario.
3. Cada perfil puede tener uno o varios `LogBook`.
4. Cada `LogBook` puede tener múltiples `LogEntry` asociados, que pueden compartirse entre distintos `LogBook`.
5. Las entradas (`LogEntry`) cuentan con geolocalización gracias a los campos de tipo **GIS**.

---

## 📦 Tecnologías Usadas

-   **Python**
-   **Django** y **Django REST Framework** para la API.
-   **PostgreSQL** como base de datos principal.
-   **PostGIS** como extensión geoespacial para **Django GIS**.
-   **Google Maps API** para enriquecer direcciones con coordenadas.

---

## ⚙️ Instalación de Dependencias

Antes de correr la API, asegúrate de tener un entorno virtual configurado (opcional pero recomendado). Para instalar todas las dependencias listadas en el archivo `requirements.txt`, ejecuta:

```bash
pip install -r requirements.txt
```

🔑 API Key de Google
Esta API trabaja en conjunto con la `API de Google Maps` para la geolocalización de direcciones.
Necesitarás proporcionar tu propia clave de API de Google para que la funcionalidad de geolocalización funcione correctamente.

🔹 La clave debe incluirse en tu archivo .env como:
