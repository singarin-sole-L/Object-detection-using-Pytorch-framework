import os



def get_data(dataset_part ="train/", plane = "axial/", raw_data_directory="data/raw/"):
    root_directory = raw_data_directory + plane 
    annotations_dir = root_directory + "labels/" + dataset_part
    images_dir = root_directory + "images/" + dataset_part

    dataset = []
    
    for filename in os.listdir(annotations_dir):
        if not filename.endswith(".txt"):
            continue
    
        file_path = os.path.join(annotations_dir, filename)
        image_name = os.path.splitext(filename)[0] + ".jpg"
        image_path = os.path.join(images_dir, image_name)
    
        labels = []
        bboxes = []

        with open(file_path, "r") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) != 5:
                    continue  
                label = int(parts[0])
                bbox = [float(x) for x in parts[1:]]  # [x_center, y_center, width, height]
    
                labels.append(label)
                bboxes.append(bbox)
    
        dataset.append({
            "image_path": image_path,
            "labels": labels,
            "bboxes": bboxes
        })
    return dataset
