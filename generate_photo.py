import os
import json

# Folder containing your images
image_folder = "images"

# Get all files in the folder
files = os.listdir(image_folder)

# Keep only image files (jpg, jpeg, png, gif)
image_files = [f for f in files if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))]

# Sort alphabetically (optional)
image_files.sort()

# Save to JSON file
with open("photos.json", "w") as f:
    json.dump(image_files, f, indent=2)

print(f"photos.json generated with {len(image_files)} images!")