import cv2
import numpy as np
import os

image_files = {"Higgs": "Higgs.png",
               "Electromagnetic": "Electromagnetic.png",
               "Weak_W_Lepton": "Weak_W_Lepton.png",
               "Weak_W_Quark": "Weak_W_Quark.png",
               "Weak_Z": "Weak_Z.png",
               "Strong": "Strong.png"}
input_dir = "input_images"
output_dir = "augmented_images"
os.makedirs(output_dir, exist_ok=True)

def apply_augmentations(image):
    h, w = image.shape[:2]

    angle = np.random.uniform(-5, 5)
    center = (w // 2, h // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, rotation_matrix, (w, h), cv2.BORDER_CONSTANT, borderValue=(255, 255, 255))

    zoom_factor = np.random.uniform(.95, 1.05)
    new_w, new_h = int(w * zoom_factor), int(h * zoom_factor)
    zoomed = cv2.resize(rotated, (new_w, new_h))
    if zoom_factor > 1:
        crop_x = (new_w - w) // 2
        crop_y = (new_h - h) // 2
        zoomed = zoomed[crop_y:crop_y + h, crop_x:crop_x + w]
    else:
        pad_x = (w - new_w) // 2
        pad_y = (h - new_h) // 2
        zoomed = cv2.copyMakeBorder(zoomed, pad_y, pad_y, pad_x, pad_x, cv2.BORDER_CONSTANT, value=(255, 255, 255))
    
    max_shift = .05
    dx = int(np.random.uniform(-max_shift, max_shift) * w)
    dy = int(np.random.uniform(-max_shift, max_shift) * h)
    translation_matrix = np.float32([[1, 0, dx], [0, 1, dy]])
    shifted = cv2.warpAffine(zoomed, translation_matrix, (w, h), cv2.BORDER_CONSTANT, borderValue=(255, 255, 255))
    
    shear_factor = np.random.uniform(-.05, .05)
    shear_matrix = np.float32([[1, shear_factor, 0], [0, 1, 0]])
    sheared = cv2.warpAffine(shifted, shear_matrix, (w, h), cv2.BORDER_CONSTANT, borderValue=(255, 255, 255))
    return sheared

for category, filename in image_files.items():
    input_path = os.path.join(input_dir, filename)
    category_output_dir = os.path.join(output_dir, category)
    os.makedirs(category_output_dir, exist_ok=True)
    img = cv2.imread(input_path)
    if img is None:
        print(f"Gambar tidak ditemukan: {filename}")
        continue
    for i in range(399):
        augmented_image = apply_augmentations(img)
        output_path = os.path.join(category_output_dir, f"{category}_{i+1}.png")
        cv2.imwrite(output_path, augmented_image)
    print(f"Augmentasi selesai untuk kategori: {category}")
print(f"Semua augmentasi selesai. Gambar disimpan di folder: {output_dir}")