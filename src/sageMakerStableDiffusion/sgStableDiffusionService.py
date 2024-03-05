from src.sageMakerStableDiffusion.sgStableDiffusionModel import SgStableDiffusionRequestInput
from PIL import Image
from io import BytesIO
import base64
import boto3
import json
from src.utils.file_utils import get_unique_tmp_file_path

sage_maker_client = boto3.client('runtime.sagemaker', region_name="us-east-1")
endpoint_name = 'jumpstart-dft-stable-diffusion-v2-1-base-v4'


def parse_response_multiple_images(query_response):
    print("query_response >> ",query_response)
    response_dict = json.loads(query_response['Body'].read())
    return response_dict['generated_images'], response_dict['prompt']


def generate_image_from_sage_maker(data: SgStableDiffusionRequestInput):
    print("generate_image_from_sage_maker >> ",data)
    image_path = ""
    mime_type = "image/png"

    payload = data.to_dict()
    query_response = sage_maker_client.invoke_endpoint(EndpointName=endpoint_name, ContentType='application/json',
                                                       Body=json.dumps(payload).encode('utf-8'),
                                                       Accept='application/json;jpeg')

    generated_images, prompt = parse_response_multiple_images(query_response)

    # generated_images are a list of jpeg images as bytes with b64 encoding.
    # Next, we decode the images and convert to RGB format before displaying

    for generated_image in generated_images:
        generated_image_decoded = BytesIO(base64.b64decode(generated_image.encode()))
        generated_image_rgb = Image.open(generated_image_decoded).convert("RGB")
        image_path = get_unique_tmp_file_path('png')
        generated_image_rgb.save(image_path, "PNG")
        break

    return image_path, mime_type
