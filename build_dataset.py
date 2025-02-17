import os,csv

#directory containing subfolders with the images
root_dir = 'images/'

#prepare to write csv file
dataset_csv = "image_labels.csv"
with open(dataset_csv, mode='w', newline='') as file:
    writer = csv.writer(file)
    #create header row
    writer.writerow(['image_path', 'label'])

    #traverse each class folder
    for class_name in os.listdir(root_dir):
        class_folder = os.path.join(root_dir, class_name)
        
        if os.path.isdir(class_folder):
            #loop through each image
            for image_name in os.listdir(class_folder):
                image_path = os.path.join(class_folder, image_name)

                if image_path.lower().endswith(('.jpg')):
                    writer.writerow([image_path, class_name])

print(f"CSV file '{dataset_csv}' has been created successfully.")