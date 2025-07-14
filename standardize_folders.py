#!/usr/bin/env python3
"""
Targeted script to standardize folder names to match exactly with product descriptions.
This script focuses on the specific patterns we identified in our analysis.
"""

import os
import csv
import shutil
from pathlib import Path

def read_product_descriptions(csv_file):
    """Read product descriptions from CSV file."""
    products = {}
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            sku = row['SKU']
            description = row['Description']
            category = row['CATEGORY']
            sub_category = row['SUB CATEGORY']
            storage = row['Storage']
            colour = row['Colour']
            
            products[sku] = {
                'description': description,
                'category': category,
                'sub_category': sub_category,
                'storage': storage,
                'colour': colour
            }
    return products

def create_folder_mapping():
    """Create a mapping of current folder names to standardized product description names."""
    
    # Define the mapping based on our analysis
    folder_mapping = {
        # iPhone 15 Series
        "Apple iPhone 15 128GB Black": "iPhone 15 128GB Black",
        "Apple iPhone 15 128GB Pink": "iPhone 15 128GB Pink", 
        "Apple iPhone 15 128GB Green": "iPhone 15 128GB Green",
        "Apple iPhone 15 128GB Blue": "iPhone 15 128GB Blue",
        "Apple iPhone 15 128GB Yellow ": "iPhone 15 128GB Yellow",
        
        # iPhone 15 Plus Series
        "Apple iPhone 15 Plus 128GB Black": "iPhone 15 Plus 128GB Black",
        "Apple iPhone 15 Plus 128GB Pink": "iPhone 15 Plus 128GB Pink",
        "Apple iPhone 15 Plus 128GB Green": "iPhone 15 Plus 128GB Green", 
        "Apple iPhone 15 Plus 128GB Blue": "iPhone 15 Plus 128GB Blue",
        "Apple iPhone 15 Plus 128GB Yellow": "iPhone 15 Plus 128GB Yellow",
        
        # iPhone 15 Pro Series
        "Apple iPhone 15 Pro 128GB Black Titanium": "iPhone 15 Pro 128GB Black Titanium",
        "Apple iPhone 15 Pro 128GB White Titanium": "iPhone 15 Pro 128GB White Titanium",
        "Apple iPhone 15 Pro 128GB Natural Titanium": "iPhone 15 Pro 128GB Natural Titanium",
        "Apple iPhone 15 Pro 128GB Blue Titanium": "iPhone 15 Pro 128GB Blue Titanium",
        "Apple iPhone 15 Pro 256GB Black Titanium": "iPhone 15 Pro 256GB Black Titanium",
        
        # iPhone 15 Pro Max Series
        "Apple iPhone 15 Pro Max 256GB White Titanium": "iPhone 15 Pro Max 256GB White Titanium",
        "Apple iPhone 15 Pro Max 512GB White Titanium": "iPhone 15 Pro Max 512GB White Titanium",
        "Apple iPhone 15 Pro Max 512GB Natural Titanium": "iPhone 15 Pro Max 512GB Natural Titanium",
        "Apple iPhone 15 Pro Max 1TB Black Titanium": "iPhone 15 Pro Max 1TB Black Titanium",
        "Apple iPhone 15 Pro Max 1TB Blue Titanium": "iPhone 15 Pro Max 1TB Blue Titanium",
        
        # iPhone 14 Series
        "Apple iPhone 14 Midnight": "iPhone 14 128GB Midnight",
        "iPhone 14 128GB Starlight": "iPhone 14 128GB Starlight",
        "iPhone 14 128GB Blue": "iPhone 14 128GB Blue",
        "Apple iPhone 14 128GB Blue": "iPhone 14 128GB Blue",
        "Apple iPhone 14 128GB Yellow": "iPhone 14 128GB Yellow",
        "Apple iPhone 14 128GB Purple": "iPhone 14 128GB Purple",
        "Apple iPhone 14 128GB (PRODUCT)RED ": "iPhone 14 128GB (PRODUCT)RED",
        
        # iPhone 14 Plus Series
        "Apple iPhone 14 Plus 128GB Starlight": "iPhone 14 Plus 128GB Starlight",
        "Apple iPhone 14 Plus 128GB Purple": "iPhone 14 Plus 128GB Purple",
        "Apple iPhone 14 Plus 128GB Midnight": "iPhone 14 Plus 128GB Midnight",
        "Apple iPhone 14 Plus 128GB Blue": "iPhone 14 Plus 128GB Blue",
        "Apple iPhone 14 Plus (128 GB) - (Product) RED": "iPhone 14 Plus 128GB (PRODUCT)RED",
        
        # iPhone 14 Pro Series
        "iPhone 14 Pro 128GB Space Black": "iPhone 14 Pro 128GB Space Black",
        "iPhone 14 Pro 128GB Silver": "iPhone 14 Pro 128GB Silver",
        "iPhone 14 Pro 128GB Gold": "iPhone 14 Pro 128GB Gold",
        "iPhone 14 Pro 128GB Deep Purple": "iPhone 14 Pro 128GB Deep Purple",
        
        # iPhone 14 Pro Max Series
        "iPhone 14 Pro Max 128GB Space Black": "iPhone 14 Pro Max 128GB Space Black",
        "iPhone 14 Pro Max 128GB Silver": "iPhone 14 Pro Max 128GB Silver",
        "iPhone 14 Pro Max 128GB Gold": "iPhone 14 Pro Max 128GB Gold",
        "iPhone 14 Pro Max 128GB Deep Purple": "iPhone 14 Pro Max 128GB Deep Purple",
        
        # iPhone 13 Series
        "Apple iPhone 13 128GB Midnight": "iPhone 13 128GB Midnight",
        "Apple iPhone 13 128GB Starlight": "iPhone 13 128GB Starlight",
        "Apple iPhone 13 128GB Pink": "iPhone 13 128GB Pink",
        "Apple iPhone 13 128GB Green ": "iPhone 13 128GB Green",
        "iPhone 13 128GB (PRODUCT)RED": "iPhone 13 128GB (PRODUCT)RED",
        "Apple iPhone 13 256GB (PRODUCT)RED": "iPhone 13 256GB (PRODUCT)RED",
        "iphone 13 blue 128 GB": "iPhone 13 128GB Blue",
        
        # iPhone SE Series
        "Apple iPhone SE 128GB Starlight": "iPhone SE 128GB Starlight",
        "Apple iPhone SE 128GB Midnight": "iPhone SE 128GB Midnight",
        "Apple iPhone SE 128GB (PRODUCT)RED": "iPhone SE 128GB (PRODUCT)RED",
        
        # iPhone 12 Series
        "Apple iPhone 12 64GB White": "iPhone 12 64GB White",
        "Apple iPhone 12 64GB Green": "iPhone 12 64GB Green",
        "Apple iPhone 12 64GB Black": "iPhone 12 64GB Black",
        "Apple iPhone 12 128GB White": "iPhone 12 128GB White",
        "Apple iPhone 12 128GB Purple ": "iPhone 12 128GB Purple",
        "Apple iPhone 12 128GB Purple": "iPhone 12 128GB Purple",
        "Apple iPhone 12 128GB Black": "iPhone 12 128GB Black",
        "Apple iPhone 12 Mini (256GB) - Blue": "iPhone 12 Mini 256GB Blue",
        
        # iPhone 11 Series
        "Apple iPhone 11 128GB Black": "iPhone 11 128GB Black",
        "Apple iPhone 11 (64GB) - White": "iPhone 11 64GB White",
        
        # iPad Series
        "Apple 11-inch iPad Pro Wi-Fi 256GB - Space Grey": "11-inch iPad Pro Wi-Fi 256GB - Space Grey",
        "11-inch iPad Wi-Fi 256GB - Silver": "11-inch iPad Wi-Fi 256GB - Silver",
        "12.9-inch iPad Pro Wi‑Fi + Cellular 128GB - Space Grey": "12.9-inch iPad Pro Wi-Fi + Cellular 128GB - Space Grey",
        "10.9-inch iPad Air Wi-Fi 64GB - Space Grey": "10.9-inch iPad Air Wi-Fi 64GB - Space Grey",
        "Apple 10.2-inch iPad Wi-Fi 64GB - Space Grey": "10.2-inch iPad Wi-Fi 64GB - Space Grey",
        " Apple 10.2-inch iPad Wi-Fi Cellular 64GB - Space Grey (Demo)": "10.2-inch iPad Wi-Fi + Cellular 64GB - Space Grey (Demo)",
        
        # MacBook Air Series
        "Apple 13-inch MacBook Air - M2 chip with 8-core CPU and 8-core GPU 8GB Ram & 256GB - Starlight": "13-inch MacBook Air: Apple M2 chip with 8-core CPU and 8-core GPU, 16GB, 256GB - Starlight",
        "Apple 13-inch MacBook Air - M2 chip with 8-core CPU and 8-core GPU 8GB Ram & 256GB - Silver": "13-inch MacBook Air: Apple M2 chip with 8-core CPU and 8-core GPU, 16GB, 256GB - Silver",
        "Apple 13-inch MacBook Air - M2 chip with 8-core CPU and 8-core GPU 8GB Ram & 256GB - Midnight": "13-inch MacBook Air: Apple M2 chip with 8-core CPU and 8-core GPU, 16GB, 256GB - Midnight",
        "Apple 13-inch MacBook Air - M2 chip with 8-core CPU and 10-core GPU 8GB Ram & 512GB - Starlight": "13-inch MacBook Air: Apple M2 chip with 8-core CPU and 10-core GPU, 16GB, 512GB - Starlight",
        "Apple 13-inch MacBook Air - M2 chip with 8-core CPU and 10-core GPU 8GB Ram & 512GB - Space Grey": "13-inch MacBook Air: Apple M2 chip with 8-core CPU and 10-core GPU, 16GB, 512GB - Space Grey",
        "Apple 13-inch MacBook Air - M2 chip with 8-core CPU and 10-core GPU 8GB Ram & 512GB - Silver": "13-inch MacBook Air: Apple M2 chip with 8-core CPU and 10-core GPU, 16GB, 512GB - Silver",
        "Apple 13-inch MacBook Air - M2 chip with 8-core CPU and 10-core GPU 8GB Ram & 512GB - Midnight": "13-inch MacBook Air: Apple M2 chip with 8-core CPU and 10-core GPU, 16GB, 512GB - Midnight",
        "Apple 15-inch MacBook Air - M2 chip with 8-core CPU and 10-core GPU 8GB Ram & 256GB - Starlight": "15-inch MacBook Air: Apple M2 chip with 8-core CPU and 10-core GPU, 16GB, 256GB - Starlight",
        "Apple 15-inch MacBook Air - M2 chip with 8-core CPU and 10-core GPU 8GB Ram & 256GB - Silver": "15-inch MacBook Air: Apple M2 chip with 8-core CPU and 10-core GPU, 16GB, 256GB - Silver",
        "Apple 15-inch MacBook Air - M2 chip with 8-core CPU and 10-core GPU 8GB Ram & 256GB - Midnight": "15-inch MacBook Air: Apple M2 chip with 8-core CPU and 10-core GPU, 16GB, 256GB - Midnight",
        "Apple 15-inch MacBook Air - M2 chip with 8-core CPU and 10-core GPU 8GB Ram & 512GB - Silver": "15-inch MacBook Air: Apple M2 chip with 8-core CPU and 10-core GPU, 16GB, 512GB - Silver",
        "Apple 15-inch MacBook Air - M2 chip with 8-core CPU and 10-core GPU 8GB Ram & 512GB - Midnight": "15-inch MacBook Air: Apple M2 chip with 8-core CPU and 10-core GPU, 16GB, 512GB - Midnight",
        
        # Accessories
        "Lightning to SD Card Camera Reader": "Lightning to SD Card Camera Reader",
        "Lightning to USB Cable ": "Lightning to USB Cable (1m)",
        "Lightning to USB Cable (2 m) ": "Lightning to USB Cable (2 m)",
        "Lightning to USB Camera Adapter": "Lightning to USB Camera Adapter",
        "Lightning Digital AV Adapter": "Lightning to Digital AV Adapter",
        "USB-C to Lightning Cable ": "USB-C to Lightning Cable (1m)",
        "USB-C to USB Adapter": "USB-C to USB Adapter",
        "Apple Pencil (USB-C) ": "Apple Pencil (USB-C)",
        "Apple EarPods with Lightning Connector": "EarPods (Lightning Connector)",
        "Apple 5W USB Power Adapter": "Apple 5W USB Power Adapter",
        "Apple 12W USB Power Adapter": "Apple 12W USB Power Adapter",
        "20W USB-C Power Adapter": "20W USB-C Power Adapter",
        "Apple 30W USB-C Power Adapter": "Apple 30W USB-C Power Adapter",
        "Apple 35W Dual USB-C Port Power Adapter": "Apple 35W Dual USB-C Port Power Adapter",
        "Apple 96W USB-C Power Adapter": "Apple 96W USB-C Power Adapter",
        "Apple 140W USB-C Power Adapter": "Apple 140W USB-C Power Adapter",
        "Apple 240W USBC Charge Cable (2 m)": "240W USB-C Charge Cable (2 m)",
        " Apple TV": "Apple TV 4K Wi-Fi with 64GB storage",
    }
    
    return folder_mapping

