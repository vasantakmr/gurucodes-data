import os
import csv
import sys

# Configuration
ROOT_DIR = 'websites/conquer'
MEDIA_URL_PREFIX = 'https://gurucodes-data.pages.dev/websites/conquer/'
IMAGE_EXTS = {'.jpg', '.jpeg', '.png', '.webp', '.gif'}

# Helper to get delimiter and output file based on extension
def get_format(filename):
    if filename.endswith('.csv'):
        return ',', filename.replace('.csv', '_updated.csv')
    elif filename.endswith('.tsv'):
        return '\t', filename.replace('.tsv', '_updated.tsv')
    else:
        raise ValueError('Unsupported file type')

# Step 1: Build a mapping from leaf folder name (lowercase) to list of image file relative paths
folder_to_images = {}
for dirpath, dirnames, filenames in os.walk(ROOT_DIR):
    if not dirnames:
        leaf_folder = os.path.basename(dirpath)
        images = [f for f in filenames if os.path.splitext(f)[1].lower() in IMAGE_EXTS]
        if images:
            folder_to_images[leaf_folder.lower()] = [
                os.path.relpath(os.path.join(dirpath, img), ROOT_DIR) for img in images
            ]

# Step 2: Process both TSV and CSV
for input_file in ['products.tsv', 'products.csv']:
    if not os.path.exists(input_file):
        continue
    delimiter, output_file = get_format(input_file)
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        reader = csv.DictReader(infile, delimiter=delimiter)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter=delimiter)
        writer.writeheader()
        for row in reader:
            variant = row.get('Product Variant Name', '').strip().lower()
            urls = []
            if variant and variant in folder_to_images:
                urls = [MEDIA_URL_PREFIX + path.replace('\\', '/').replace(' ', '%20') for path in folder_to_images[variant]]
            row['Media URLs'] = ';'.join(urls)
            writer.writerow(row) 

APPLECARE_IMAGE_URL = "https://gurucodes-data.pages.dev/websites/conquer/AppleCare/applecare.png"
INPUT_CSV = "products.csv"
OUTPUT_CSV = "products_updated.csv"

with open(INPUT_CSV, newline='', encoding='utf-8') as infile, open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    header = next(reader)
    writer.writerow(header)
    media_urls_index = header.index('Media URLs')
    variant_name_index = header.index('Product Variant Name')
    for row in reader:
        if len(row) > variant_name_index and 'applecare' in row[variant_name_index].lower():
            # Set only the Media URLs column to the AppleCare image URL
            if len(row) <= media_urls_index:
                row += [''] * (media_urls_index - len(row) + 1)
            row[media_urls_index] = APPLECARE_IMAGE_URL
        writer.writerow(row) 