
# Evaluación Final - Aplicación Web con Flask

Este proyecto corresponde al **Examen** de la asignatura **Programación Web**.  
La aplicación fue desarrollada utilizando **Python** y **Flask**, incorporando un menú principal con dos ejercicios y una página con link directo al repositorio.

## Descripción del proyecto

La aplicación permite acceder a dos ejercicios:

- **Ejercicio 1:** cálculo del total de compra de tarros de pintura aplicando descuentos según la edad del cliente.
  
  - Cada tarro tiene un valor de $9000.
  - Personas entre 18 y 30 años reciben un descuento del 15%.
  - Personas mayores de 30 años reciben un descuento del 25%.
  - Menores de 18 años **no reciben descuento**.
  
  El sistema muestra:
  - Nombre del cliente
  - Total sin descuento
  - Monto descontado
  - Porcentaje de descuento aplicado
  - Total final a pagar

- **Ejercicio 2:** validación de usuarios registrados mediante usuario y contraseña.
  
  Usuarios disponibles:
  
  - Usuario: `juan`
    Contraseña: `admin`
  
  - Usuario: `pepe`
    Contraseña: `user`
  
  Dependiendo de los datos ingresados, el sistema muestra un mensaje de bienvenida o un mensaje de error.

- **Repositorio:** página breve con link directo al repositorio del proyecto.

## Estructura del proyecto

```bash
ev3/
│
├── main.py
├── templates/
│   ├── index.html
│   ├── ejercicio1.html
│   ├── ejercicio2.html
│   └── repositorio.html
│
├── static/
│   └── style.css
│
└── README.md
```


## Requisitos

- Python 3 instalado
- Flask instalado mediante pip

## Instalación de Flask
En la terminal ejecutar:
```py -m pip install flask```

## Ejecución del proyecto
Desde la carpeta del proyecto ejecutar:
```py main.py```

## Luego abrir en el navegador:
```http://127.0.0.1:5000/```