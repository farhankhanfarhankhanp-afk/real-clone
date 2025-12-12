import gradio as gr
import torch
from TTS.api import TTS

# ماڈل لوڈ (پہلی بار تھوڑا ٹائم لے گا)
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)

def voice_clone(reference_audio, text, language="ur"):
    output_path = "output.wav"
    tts.tts_to_file(text=text,
                    speaker_wav=reference_audio,
                    language=language,
                    file_path=output_path)
    return output_path

with gr.Blocks(title="فرحان کا Voice Clone 🔥") as demo:
    gr.Markdown("# فرحان کا فری وائس کلونر 🇵🇰")
    gr.Markdown("اپنی ۵-۱۰ سیکنڈ آواز دو → جو مرضی لکھو → وہی آواز میں بولے گا!")
    
    with gr.Row():
        audio_input = gr.Audio(label="اپنی آواز ریکارڈ کرو یا اپ لوڈ کرو", type="filepath")
        text_input = gr.Textbox(label="یہاں لکھو جو بولنا ہے", placeholder="سلام علیکم، میرا نام فرحان ہے...", lines=3)
    
    btn = gr.Button("🔥 Generate کرو – میری آواز میں بولو!", variant="primary")
    output = gr.Audio(label="تیار شدہ آواز سنو")
    
    btn.click(voice_clone, inputs=[audio_input, text_input], outputs=output)
    
    gr.Markdown("بنایا ہے فرحان خان نے ❤️")

demo.launch()
