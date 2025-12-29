import cv2
import torch
from watermark.decoder import WatermarkDecoder
from config import IMAGE_SIZE

def verify_pipeline(image_path, secret_key):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, IMAGE_SIZE)

    img_tensor = torch.tensor(img / 255.0).float().unsqueeze(0).unsqueeze(0)

    decoder = WatermarkDecoder()
    return decoder.extract(img_tensor, secret_key)