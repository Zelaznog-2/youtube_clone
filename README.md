# ✅ README Mejorado – Clon de YouTube

## 🚀 Pasos para ejecutar el proyecto

1. **Clona el repositorio:**

```bash
git clone https://github.com/Zelaznog-2/youtube_clone.git
```

2. **Accede al directorio del backend:**

```bash
cd youtube_clone
```

> **Nota:** Asegúrate de tener **Python 3.9 o superior** instalado en tu sistema.

3. **Configura la base de datos:**

- Dentro de la carpeta `youtube_clone`, localiza el archivo `settings.py`.
- Modifica manualmente la configuración de la base de datos con tus credenciales.
- (En el futuro se planea usar un archivo `.env`, pero aún no se ha implementado).

4. **Ejecuta las migraciones:**

- En **Linux/MacOS**:

```bash
python manage.py migrate
```

- En **Windows**:

```bash
py manage.py migrate
```

5. **Crea un superusuario:**

- En **Linux/MacOS**:

```bash
python manage.py createsuperuser
```

- En **Windows**:

```bash
py manage.py createsuperuser
```

6. **Inicia el servidor:**

- En **Linux/MacOS**:

```bash
python manage.py runserver
```

- En **Windows**:

```bash
py manage.py runserver
```

7. **Accede al panel de administración:**

Abre tu navegador y visita:  
👉 [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

Desde ahí podrás:
- Crear nuevos usuarios
- Subir videos

8. **Visualiza el sistema:**

Ir a:  
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)