import os
import sys
import speech_recognition as sr
import subprocess
import datetime
import pyttsx3

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
    return f"Archivo JS creado en: la ruta especificada"

def reconocer_voz(proyecto_dir, engine):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)  # Ajustar para ruido ambiente
    
        print("La aplicación está escuchando. Presiona Ctrl+C para detenerla.")
        engine.say("La aplicación está escuchando. Presiona Ctrl+C para detenerla.")
        engine.runAndWait()

        while True:
            print("Esperando comando...")
            audio = recognizer.listen(source)

            try:
                texto = recognizer.recognize_google(audio, language='es-ES')
                print(f'Dijiste: "{texto}"')
                engine.say(f'Dijiste: "{texto}"')
                engine.runAndWait()

                if "hazme un commit" in texto.lower():
                    print("¡Realizando commit y push en el proyecto!")
                    engine.say("Realizando commit y push en el proyecto")
                    engine.runAndWait()
                    mensaje = crear_archivo_js(proyecto_dir)
                    engine.say(mensaje)
                    engine.runAndWait()

                    os.chdir(proyecto_dir)
                    subprocess.run(['git', 'add', '.'])
                    subprocess.run(['git', 'commit', '-m', '"Nuevo commit"'])
                    subprocess.run(['git', 'push'])

                    print("Commit y push realizados exitosamente.")
                    engine.say("Commit y push realizados exitosamente")
                    engine.runAndWait()
                else:
                    continue  # Si no es "hazme un commit", vuelve al inicio del bucle

            except sr.UnknownValueError:
                print("No se pudo entender lo que dijiste")
                engine.say("No se pudo entender lo que dijiste")
                engine.runAndWait()
            except sr.RequestError as e:
                print(f"Error en la solicitud al servicio de reconocimiento de voz: {e}")
                engine.say(f"Error en la solicitud al servicio de reconocimiento de voz: {e}")
                engine.runAndWait()
            except KeyboardInterrupt:
                print("Programa detenido por el usuario.")
                engine.say("Programa detenido por el usuario.")
                engine.runAndWait()
                break
            except Exception as e:
                print(f"Otro error: {e}")
                engine.say(f"Otro error: {e}")
                engine.runAndWait()

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    # Si el script está empaquetado como ejecutable, usa pythonw.exe
    pythonw_path = os.path.join(sys._MEIPASS, 'pythonw.exe')
    subprocess.Popen([pythonw_path, __file__])
else:
    proyecto_dir = r"C:\Users\Geodev\Documents\pythonProyects\prueba1"
    engine = pyttsx3.init()

    try:
        reconocer_voz(proyecto_dir, engine)
    except KeyboardInterrupt:
        print("Programa detenido por el usuario.")
        engine.say("Programa detenido por el usuario.")
        engine.runAndWait()
