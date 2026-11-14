#!/usr/bin/env python3
"""Extrae luces y sombras de las fotos de papel, sin generar pliegues.

Uso: python3 tools/extract-paper-textures.py /ruta/a/Downloads
Solo la regeneración de los recursos requiere Pillow y NumPy.
"""

import base64
import hashlib
import io
import json
from pathlib import Path
import sys

import numpy as np
from PIL import Image, ImageFilter


SOURCES = [
    ('photo-soft', 'Pliegues amplios · foto', 'white-crinkled-paper-texture-background.jpg'),
    ('photo-creased', 'Papel arrugado · foto', 'white-paper-texture-background(1).jpg'),
    ('photo-torn', 'Papel desgarrado · foto', 'white-paper-texture-background.jpg'),
    ('photo-glued-1', 'Papel pegado 1 · foto', 'papel pegado/papel pegado1.jpg'),
    ('photo-glued-2', 'Papel pegado 2 · foto', 'papel pegado/papel pegado2.jpg'),
    ('photo-glued-3', 'Papel pegado 3 · foto', 'papel pegado/papel pegado3.jpg'),
    ('photo-glued-4', 'Papel pegado 4 · foto', 'papel pegado/papel pegado4.jpg'),
    ('photo-glued-5', 'Papel pegado 5 · foto', 'papel pegado/papel pegado5.jpg'),
]


def extract(path):
    with Image.open(path) as source:
        original_size = source.size
        scale = min(1, 2400 / min(source.size))
        size = tuple(round(v * scale) for v in source.size)
        gray = source.convert('L').resize(size, Image.Resampling.LANCZOS)
    # Suprime el ruido de cámara conservando la posición de crestas y sombras.
    gray = gray.filter(ImageFilter.GaussianBlur(min(size) / 3200))
    baseline = gray.filter(ImageFilter.GaussianBlur(min(size) * 0.12))
    luminance = np.asarray(gray, dtype=np.float32)
    illumination = np.asarray(baseline, dtype=np.float32)
    # El cociente retira el blanco y la iluminación lenta; no estima alturas 3D.
    signal = np.log(np.maximum(luminance, 1) / np.maximum(illumination, 1))
    signal -= np.median(signal)
    signal = np.sign(signal) * np.maximum(0, np.abs(signal) - 0.002)
    packed = Image.fromarray(np.clip(np.rint(128 + 512 * signal), 0, 255).astype('uint8'))
    output = io.BytesIO()
    packed.save(output, format='JPEG', quality=96, optimize=True)
    return original_size, size, output.getvalue()


def main():
    source_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.home() / 'Downloads'
    target = Path(__file__).resolve().parents[1] / 'assets' / 'paper' / 'textures.js'
    textures = []
    for texture_id, label, filename in SOURCES:
        path = source_dir / filename
        original_size, size, data = extract(path)
        textures.append({
            'id': texture_id, 'label': label, 'source': filename,
            'sourceSize': original_size, 'width': size[0], 'height': size[1],
            'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
            'data': 'data:image/jpeg;base64,' + base64.b64encode(data).decode('ascii'),
        })
        print(f'{filename}: {original_size} → {size}, {len(data):,} bytes')
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        '// Mapas de iluminación extraídos de las fotos de prueba aportadas por el usuario.\n'
        '// Regenerar: python3 tools/extract-paper-textures.py /ruta/a/Downloads\n'
        '// Gris 128 = transparente; señal logarítmica = (gris - 128) / 512.\n'
        'window.forjaPaperTextures = ' + json.dumps(textures, ensure_ascii=False, separators=(',', ':')) + ';\n',
        encoding='utf-8',
    )


if __name__ == '__main__':
    main()
