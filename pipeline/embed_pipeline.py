import cv2
import torch
from watermark.encoder import WatermarkEncoder
from config import IMAGE_SIZE

def embed_pipeline(image_path, patient_info, secret_key, output_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, IMAGE_SIZE)

    img_tensor = torch.tensor(img / 255.0).float().unsqueeze(0).unsqueeze(0)

    encoder = WatermarkEncoder()
    watermarked = encoder.embed(img_tensor, patient_info, secret_key)

    out_img = (watermarked.squeeze().numpy() * 255).astype("uint8")
    cv2.imwrite(output_path, out_img)