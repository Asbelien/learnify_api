Learnify API — Gestor de Cursos Online 🎓

Learnify API es una aplicación desarrollada en Django y Django REST Framework (DRF) que permite la gestión de cursos online y los instructores encargados de dictarlos.
Este proyecto forma parte del Laboratorio 7 y 8 del curso Desarrollo de Aplicaciones Empresariales, y tiene como objetivo aplicar los conceptos fundamentales del desarrollo de APIs RESTful utilizando Django.

🧠 Descripción del proyecto

La API está diseñada para simular el backend de una plataforma educativa llamada Learnify, donde los usuarios pueden consultar, registrar, editar y eliminar información sobre cursos y sus instructores.

La aplicación incluye dos entidades principales:

Instructores — Representan a los docentes o especialistas que dictan los cursos.
Contienen información básica como nombre y especialidad.

Cursos — Representan los cursos disponibles en la plataforma.
Cada curso tiene un nombre, duración en horas, nivel (básico, intermedio, avanzado) y una relación directa con un instructor.

La API está completamente implementada mediante endpoints de Django REST Framework, sin uso del panel de administración de Django, cumpliendo así con los requisitos del laboratorio.

🎯 Objetivos del proyecto

Implementar un CRUD completo para dos entidades relacionadas.

Aplicar serializadores (Serializers) para transformar los datos entre modelos y JSON.

Configurar ViewSets y Routers para automatizar los endpoints de DRF.

Implementar búsqueda dinámica mediante filtros de consulta (?search=).

Probar los endpoints utilizando herramientas como Postman o cURL.

Documentar adecuadamente la estructura del proyecto y las rutas disponibles.

🛠️ Tecnologías utilizadas
Tecnología	Descripción
🐍 Python 3.12	Lenguaje de programación base
🧱 Django 5.x	Framework principal para el backend
⚙️ Django REST Framework	Extensión para crear APIs RESTful
🗄️ SQLite	Base de datos ligera por defecto
🧩 venv / Pipenv	Manejo de entornos virtuales
🐙 Git / GitHub	Control de versiones y alojamiento del proyecto
⚙️ Instalación y configuración

Sigue estos pasos para ejecutar el proyecto en tu máquina local:

1️⃣ Clonar el repositorio

git clone https://github.com/Asbelien/learnify_api.git
cd learnify_api


2️⃣ Crear un entorno virtual

python -m venv venv


3️⃣ Activar el entorno virtual

En Windows PowerShell:

venv\Scripts\Activate.ps1


En Windows CMD:

venv\Scripts\activate.bat


En Linux/Mac:

source venv/bin/activate


4️⃣ Instalar dependencias

pip install -r requirements.txt


5️⃣ Aplicar migraciones

python manage.py makemigrations
python manage.py migrate


6️⃣ Ejecutar el servidor de desarrollo

python manage.py runserver


7️⃣ Probar la API
Abre tu navegador o herramientas como Postman y visita:

http://127.0.0.1:8000/api/v1/cursos/
http://127.0.0.1:8000/api/v1/instructores/

📂 Endpoints disponibles
Cursos
Método	Endpoint	Descripción
GET	/api/v1/cursos/	Listar todos los cursos
POST	/api/v1/cursos/	Crear un nuevo curso
PUT/PATCH	/api/v1/cursos/{id}/	Editar un curso existente
DELETE	/api/v1/cursos/{id}/	Eliminar un curso existente
GET	/api/v1/cursos/?search=<nombre>	Buscar cursos por nombre

Ejemplo cURL para crear un curso:

curl -X POST http://127.0.0.1:8000/api/v1/cursos/ \
-H "Content-Type: application/json" \
-d '{"nombre": "Django Básico", "duracion_horas": 20, "nivel": "Básico", "instructor": 1}'

Instructores
Método	Endpoint	Descripción
GET	/api/v1/instructores/	Listar todos los instructores
POST	/api/v1/instructores/	Crear un nuevo instructor
PUT/PATCH	/api/v1/instructores/{id}/	Editar un instructor existente
DELETE	/api/v1/instructores/{id}/	Eliminar un instructor existente

Ejemplo cURL para listar instructores:

curl http://127.0.0.1:8000/api/v1/instructores/

✅ Notas finales

Todos los endpoints están implementados sin usar Django Admin.

La API es totalmente funcional y lista para integrarse con un frontend o app móvil.

Se recomienda usar Postman o cURL para probar y verificar cada endpoint.
