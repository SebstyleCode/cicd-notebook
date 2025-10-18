# App/app.py
import gradio as gr
import time

# --- Simulación de la función de predicción ---
# En un proyecto real, aquí cargarías tu modelo ("Model/model.pkl")
# y lo usarías para hacer predicciones.
def predict(age, sex, blood_pressure, cholesterol, na_to_k):
    # Simplemente devolvemos una respuesta de ejemplo después de una pausa
    time.sleep(1)
    # El tipo de droga se elige de forma simulada basado en la edad
    if age < 30:
        return "Drug A"
    elif age < 50:
        return "Drug B"
    else:
        return "Drug C"

# --- Creación de la Interfaz de Gradio ---
with gr.Blocks() as demo:
    gr.Markdown("# Drug Classification")
    gr.Markdown("Enter the details to correctly identify Drug type?")

    with gr.Row():
        with gr.Column():
            age = gr.Slider(minimum=15, maximum=74, label="Age")
            sex = gr.Radio(["M", "F"], label="Sex")
            blood_pressure = gr.Radio(["HIGH", "LOW", "NORMAL"], label="Blood Pressure")
            cholesterol = gr.Radio(["HIGH", "NORMAL"], label="Cholesterol")
            na_to_k = gr.Slider(minimum=6.2, maximum=38.2, label="Na_to_K")
            
            with gr.Row():
                clear_button = gr.ClearButton()
                submit_button = gr.Button("Submit", variant="primary")

        with gr.Column():
            output_label = gr.Label(label="Output")

    gr.Examples(
        examples=[
            [30, "M", "HIGH", "NORMAL", 15.4],
            [35, "F", "LOW", "NORMAL", 8],
            [50, "M", "HIGH", "HIGH", 34],
        ],
        inputs=[age, sex, blood_pressure, cholesterol, na_to_k],
        outputs=output_label,
        fn=predict,
        cache_examples=False,
    )

    submit_button.click(
        fn=predict,
        inputs=[age, sex, blood_pressure, cholesterol, na_to_k],
        outputs=output_label,
    )

demo.launch()