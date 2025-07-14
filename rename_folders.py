#!/usr/bin/env python3
"""
Script to rename leaf folders to match exactly with product descriptions from CSV.
This will standardize folder names and make mapping much cleaner.
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
            
            # Create a clean folder name from description
            folder_name = description.strip()
            
            products[sku] = {
                'description': description,
                'folder_name': folder_name,
                'category': category,
                'sub_category': sub_category,
                'storage': storage,
                'colour': colour
            }
    return products

def find_existing_folders(base_path):
    """Find all existing leaf folders in the directory structure."""
    existing_folders = []
    
    for root, dirs, files in os.walk(base_path):
        # If this is a leaf directory (no subdirectories)
        if not dirs and files:
            existing_folders.append(root)
    
    return existing_folders

def create_mapping_plan(products, existing_folders):
    """Create a mapping plan for renaming folders."""
    mapping_plan = []
    
    # Group products by category and sub-category
    product_groups = {}
    for sku, product in products.items():
        key = f"{product['category']}_{product['sub_category']}"
        if key not in product_groups:
            product_groups[key] = []
        product_groups[key].append(product)
    
    # For each existing folder, find the best matching product
    for folder_path in existing_folders:
        folder_name = os.path.basename(folder_path)
        parent_path = os.path.dirname(folder_path)
        
        # Try to find matching product
        best_match = None
        best_score = 0
        
        for sku, product in products.items():
            score = 0
            
            # Check if folder name contains key elements from product description
            if product['colour'] and product['colour'].lower() in folder_name.lower():
                score += 2
            if product['storage'] and product['storage'].lower() in folder_name.lower():
                score += 2
            if any(word in folder_name.lower() for word in product['description'].lower().split()):
                score += 1
            
            if score > best_score:
                best_score = score
                best_match = product
        
        if best_match:
            new_folder_name = best_match['folder_name']
            new_folder_path = os.path.join(parent_path, new_folder_name)
            
            mapping_plan.append({
                'old_path': folder_path,
                'new_path': new_folder_path,
                'old_name': folder_name,
                'new_name': new_folder_name,
                'product_sku': sku,
                'confidence': best_score
            })
    
    return mapping_plan

def execute_renaming(mapping_plan, dry_run=True):
    """Execute the folder renaming plan."""
    successful_renames = []
    failed_renames = []
    
    for mapping in mapping_plan:
        old_path = mapping['old_path']
        new_path = mapping['new_path']
        old_name = mapping['old_name']
        new_name = mapping['new_name']
        
        print(f"Renaming: {old_name} -> {new_name}")
        print(f"  Old path: {old_path}")
        print(f"  New path: {new_path}")
        print(f"  Confidence: {mapping['confidence']}")
        print()
        
        if not dry_run:
            try:
                # Check if new path already exists
                if os.path.exists(new_path):
                    print(f"  WARNING: {new_path} already exists, skipping...")
                    failed_renames.append(mapping)
                    continue
                
                # Rename the folder
                os.rename(old_path, new_path)
                successful_renames.append(mapping)
                print(f"  SUCCESS: Renamed successfully")
                
            except Exception as e:
                print(f"  ERROR: Failed to rename - {e}")
                failed_renames.append(mapping)
        else:
            successful_renames.append(mapping)
    
    return successful_renames, failed_renames

def main():
    # Configuration
    csv_file = "websites/conquer/products.csv"
    base_path = "websites/conquer"
    
    print("=== Folder Renaming Script ===")
    print(f"CSV File: {csv_file}")
    print(f"Base Path: {base_path}")
    print()
    
    # Read product descriptions
    print("Reading product descriptions from CSV...")
    products = read_product_descriptions(csv_file)
    print(f"Found {len(products)} products")
    print()
    
    # Find existing folders
    print("Finding existing leaf folders...")
    existing_folders = find_existing_folders(base_path)
    print(f"Found {len(existing_folders)} leaf folders")
    print()
    
    # Create mapping plan
    print("Creating mapping plan...")
    mapping_plan = create_mapping_plan(products, existing_folders)
    print(f"Created {len(mapping_plan)} mappings")
    print()
    
    # Show mapping plan
    print("=== MAPPING PLAN ===")
    for i, mapping in enumerate(mapping_plan, 1):
        print(f"{i}. {mapping['old_name']} -> {mapping['new_name']}")
        print(f"   Confidence: {mapping['confidence']}")
        print()
    
    # Ask for confirmation
    response = input("Do you want to proceed with renaming? (y/n): ").lower().strip()
    
    if response == 'y':
        print("\nExecuting renaming...")
        successful, failed = execute_renaming(mapping_plan, dry_run=False)
        
        print(f"\n=== RESULTS ===")
        print(f"Successful renames: {len(successful)}")
        print(f"Failed renames: {len(failed)}")
        
        if failed:
            print("\nFailed renames:")
            for mapping in failed:
                print(f"  {mapping['old_name']} -> {mapping['new_name']}")
    else:
        print("Renaming cancelled.")

if __name__ == "__main__":
    main() 