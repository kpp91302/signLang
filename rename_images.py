import os

# Path to the parent folder containing subfolders
parent_folder = "images/"

# List all subfolders in the parent folder
subfolders = [f for f in os.listdir(parent_folder) if os.path.isdir(os.path.join(parent_folder, f))]

# Loop through each subfolder and rename the images
for index, subfolder in enumerate(subfolders):
    subfolder_path = os.path.join(parent_folder, subfolder)
    
    # List all image files in the subfolder (assuming they are all images and have extensions like .jpg, .png, etc.)
    images = [f for f in os.listdir(subfolder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]
    
    # Sort images (optional, in case the order matters)
    images.sort()

    # Rename each image in the subfolder
    for i, image in enumerate(images, start=1):
        new_name = f"{chr(97 + index)}{i}{os.path.splitext(image)[1]}"  # a1, a2, ..., b1, b2, ..., etc.
        old_image_path = os.path.join(subfolder_path, image)
        new_image_path = os.path.join(subfolder_path, new_name)
        
        # Rename the file
        os.rename(old_image_path, new_image_path)
        
    print(f"Renamed images in subfolder: {subfolder}")

print("Renaming complete!")
