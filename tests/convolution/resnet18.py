import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import urllib.request

def run_resnet18(image_url, device="cuda" if torch.cuda.is_available() else "cpu"):
    print("DEVICE IS"+device)
    """
    Runs the ResNet18 model on an image from a URL and prints the top 5 predictions.

    Args:
        image_url (str): URL of the image.
        device (str): "cuda" for GPU, "cpu" for CPU.
    """

    try:
        # Download the image
        urllib.request.urlretrieve(image_url, "temp_image.jpg")
        img = Image.open("temp_image.jpg")

        # Preprocessing
        transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
        img_t = transform(img).unsqueeze(0).to(device) # unsqueeze adds a batch dimension.

        # Load the model
        model = models.resnet18(pretrained=True).to(device).eval()  # eval() for inference mode

        # Inference
        with torch.no_grad(): # disable gradient calculations
            output = model(img_t)

        # Process the output
        probabilities = torch.nn.functional.softmax(output[0], dim=0) # convert to probabilities
        with open("imagenet_classes.txt", "r") as f: # Download from pytorch webpage
            categories = [s.strip() for s in f.readlines()]

        top5_prob, top5_catid = torch.topk(probabilities, 5)

        for i in range(top5_prob.size(0)):
            print(categories[top5_catid[i]], top5_prob[i].item())

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Cup_and_Saucer_LACMA_47.35.6a-b_%281_of_3%29.jpg/1280px-Cup_and_Saucer_LACMA_47.35.6a-b_%281_of_3%29.jpg" # Example image
    run_resnet18(image_url)

#Download imagenet_classes.txt from:
#https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt
