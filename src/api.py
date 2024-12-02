from fastapi import FastAPI, File, UploadFile
import torchaudio
from model import SpeechToTextModel

app = FastAPI()
model = SpeechToTextModel(input_dim=40, hidden_dim=128, output_dim=len("abcdefghijklmnopqrstuvwxyz "))

@app.post("/speech-to-text/")
async def speech_to_text(file: UploadFile = File(...)):
    waveform, sample_rate = torchaudio.load(file.file)
    features = extract_features(waveform, sample_rate)
    result = model(features)
    return {"transcript": result}
