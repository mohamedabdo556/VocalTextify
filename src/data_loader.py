import os
import torchaudio
from torch.utils.data import Dataset, DataLoader

class SpeechDataset(Dataset):
    def __init__(self, data_dir, transcripts_dir):
        self.audio_files = [os.path.join(data_dir, f) for f in os.listdir(data_dir)]
        self.transcripts = self._load_transcripts(transcripts_dir)

    def _load_transcripts(self, transcripts_dir):
        with open(transcripts_dir, 'r') as file:
            return file.readlines()

    def __len__(self):
        return len(self.audio_files)

    def __getitem__(self, idx):
        waveform, sample_rate = torchaudio.load(self.audio_files[idx])
        transcript = self.transcripts[idx].strip()
        return waveform, sample_rate, transcript

def get_data_loader(data_dir, transcripts_dir, batch_size):
    dataset = SpeechDataset(data_dir, transcripts_dir)
    return DataLoader(dataset, batch_size=batch_size, shuffle=True)
