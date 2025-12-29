from utils.text_codec import tensor_to_text
from utils.key_hash import key_to_coords
from config import PATCH_H, PATCH_W

class WatermarkDecoder:
    def extract(self, image, key):
        _, _, h, w = image.shape
        x, y = key_to_coords(key, (h, w))

        patch = image[:, :, x:x+PATCH_H, y:y+PATCH_W]
        return tensor_to_text(patch)