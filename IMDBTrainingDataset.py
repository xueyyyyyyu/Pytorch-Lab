import pandas as pd
from torch.utils.data import Dataset


class IMDBTrainingDataset(Dataset):
    def __init__(self, train_file, transform=None, target_transform=None):
        self.vectors_labels = pd.read_csv(train_file)

    def __len__(self):
        return len(self.vectors_labels)

    def __getitem__(self, idx):
        vector = self.vectors_labels.iloc[idx, 0]
        label = self.vectors_labels.iloc[idx, 1]
        return vector, label

