<<<<<<< HEAD
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six

class GeneradorToken(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (six.text_type(user.id) + six.text_type(timestamp)) + six.text_type(user.is_active)

=======
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six

class GeneradorToken(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (six.text_type(user.id) + six.text_type(timestamp)) + six.text_type(user.is_active)

>>>>>>> e52eb3d7b49d41807b971e577dff8ec8b0db68e6
token_activacion = GeneradorToken()