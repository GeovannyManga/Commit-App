import os
import subprocess
import datetime
import random
import time

def contar_archivos_js(proyecto_dir):
    archivos_js = [archivo for archivo in os.listdir(proyecto_dir) if archivo.endswith(".js")]
    return len(archivos_js)

def eliminar_archivos_js(proyecto_dir, limite):
    archivos_js = [archivo for archivo in os.listdir(proyecto_dir) if archivo.endswith(".js")]
    
    if len(archivos_js) > limite:
        print(f"Eliminando archivos .js (total: {len(archivos_js)})...")
        for archivo in archivos_js:
            ruta_archivo = os.path.join(proyecto_dir, archivo)
            os.remove(ruta_archivo)
        print("Archivos .js eliminados.")

def crear_archivo_js(proyecto_dir):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo_js = f"nuevo_archivo_{timestamp}.js"
    contenido_js = f"""
    // Contenido del archivo JS
    console.log("Hola, este es un nuevo archivo JS creado automáticamente en {timestamp}.");
    """
    ruta_archivo_js = os.path.join(proyecto_dir, nombre_archivo_js)
    with open(ruta_archivo_js, "w") as archivo_js:
        archivo_js.write(contenido_js)
    return f"Archivo JS creado en: {ruta_archivo_js}"

def realizar_commit_push(proyecto_dir, num_commits):
    os.chdir(proyecto_dir)
    
    for _ in range(num_commits):
        subprocess.run(['git', 'commit', '--allow-empty', '-m', '"Nuevo commit"'])
        time.sleep(1)
    
    subprocess.run(['git', 'push'])

proyecto_dir = r"C:\Users\Geodev\Documents\pythonProyects\prueba1"
limite_archivos_js = 20

while True:
    try:
        now = datetime.datetime.now()

        # Verificar si es las 10:00 AM
        if now.hour == 20 and now.minute == 10:
            # Eliminar archivos .js si superan el límite
            eliminar_archivos_js(proyecto_dir, limite_archivos_js)

            # Generar un número aleatorio de commits entre 10 y 25
            num_commits = random.randint(10, 25)

            print(f"Realizando {num_commits} commits y push en el proyecto - {now}")

            mensaje = crear_archivo_js(proyecto_dir)
            print(mensaje)

            realizar_commit_push(proyecto_dir, num_commits)

            print("Commits y push realizados exitosamente.")
        
        # Esperar un minuto antes de verificar nuevamente
        time.sleep(60)

    except KeyboardInterrupt:
        print("Programa detenido por el usuario.")
        break
    except Exception as e:
        print(f"Error: {e}")
