# Python Rest API with Stable Diffusion API

- The model was deployed on AWS SageMaker
- The Python RestAPI works as a bridge to allow a code connection to the model deployed on AWS

## Python RestAPI
- A Rest API was created, were, on the root route, you can make a POST call to interact with the AI model
- Available parameters:
```
prompt: str -> Main parameter
negative_prompt: Optional[str] -> Optional negative parameter prompt to not be included in the final image
seed: Optional[int] -> Random number to feed the AI model for generating the image 
width: Optional[int] -> Image width
height: Optional[int] -> Image height
num_inference_steps: Optional[int] -> How many steps to take for creating the image
guidance_scale: Optional[float] -> Don't know what it does LOL
num_images_per_prompt: Optional[int] -> How many images you want to create. Ps: The code is not ready for returning many images at once
```