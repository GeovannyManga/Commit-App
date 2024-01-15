import os
import speech_recognition as sr
import subprocess
import datetime

def crear_archivo_js(proyecto_dir):
    # Generar un nombre de archivo único basado en la fecha y hora
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo_js = f"nuevo_archivo_{timestamp}.js"

    # Contenido del nuevo archivo JS
    contenido_js = f"""
    // Contenido del archivo JS
    console.log("Hola, este es un nuevo archivo JS creado automáticamente en {timestamp}.");
    """

    # Ruta del nuevo archivo JS
    ruta_archivo_js = os.path.join(proyecto_dir, nombre_archivo_js)

    # Crear y escribir en el archivo JS
    with open(ruta_archivo_js, "w") as archivo_js:
        archivo_js.write(contenido_js)

    print(f"Archivo JS creado en: {ruta_archivo_js}")

def reconocer_voz():
    recognizer = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Esperando comando...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            texto = recognizer.recognize_google(audio, language = 'ES')
            print(f'Dijiste: "{texto}"')

            if "hazme un commit" in texto.lower():
                print("¡Realizando commit y push en el proyecto!")

                proyecto_dir = r"C:\Users\Geodev\Documents\pythonProyects\prueba1"

                # Crear el archivo JS antes de hacer el commit y push
                crear_archivo_js(proyecto_dir)

                # Cambiar al directorio del proyecto
                os.chdir(proyecto_dir)

                # Ejecutar los comandos de Git
                subprocess.run(['git', 'add', '.'])
                subprocess.run(['git', 'commit', '-m', '"Nuevo commit"'])
                subprocess.run(['git', 'push'])
                
                print("Commit y push realizados exitosamente.")
                break
        except sr.UnknownValueError:
            print("No se pudo entender lo que dijiste")
        except sr.RequestError as e:
            print(f"Error en la solicitud al servicio de reconocimiento de voz: {e}")
        except Exception as e:
            print(f"Otro error: {e}")

if __name__ == "__main__":
    reconocer_voz()
