# Simulacion de una cola M/M/1

Este proyecto ejecuta una simulacion de una cola M/M/1 con un solo servidor.
El archivo `servidor_web_mm1.py` muestra los promedios simulados de espera en
cola y tiempo en el sistema, y los compara con sus valores teoricos.

## Requisitos

- Python 3.10 o posterior
- `pip`

La unica dependencia externa es SimPy. Se instala desde `requirements.txt`.

## Ejecucion en Windows (PowerShell)

Abre PowerShell en esta carpeta y ejecuta:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python servidor_web_mm1.py
```

Si PowerShell bloquea la activacion del entorno, puedes ejecutar el programa
sin activarlo:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe servidor_web_mm1.py
```

## Ejecucion en macOS o Linux

Abre una terminal en esta carpeta y ejecuta:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python servidor_web_mm1.py
```

Los resultados de la simulacion pueden variar entre ejecuciones porque los
tiempos entre llegadas y de servicio son aleatorios. Los valores teoricos se
imprimen como referencia.

## Archivos del proyecto

- `servidor_web_mm1.py`: codigo de la simulacion.
- `requirements.txt`: dependencias necesarias para instalar.
- `.gitignore`: excluye entornos virtuales y archivos temporales de Python.

No es necesario compartir la carpeta `venv` o `.venv`: cada usuario debe crear
su propio entorno siguiendo los pasos anteriores.
