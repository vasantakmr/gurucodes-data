import os
import csv
import re

# Configuration
ROOT_DIR = 'websites/conquer'
MEDIA_URL_PREFIX = 'https://gurucodes-data.pages.dev/websites/conquer/'
IMAGE_EXTS = {'.jpg', '.jpeg', '.png', '.webp', '.gif'}
APPLECARE_IMAGE_URL = MEDIA_URL_PREFIX + 'AppleCare/applecare.png'
INPUT_CSV = 'products.csv'
OUTPUT_CSV = 'products_updated.csv'

# Helper to extract trailing number from filename
def extract_trailing_number(filename):
    match = re.search(r'(\d+)(?=\.[^.]+$)', filename)
    return int(match.group(1)) if match else float('inf')

# Step 1: Build a mapping from leaf folder name (lowercase, stripped) to list of image file relative paths
folder_to_images = {}
for dirpath, dirnames, filenames in os.walk(ROOT_DIR):
    if not dirnames:
        leaf_folder = os.path.basename(dirpath).strip()
        images = [f for f in filenames if os.path.splitext(f)[1].lower() in IMAGE_EXTS]
        if images:
            # Sort images by trailing number, then alphabetically
            images_sorted = sorted(images, key=lambda f: (extract_trailing_number(f), f.lower()))
            folder_to_images[leaf_folder.lower()] = [
                os.path.relpath(os.path.join(dirpath, img), ROOT_DIR) for img in images_sorted
            ]

# Step 2: Process the CSV and update Media URLs
with open(INPUT_CSV, newline='', encoding='utf-8') as infile, open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    if 'Media URLs' not in fieldnames:
        fieldnames.append('Media URLs')
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in reader:
        variant = row.get('Product Variant Name', '').strip().lower()
        variant = variant.strip()  # Extra strip in case of double spaces
        urls = []
        if variant:
            if 'applecare' in variant:
                urls = [APPLECARE_IMAGE_URL]
            elif variant in folder_to_images:
                urls = [MEDIA_URL_PREFIX + path.replace('\\', '/').replace(' ', '%20') for path in folder_to_images[variant]]
        row['Media URLs'] = ';'.join(urls)
        writer.writerow(row) 