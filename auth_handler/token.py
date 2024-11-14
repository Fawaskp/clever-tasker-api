from rest_framework_simplejwt.tokens import RefreshToken

def generate_custom_token(user):
    """
    function to generate a JWT with custom payload 'email' and 'name'.
    """
    refresh = RefreshToken.for_user(user)
    
    refresh.payload['email'] = user.email
    refresh.payload['name'] = user.name

    return [str(refresh.access_token), str(refresh)]