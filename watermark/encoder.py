import torch
from utils.text_codec import text_to_tensor
from utils.key_hash import key_to_coords
from config import PATCH_H, PATCH_W

class WatermarkEncoder:
    def embed(self, image: torch.Tensor, text: str, key: str):
        patch = text_to_tensor(text)

        _, _, h, w = image.shape
        x, y = key_to_coords(key, (h, w))

        watermarked = image.clone()
        watermarked[:, :, x:x+PATCH_H, y:y+PATCH_W] = patch

        return watermarked