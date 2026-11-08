import os
from flask import Blueprint, request, send_from_directory, abort

uploads_api = Blueprint('uploads', __name__)

UPLOADS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'uploads')
UPLOADS_DIR = os.path.realpath(UPLOADS_DIR)


@uploads_api.route('/')
def get_upload():
   name = request.args.get("name")
   if not name:
      abort(400)

   # Empêche toute tentative de sortir du dossier uploads/ (../, chemins absolus, etc.)
   requested_path = os.path.realpath(os.path.join(UPLOADS_DIR, name))
   if os.path.commonpath([UPLOADS_DIR, requested_path]) != UPLOADS_DIR:
      abort(403)

   filename = os.path.basename(requested_path)
   return send_from_directory(UPLOADS_DIR, filename)