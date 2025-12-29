import hashlib
import torch
from config import PATCH_H, PATCH_W

def key_to_coords(secret_key: str, image_shape):
    h, w = image_shape

    seed = int(
        hashlib.sha256(secret_key.encode()).hexdigest(),
        16
    ) % (2**32)

    gen = torch.Generator().manual_seed(seed)

    x = torch.randint(0, h - PATCH_H, (1,), generator=gen).item()
    y = torch.randint(0, w - PATCH_W, (1,), generator=gen).item()

    return x, y