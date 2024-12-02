import torch
import torch as nn
import torch.optim as optim
from model import SpeechToTextModel
from data_loader import get_data_loader
from feature_extraction import extract_features

def train_model(data_dir, transcripts_dir, epochs, batch_size):
    data_loader = get_data_loader(data_dir, transcripts_dir, batch_size)
    model = SpeechToTextModel(input_dim=40, hidden_dim=128, output_dim=len("abcdefghijklmnopqrstuvwxyz "))
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    criterion = nn.CTCLoss()

    for epoch in range(epochs):
        model.train()
        for waveform, sample_rate, transcript in data_loader:
            features = extract_features(waveform, sample_rate)
            # تحويل النصوص لتسلسل رقمي
            optimizer.zero_grad()
            output = model(features)
            # احسب الخسارة وقم بالتحديث
            loss = criterion(output, ...)
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch+1}, Loss: {loss.item()}")

if __name__ == "__main__":
    train_model("data/raw", "data/transcripts/transcripts.txt", epochs=10, batch_size=16)