def find_and_rename_folders(base_path, folder_mapping, dry_run=True):
    """Find folders and rename them according to the mapping."""
    successful_renames = []
    failed_renames = []
    
    for root, dirs, files in os.walk(base_path):
        for dir_name in dirs:
            if dir_name in folder_mapping:
                old_path = os.path.join(root, dir_name)
                new_name = folder_mapping[dir_name]
                new_path = os.path.join(root, new_name)
                
                print(f"Found: {old_path}")
                print(f"Renaming to: {new_path}")
                print(f"New name: {new_name}")
                print()
                
                if not dry_run:
                    try:
                        # Check if new path already exists
                        if os.path.exists(new_path):
                            print(f"  WARNING: {new_path} already exists, skipping...")
                            failed_renames.append((old_path, new_path, "Path already exists"))
                            continue
                        
                        # Rename the folder
                        os.rename(old_path, new_path)
                        successful_renames.append((old_path, new_path, "Success"))
                        print(f"  SUCCESS: Renamed successfully")
                        
                    except Exception as e:
                        print(f"  ERROR: Failed to rename - {e}")
                        failed_renames.append((old_path, new_path, str(e)))
                else:
                    successful_renames.append((old_path, new_path, "Dry run"))
    
    return successful_renames, failed_renames

def main():
    # Configuration
    base_path = "websites/conquer"
    
    print("=== Folder Standardization Script ===")
    print(f"Base Path: {base_path}")
    print()
    
    # Create folder mapping
    print("Creating folder mapping...")
    folder_mapping = create_folder_mapping()
    print(f"Created {len(folder_mapping)} mappings")
    print()
    
    # Show mapping plan
    print("=== MAPPING PLAN ===")
    for i, (old_name, new_name) in enumerate(folder_mapping.items(), 1):
        print(f"{i}. {old_name} -> {new_name}")
    print()
    
    # Find and rename folders (dry run first)
    print("=== DRY RUN ===")
    successful, failed = find_and_rename_folders(base_path, folder_mapping, dry_run=True)
    print(f"Would rename {len(successful)} folders")
    print()
    
    # Ask for confirmation
    response = input("Do you want to proceed with actual renaming? (y/n): ").lower().strip()
    
    if response == 'y':
        print("\n=== EXECUTING RENAMING ===")
        successful, failed = find_and_rename_folders(base_path, folder_mapping, dry_run=False)
        
        print(f"\n=== RESULTS ===")
        print(f"Successful renames: {len(successful)}")
        print(f"Failed renames: {len(failed)}")
        
        if failed:
            print("\nFailed renames:")
            for old_path, new_path, reason in failed:
                print(f"  {os.path.basename(old_path)} -> {os.path.basename(new_path)} (Reason: {reason})")
    else:
        print("Renaming cancelled.")

if __name__ == "__main__":
    main() 