import torchaudio.transforms as T

def extract_features(waveform, sample_rate):
    mfcc = T.MFCC(sample_rate=sample_rate, n_mfcc=40)
    return mfcc(waveform)
