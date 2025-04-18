from script_graph import ScriptGraph
import gradio as gr

script_graph = ScriptGraph()

# Function to create script from the content
def generate(content):
  return script_graph.create_script(content)

# Set up Gradio interface
with gr.Blocks() as iface:
  content = gr.TextArea(label="Content")
  script = gr.TextArea(label="Script")
  generate_btn = gr.Button("Generate")
  clear_btn = gr.ClearButton([content, script])
  generate_btn.click(fn=generate, inputs=content, outputs=script, api_name="generate")

# Launch the Gradio app
iface.launch(server_name="0.0.0.0", server_port=7860, share=False)
