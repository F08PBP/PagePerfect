from django.forms import ModelForm
from .models import Message  # Import the Message model

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ["message"]