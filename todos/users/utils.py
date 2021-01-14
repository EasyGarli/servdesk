from .serializers import FullCustomUserSerializer

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': FullCustomUserSerializer(user, context={'request': request}).data
    }