from dataclasses import dataclass, field
from typing import Optional
from random import randint

DEFAULT_WIDTH = 400
DEFAULT_HEIGHT = 400
DEFAULT_NUMBER_INF_STEPS = 50
DEFAULT_GUIDANCE_SCALE = 7.5
DEFAULT_NUM_IMAGES_PER_PROMPT = 1


@dataclass
class SgStableDiffusionRequestInput:
    prompt: str
    negative_prompt: Optional[str] = field(default=None)
    seed: Optional[int] = field(default_factory=lambda: randint(1, 100))
    width: Optional[int] = field(default=DEFAULT_WIDTH)
    height: Optional[int] = field(default=DEFAULT_HEIGHT)
    num_inference_steps: Optional[int] = field(default=DEFAULT_NUMBER_INF_STEPS)
    guidance_scale: Optional[float] = field(default=DEFAULT_GUIDANCE_SCALE)
    num_images_per_prompt: Optional[int] = field(default=DEFAULT_NUM_IMAGES_PER_PROMPT)

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def new_instance_from_dict(data: dict) -> 'SgStableDiffusionRequestInput':
        if 'num_images_per_prompt' in data and data['num_images_per_prompt']:
            raise Exception('num_images_per_prompt cannot be greater than 1')
        return SgStableDiffusionRequestInput(**data)
