# Estudio de Abogados:
 ### Gestión de Procesos y Clientes para Estudios Jurídicos

![Abogados](abogados.jpg)

# Índice

1. [Funcionalidades Principales](#funcionalidades-principales)
2. [Requisitos](#requisitos)
3. [Modo de uso](#modo-de-uso)
4. [Estructura del Proyecto](#estructura-del-proyecto)
5. [Imagenes](#images)
6. [Archivos Principales](#archivos-principales)
7. [Notas](#notas)
8. [Contacto](#contacto)
9. [Tecnologías utilizadas](#tecnolog%C3%ADas-utilizadas)

Este proyecto consiste en una aplicación desarrollada con Python, Pandas y Streamlit que facilita la gestión integral de un estudio jurídico. La aplicación permite a los usuarios agregar, visualizar y gestionar datos relacionados con juicios, procesos, clientes y abogados. Además, proporciona funcionalidades para mantener un control de los vencimientos de los procesos y emitir avisos pertinentes.

## Funcionalidades Principales

1. **Gestión de Juicios y Procesos:**
   - **Agregar y Visualizar Juicios:** Permite ingresar nuevos juicios y consultar información detallada de los juicios existentes.
   - **Administración de Procesos:** Gestión de los procesos asociados a cada juicio, incluyendo información sobre pruebas, movimientos y comentarios.

2. **Gestión de Clientes y Abogados:**
   - **Registrar y Consultar Clientes:** Agrega información detallada de los clientes, tanto personas físicas como empresas.
   - **Administración de Abogados:** Registro y consulta de abogados asociados al estudio.

3. **Control de Vencimientos:**
   - **Avisos de Vencimientos:** Mantiene un control sobre las fechas de vencimiento de los procesos, emitiendo avisos y recordatorios.

4. **Gestión Financiera:**
   - **Visualización de Gastos y Cobros:** Muestra listas de gastos y cobros asociados a los procesos, permitiendo el filtrado y la descarga de datos.
   - **Creación de Tipos de Gastos y Cobros:** Permite la adición de nuevos tipos de gastos y cobros directamente desde la interfaz.

5. **Descarga de Datos:**
   - **Exportación a Excel:** Los datos filtrados pueden ser descargados en formato Excel para un análisis adicional.



## Requisitos

Asegúrate de tener Python 3.x instalado y las siguientes bibliotecas requeridas:

- Pandas
- Streamlit


Puedes instalar las dependencias con el siguiente comando:

```
pip install pandas streamlit
```

## Modo de uso

### Cómo Inicializar en tu PC.

Para ejecutar esta aplicación en tu máquina local, sigue estos pasos:

1. Clona este repositorio en tu sistema local.
```
    git clone <URL-del-repositorio>
    cd nombre-del-repositorio
```

2. **Instalar Dependencias:**

    Asegúrate de tener Python y pip instalados. Luego, instala las dependencias necesarias ejecutando:
```
    pip install -r requirements.txt
```
3. **Ejecutar la Aplicación:**

    Una vez que todas las dependencias estén instaladas, puedes ejecutar la aplicación usando Streamlit:

```
    streamlit run main.py
```

4. **Interactuar con la Aplicación:**

    Abre tu navegador y visita http://localhost:8501 para ver y utilizar la aplicación.



    ![Modo de Uso](gifs/usage.gif)


## Estructura del Proyecto

La aplicación se organiza a través de un menú principal con las siguientes opciones:

**1. Principal:**

- Indicaciones de uso y diccionario de las tablas y el significado de las columnas.

**2. Vencimientos:**

Muestra los procesos que están próximos a vencerse.

**3. Juicios:**

-Permite agregar, observar y gestionar juicios.

**4. Procesos:**

- Similar a "Juicios", permite agregar, observar y gestionar procesos dentro de cada juicio.

**5. Clientes:**

- Se divide en "Personas Físicas" y "Empresas". Permite seleccionar, filtrar y crear registros.

**6. Abogados:**

- Similar a "Clientes", permite gestionar la información de los abogados del estudio.

**7. Gastos y Cobros:**

- Permite observar y crear tipos de gastos y cobros asociados a los procesos.

**8. Escritos:**

- Los usuarios pueden subir escritos para ser modificados y 
gestionados.


## Imagenes

![Menú Principal](Menu.PNG)
![Juicios](Juicios.PNG)
![Procesos](Procesos.PNG)


## Archivos Principales

**- main.py:** 
  Archivo principal que contiene el código de la aplicación.

**Archivos Excel (.xlsx):**
   - Abogados.xlsx
   - Clientes.xlsx
   - Cobros.xlsx
   - Empresas.xlsx
   - Estado Civil.xlsx
   - Exp Fisico.xlsx
   - Fueros.xlsx
   - Gastos.xlsx
   - Juicios.xlsx
   - Movimientos.xlsx
   - Nacionalidad.xlsx
   - Procesos.xlsx
   - Imágenes (.jpg y .png): Utilizadas en la interfaz de usuario.
Notas
Asegúrate de mantener actualizados los archivos Excel en el directorio raíz del proyecto para que la aplicación funcione correctamente.


## Notas

Asegúrate de mantener actualizados los archivos Excel en el directorio raíz del proyecto para que la aplicación funcione correctamente.

## Contacto

### Blas Fernando Pacios

[   ![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)
](https://www.linkedin.com/in/blas-fernando-pacios) 
[![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)
](https://wa.me/5493815467488)

## Tecnologías utilizadas


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

---


