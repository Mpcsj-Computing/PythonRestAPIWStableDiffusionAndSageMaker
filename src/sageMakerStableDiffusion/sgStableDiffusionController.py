from flask import Blueprint, send_file, request
from src.sageMakerStableDiffusion.sgStableDiffusionService import generate_image_from_sage_maker
from src.sageMakerStableDiffusion.sgStableDiffusionModel import SgStableDiffusionRequestInput

route_path = "sage-maker/stable-diffusion"
route_blueprint = Blueprint(route_path, __name__)


@route_blueprint.route("", methods=["POST"])
def generate_image():
    body = request.json
    result_image_path, mime_type = generate_image_from_sage_maker(
        SgStableDiffusionRequestInput.new_instance_from_dict(body))
    return send_file(result_image_path, mimetype=mime_type)
