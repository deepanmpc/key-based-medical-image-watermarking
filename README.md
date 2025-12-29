# Medical Image Watermarking (RSA-based)

This small demo embeds an RSA signature of a message into the LSBs of an image's blue channel and verifies it.

Quick start:

1. Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

2. Place an input image at `data/input_image.png` (PNG recommended).

3. Embed a watermark (this will generate keys and write `data/private_key.pem` and `data/public_key.pem`):

```bash
python3 main.py embed -m "patient-id:123" --generate-keys
```

4. Verify:

```bash
python3 main.py verify
```
