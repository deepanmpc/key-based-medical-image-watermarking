import torch
import numpy as np
from config import PATCH_H, PATCH_W

def text_to_tensor(text: str):
    max_chars = PATCH_H * PATCH_W
    text = text[:max_chars].ljust(max_chars)

    ascii_vals = [ord(c) / 255.0 for c in text]
    tensor = torch.tensor(ascii_vals, dtype=torch.float32)
    return tensor.view(1, 1, PATCH_H, PATCH_W)

def tensor_to_text(tensor: torch.Tensor):
    chars = (
        tensor.view(-1)
        .cpu()
        .numpy() * 255
    ).round().clip(0, 255).astype(np.uint8)

    return bytes(chars).decode("utf-8", errors="ignore").strip()