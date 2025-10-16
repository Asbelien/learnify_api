# 🎓 Learnify API — Gestor de Cursos Online

**Learnify API** es una aplicación desarrollada en **Django** y **Django REST Framework (DRF)** que permite la **gestión de cursos online** y los **instructores** encargados de dictarlos.  
Este proyecto forma parte del **Laboratorio 7 y 8** del curso *Desarrollo de Aplicaciones Empresariales*, y tiene como objetivo aplicar los conceptos fundamentales del desarrollo de APIs RESTful utilizando Django.

---

## 🧠 Descripción del proyecto

La API está diseñada para simular el backend de una plataforma educativa llamada **Learnify**, donde los usuarios pueden consultar, registrar, editar y eliminar información sobre cursos y sus instructores.

La aplicación incluye dos entidades principales:

1. **Instructores** — Representan a los docentes o especialistas que dictan los cursos.  
   Contienen información básica como nombre y especialidad.

2. **Cursos** — Representan los cursos disponibles en la plataforma.  
   Cada curso tiene un nombre, duración en horas, nivel (básico, intermedio, avanzado) y una relación directa con un instructor.

La API está completamente implementada mediante **endpoints de Django REST Framework**, sin uso del panel de administración de Django, cumpliendo así con los requisitos del laboratorio.

---

## 🎯 Objetivos del proyecto

- Implementar un **CRUD completo** para dos entidades relacionadas.
- Aplicar **serializadores (Serializers)** para transformar los datos entre modelos y JSON.
- Configurar **ViewSets y Routers** para automatizar los endpoints de DRF.
- Implementar **búsqueda dinámica** mediante filtros de consulta (`?search=`).
- Probar los endpoints utilizando herramientas como **Postman** o **cURL**.
- Documentar adecuadamente la estructura del proyecto y las rutas disponibles.

---

## 🛠️ Tecnologías utilizadas

| Tecnología | Descripción |
|-------------|--------------|
| 🐍 **Python 3.12** | Lenguaje de programación base |
| 🧱 **Django 5.x** | Framework principal para el backend |
| ⚙️ **Django REST Framework** | Extensión para crear APIs RESTful |
| 🗄️ **SQLite** | Base de datos ligera por defecto |
| 🧩 **Pipenv / venv** | Manejo de entornos virtuales |
| 🐙 **Git / GitHub** | Control de versiones y alojamiento del proyecto |

---

## ⚙️ Instalación y configuración

Sigue estos pasos para ejecutar el proyecto en tu máquina local:

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/Asbelien/learnify_api.git
cd learnify_api
