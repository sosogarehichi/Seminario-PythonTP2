# Seminario-PythonTP2
Garehichi Sofia
23668/8

## Ejercicio 10

En este ejercicio se imprimen los resultados de varias rondas, generando rankings y determinando los MVPs en base al puntaje, permitiendo ver el progreso del equipo.

El codigo de las funciones necesarias se encuentra en el directorio `src`, mientras que los notebooks estan en la carpeta `notebooks`.

## Instalacion de Dependencias

Para ejecutar este proyecto, se recomienda crear un entorno virtual y luego instalar las dependencias necesarias.

### 1. Crear un entorno virtual
Por convención se tiene el entorno virtual dentro el repositorio y del proyecto.
Para crearlo se utiliza el comando:
python -m venv venv
- m de módulo
- venv el módulo que se quiere ejecutar
- venv el nombre de la carpeta en la que se van a guardar las cosas

```bash
python -m venv venv
```

### 2. Activar y Desactivar el entorno virtual
- En Windows:
  ```bash
  source venv\Scripts\activate
  ```
- En macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

- Para desactivar el entorno virtual:
  ```
    deactivate
  ```

### 3. Instalar dependencias
Ejecuta el siguiente comando en la terminal dentro del proyecto:
```bash
pip install -r requirements.txt
```
Si el archivo `requirements.txt` no está presente, puedes generarlo con:
```bash
pip freeze > requirements.txt
```

### Detalle importante
Se debe agregar la carpeta venv al .gitignore debido a la cantidad de carpetas que contiene.

## Ejecución del Proyecto

Si se desea trabajar desde un **notebook**, asegurate de estar en el entorno virtual y luego abre Jupyter Notebook:
```bash
jupyter notebook
```
Dentro de Jupyter, navega hasta la carpeta `notebooks` y abre el archivo correspondiente.

## Estructura del Proyecto
```
proyecto/
│── notebooks/             # Notebooks
│   ├── ejercicio10.ipynb  # Código fuente del ejercicio
│── src/                   # Carpeta src
│   ├── __init__.py        # Para indicar que es un paquete
│   ├── funciones.py       # Modulo con funciones principales
│── requirements.txt       # Dependencias del proyecto
│── README.md              # Instrucciones y documentación
```
