from sys import api_version
from rest_framework.exceptions import APIException

class NotYourProfile(APIException):
    status_code = 403
    default_detail = "You cannot edit profile that doesn't belong to you."

class CantFollowYourself(APIException):
    status_code = 403
    default_detail = "You cannot follow yourself."
