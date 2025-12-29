from pipeline.embed_pipeline import embed_pipeline
from pipeline.verify_pipeline import verify_pipeline

IMAGE = "data/input_image.png"
OUT_IMAGE = "data/watermarked_image.png"

PATIENT_INFO = "Name: Rajesh Tulasi | ID: 2300 | DOB: 2000-01-01"
SECRET_KEY = "Doctor_One_Private_Key"

embed_pipeline(
    IMAGE,
    PATIENT_INFO,
    SECRET_KEY,
    OUT_IMAGE
)

decoded = verify_pipeline(OUT_IMAGE, SECRET_KEY)

print("Decoded Patient Info:")
print(decoded)