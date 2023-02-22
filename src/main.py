from fastapi import FastAPI, UploadFile, File
from .model_runner import load_model, predict_class, get_class_label
from PIL import Image
import torchvision.transforms as transforms

app = FastAPI()

# Load the model and label map
model = load_model('./models/model.pth') 

transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

import os
import io
from PIL import Image

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    print(type(file))

    # ## Save the uploaded file to disk
    with open(file.filename, "wb") as buffer:
        buffer.write(await file.read())

    # Check that the file exists and is readable
    if not os.path.isfile(file.filename) or not os.access(file.filename, os.R_OK):
        return {"error": "File not found or not readable"}
    image_path = './data/images/'+file.filename

    # Open the image file using Pillow
    with io.BufferedReader(io.FileIO(file.filename, 'rb')) as f:
        image = Image.open(f)

        # save the image to the image path folder above
        image.save('./data/images/'+file.filename)
        if not os.path.isfile('./data/images/'+file.filename):
            image.save(image_path)
    
    # Make a prediction
    predicted_class = predict_class(image_path, model, transform)
    class_label = get_class_label(predicted_class)
    print(f"Image '{image_path}' predicted as: {class_label}")
    return {"class": class_label}




