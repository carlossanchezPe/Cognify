# CognifyProject

## Descripción
Cognify es un sistema para la rehabilitación de criminales mediante la implantación de recuerdos artificiales. Este enfoque permite cumplir sentencias largas en pocos minutos, simulando experiencias de empatía y arrepentimiento para facilitar la rehabilitación.

## Funcionalidades
- **Agregar criminales** al sistema, especificando su nombre y tipo de delito.
- **Asignar recuerdos** específicos a cada criminal basados en el tipo de delito cometido.
- **Mostrar recuerdos** asignados a cada criminal para revisar sus experiencias de rehabilitación.

## Requisitos
- **Python 3.x** instalado en tu sistema.

## Instalación
1. Clona el repositorio en tu máquina local:
   ```bash
   git clone https://github.com/carlossanchezPe/Cognify.git

Navega a la carpeta del proyecto:
cd Cognify

Ejecuta el programa desde la terminal:

python main.py

El programa mostrará un menú con las siguientes opciones:
===== Sistema Cognify =====
1. Agregar criminal
2. Asignar recuerdo
3. Mostrar recuerdos de un criminal
4. Salir

Opción 1: Agregar criminal

Ingrese el nombre del criminal: Juan Pérez
Ingrese el tipo de delito (violento/financiero/odio): violento


Asignar recuerdo

Recuerdo asignado a Juan Pérez: Empatía y sufrimiento de la víctima.

Mostrar recuerdos de un criminal

Recuerdos de Juan Pérez:
- Empatía y sufrimiento de la víctima


===== Sistema Cognify =====
1. Agregar criminal
2. Asignar recuerdo
3. Mostrar recuerdos de un criminal
4. Salir
Seleccione una opción: 1
Ingrese el nombre del criminal: Carlos López
Ingrese el tipo de delito (violento/financiero/odio): violento
Criminal agregado correctamente.

Seleccione una opción: 2
Criminales disponibles:
1. Carlos López (violento)
Seleccione el número del criminal: 1
Recuerdo asignado a Carlos López.

Seleccione una opción: 3
Recuerdos de Carlos López:
- Empatía y sufrimiento de la víctima


Estructura del Proyecto
model/: Contiene las clases de modelo (Criminal, Memory, CrimeType, ConfiguracionGlobal).
view/: Contiene la interfaz de usuario (InterfazCognify).
controller/: Contiene el controlador principal (ControladorCognify).
main.py: Archivo principal para ejecutar el programa.
