import jwt
from tanner.config import TannerConfig

def generate():
    key = TannerConfig.get("API", "auth_signature")
    encoded = jwt.encode({"user": "tanner_owner"}, key, algorithm="HS256")

    if isinstance(encoded, bytes):  
        return encoded.decode("utf-8")  # Only decode if it's bytes
    return encoded  # Return directly if it's already a string