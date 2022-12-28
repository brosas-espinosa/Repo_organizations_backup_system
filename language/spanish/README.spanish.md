# Sistema de respaldo de repositorios de una organización en Github
Este es un script simple para realizar un respaldo local de todos los repositorios de una organización en Github.
---
Lenguajes:
<p align="center">
  <a href="https://github.com/brosas-espinosa/Repo_organizaztions_backup_system/blob/99d617aed1e1262e0a98d5790c96de5793fd9d05/README.md">English</a> |
  <span>Español</span> |
</p>

Necesitarás un par de cosas para que este script funcione:
- Opcional: Entorno virtual de Python
- Librería Requests
- Librería GitPython
- Token de la API de Github
- URL de los repositorios de la organización
- Llave SSH para tu cuenta

***
## Entorno virtual
Para crear y activar un entorno virtual en Windows, puedes hacerlo ejecutando los siguientes comandos:
```powershell
mkdir <venv-name>
python -m venv <venv-name>
Set-ExecutionPolicy Unrestricted -Scope Process
.\<venv-name>\Scripts\activate
```
Usa el comando `deactivate` para salir del entorno virtual.

Para crear y activar un entorno virtual en Linux, puedes hacerlo ejecutando los siguientes comandos:
```bash
python -m venv <venv-name>
source <venv-name>/bin/activate
```
Usa el comando `deactivate` para salir del entorno virtual.
## Librerías de Python
Para instalar las librerías necesarias puedes hacerlo ejecutando el siguiente comando:
```powershell
pip install -r requirements.txt
```
## Token de la API de Github
Para obtener el token de la API de Github, necesitarás ir a la configuración de tu cuenta y crear uno nuevo. Asegúrate de crearlo con los permisos necesarios (repo, admin:org, etc).
## URL de los repositorios de la organización
Para obtener la URL de los repositorios de la organización, necesitarás obedecer la siguiente estrutura:
```powershell
https://api.github.com/orgs/<nombre_de_la_organizacion>/repos
```
Nota: El script está diseñado para trabajar con múltiples organizaciones, por lo que puedes agregar tantas como quieras en la lista `LIST_URLS`.
## Llave SSH
La llave SSH se usa para clonar los repos, por lo que necesitarás crear una y agregarla a tu cuenta de Github. El método variará dependiendo de tu sistema operativo, solo recuerda usarla antes de ejecutar el script.
***
## Ejecución del script
Para ejecutar el script, necesitarás activar el entorno virtual y ejecutar el siguiente comando:
```powershell
python backup.py
```

## Estructura de los archivos
El script creará una carpeta con el nombre `repositories_backup`, después con el nombre de la organización y dentro de ella se crearán carpetas con el año, mes y fecha completa de la fecha en la que se ejecutó el script. Dentro de cada carpeta se creará una carpeta con el nombre del repositorio y dentro de ella se clonarán los archivos del repositorio.
```
<repositories_backup>
    <organization_name>
        <year>
            <month>
                <date>
                    <repo_name>
                        <repo_files>
```
Si quieres cambiar la ruta de respaldo, puedes hacerlo cambiando la variable `V_BACKUP_DIR` en el script.
