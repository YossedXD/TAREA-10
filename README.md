# Simulaciones PyBullet dockerizadas 🐋

Autores: Yossed Riaño, Jeferson Hernández, Miguel Montaña  
Universidad Santo Tomás — 2025  

Este trabajo presenta la dockerización de tres ejemplos desarrollados en clase usando **PyBullet**:

- **brazo.py** → Brazo robótico KUKA IIWA  
- **carrito.py** → Vehículo deslizante (cubo móvil)  
- **volador.py** → Dron / cubo flotante  

Cada simulación se ejecuta en un contenedor Docker con interfaz gráfica (usando VcXsrv en Windows o X11 en Linux).

---

## Requisitos previos

### Windows
1. Instalar **Docker Desktop** → [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
2. Instalar **VcXsrv** → [https://sourceforge.net/projects/vcxsrv/](https://sourceforge.net/projects/vcxsrv/)
3. Al abrir VcXsrv, seleccionar *Disable access control*.
4. Abrir PowerShell o Visual Studio Code en la carpeta donde estén los archivos `.py` y sus `Dockerfile`.

### Linux
1. Instalar Docker con tu gestor de paquetes.
2. Permitir acceso gráfico:
   ```bash
   xhost +local:docker
   ```

---

##  Construcción y ejecución de simulaciones

###  1. Brazo Robótico (KUKA IIWA)
**Archivo:** `brazo.py`  
**Dockerfile:**
```dockerfile
FROM python:3.10-slim
RUN apt-get update && apt-get install -y xvfb x11-apps libgl1 \
    && pip install pybullet \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY brazo.py .
CMD ["python", "brazo.py"]
```
**Construcción:**
```bash
docker build -t brazo-pybullet -f Dockerfile.brazo .
```
**Ejecución (Windows):**
```bash
docker run -it --rm -e DISPLAY=host.docker.internal:0.0 brazo-pybullet
```
**Ejecución (Linux):**
```bash
docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix brazo-pybullet
```
 *Captura de ejecución:* `<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/d5d6e998-a7b2-41d7-b39f-ce393a3772a7" />
`  
*Captura dockerización:* `<img width="1116" height="221" alt="image" src="https://github.com/user-attachments/assets/ba05d205-600d-41b9-ac1a-78e0689c1c58" />
`

---

###  2. Carrito Deslizante
**Archivo:** `carrito.py`  
**Dockerfile:**
```dockerfile
FROM python:3.10-slim
RUN apt-get update && apt-get install -y xvfb x11-apps libgl1 \
    && pip install pybullet \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY carrito.py .
CMD ["python", "carrito.py"]
```
**Construcción:**
```bash
docker build -t carrito-pybullet -f Dockerfile.carrito .
```
**Ejecución (Windows):**
```bash
docker run -it --rm -e DISPLAY=host.docker.internal:0.0 carrito-pybullet
```
**Ejecución (Linux):**
```bash
docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix carrito-pybullet
```
*Captura de ejecución:* `<img width="1269" height="965" alt="image" src="https://github.com/user-attachments/assets/7cc41872-fdab-4eea-a08f-d12032be0512" />
`  
*Captura dockerización:* `<img width="1064" height="179" alt="image" src="https://github.com/user-attachments/assets/695639c3-b661-48d9-b3e9-5b38821c2167" />
`

---

###  3. Volador (Dron simple)
**Archivo:** `volador.py`  
**Dockerfile:**
```dockerfile
FROM python:3.10-slim
RUN apt-get update && apt-get install -y xvfb x11-apps libgl1 \
    && pip install pybullet \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY volador.py .
CMD ["python", "volador.py"]
```
**Construcción:**
```bash
docker build -t volador-pybullet -f Dockerfile.volador .
```
**Ejecución (Windows):**
```bash
docker run -it --rm -e DISPLAY=host.docker.internal:0.0 volador-pybullet
```
**Ejecución (Linux):**
```bash
docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix volador-pybullet
```
 *Captura de ejecución:* `<img width="1271" height="972" alt="image" src="https://github.com/user-attachments/assets/71c03e5c-b75a-47b9-aec1-aa971dd31694" />
`  
 *Captura dockerización:* `<img width="1058" height="239" alt="image" src="https://github.com/user-attachments/assets/7dd145e5-0ab6-463e-a572-3f356fd13dfc" />
`

---

## Solución de problemas

| Error | Solución |
|-------|-----------|
| the Dockerfile cannot be empty | Verifica que esté guardado y en la ruta correcta |
| libgl1-mesa-glx no disponible | Sustituir por libgl1 |
| No se ve la ventana | Ejecuta VcXsrv con *Disable access control* |
| Error X11 en Linux | Ejecuta `xhost +local:docker` antes de `docker run` |
| PyBullet no abre | Ejecuta `docker build --no-cache` |

---

## Referencias
- [PyBullet](https://pybullet.org/wordpress/)  
- [Docker Documentation](https://docs.docker.com/)  
- [VcXsrv](https://sourceforge.net/projects/vcxsrv/)  



## 🧾 Licencia
Trabajo académico – Universidad Santo Tomás 2025.
