# TP1 - Visualización de Intervalos de Medición

Este proyecto es una herramienta diseñada para automatizar el procesamiento de datos experimentales obtenidos en el laboratorio de física. El programa lee mediciones desde un archivo JSON, calcula la propagación de errores e incertidumbres, y genera gráficos comparativos para analizar la precisión entre diferentes instrumentos de medición (Regla vs. Calibre).

## 🚀 Características

El programa genera tres gráficos comparativos automáticos:
1.  **Comparativa de Altura (H):** Muestra el intervalo de error de la altura medida con regla frente a la medida con calibre.
2.  **Comparativa de Diámetro (D):** Visualiza la diferencia de precisión en las medidas del diámetro.
3.  **Comparativa de Volumen (V):** Calcula y grafica el volumen del cilindro con su respectiva propagación de error derivado de las medidas iniciales.

## 🛠️ Requisitos previos

Asegúrate de tener instalado Python en tu sistema. Además, este proyecto utiliza `matplotlib` para la generación de gráficos. Puedes instalar las dependencias necesarias ejecutando:

```bash
pip install matplotlib
```

## 📂 Estructura del Proyecto

*   `main.py`: Punto de entrada del programa. Coordina la lógica y la generación de gráficos.
*   `logic/`: Contiene los módulos de cálculo (`calcValueErr.py`, `calcCilinder.py`, etc.) encargados de la matemática detrás de los intervalos.
*   `utils/`: Funciones auxiliares para cargar el JSON y configurar el estilo de los gráficos.
*   `data/medidas.json`: Archivo de entrada donde se deben registrar las mediciones y el error instrumental.
*   `IniciarPrograma.bat`: Script de Windows para ejecutar el programa fácilmente con un doble clic.

## 📊 Uso

1.  **Preparar los datos:** Edita el archivo `data/medidas.json` con tus mediciones reales. El formato esperado es:
    ```json
    {
      "regla": {
        "medida": { "altura": 10.0, "diametro": 5.0 },
        "err": 0.1
      },
      "calibre": {
        "medida": { "altura": 10.05, "diametro": 5.02 },
        "err": 0.02
      }
    }
    ```
2.  **Ejecutar:** 
    *   En Windows: Haz doble clic en `IniciarPrograma.bat`.
    *   Desde la terminal: `python main.py`.

## 📈 Metodología de Cálculo

El software aplica las normas de cátedra para el redondeo de cifras significativas y el cálculo de errores relativos (épsilon), asegurando que el intervalo de confianza graficado sea científicamente correcto según los estándares de laboratorio.

---

<div align="center">

**Ramón Ramírez · UTN-FRBA · 2026**  