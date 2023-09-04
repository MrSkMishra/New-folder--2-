import os
import replicate

#Set the REPLICATE_API_TOKEN environment variable
os.environ["REPLICATE_API_TOKEN"] = "r8_4J3nbZKuOXb8sGCjGd5SvqbG36uAl0G3KrBhE"


model = replicate.models.get("sczhou/codeformer")
version = model.versions.get("7de2ea26c616d5bf2245ad0d5e24f0ff9a6204578a5c876db53142edd9d2cd56")


# https://replicate.com/sczhou/codeformer/versions/7de2ea26c616d5bf2245ad0d5e24f0ff9a6204578a5c876db53142edd9d2cd56#input
inputs = {
    # Input image
    'image': open("img.JPG", "rb"),

    # Balance the quality (lower number) and fidelity (higher number).
    # Range: 0 to 1
    'codeformer_fidelity': 1,

    # Enhance background image with Real-ESRGAN
    'background_enhance': True,

    # Upsample restored faces for high-resolution AI-created images
    'face_upsample': True,

    # The final upsampling scale of the image
    'upscale': 2,
}

# https://replicate.com/sczhou/codeformer/versions/7de2ea26c616d5bf2245ad0d5e24f0ff9a6204578a5c876db53142edd9d2cd56#output-schema
output = version.predict(**inputs)
print(output)