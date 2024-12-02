import torch
from model import SpeechToTextModel
from data_loader import get_data_loader
from feature_extraction import extract_features
from sklearn.metrics import accuracy_score

def evaluate_model(data_dir, transcripts_dir):
    data_loader = get_data_loader(data_dir, transcripts_dir, batch_size=16)
    model = SpeechToTextModel(input_dim=40, hidden_dim=128, output_dim=len("abcdefghijklmnopqrstuvwxyz "))
    model.load_state_dict(torch.load("model.pth"))
    model.eval()

    all_preds = []
    all_labels = []

    with torch.no_grad():
        for waveform, sample_rate, transcript in data_loader:
            features = extract_features(waveform, sample_rate)
            output = model(features)
            preds = output.argmax(dim=-1)
            all_preds.extend(preds)
            all_labels.extend(transcript)

    # قياس الأداء (يمكنك تعديل المقاييس بناءً على الحاجة)
    accuracy = accuracy_score(all_labels, all_preds)
    print(f"Model Accuracy: {accuracy:.4f}")

if __name__ == "__main__":
    evaluate_model("data/processed", "data/transcripts/transcripts.txt")
