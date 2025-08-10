from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

# Create your models here.
class CrudModels(models.Model):
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    EmailId = models.EmailField(
        unique=True,
        max_length=100,
        error_messages={'unique': "Email already exists."}
    )
    PhoneNumber = models.CharField(
        unique=True,
        max_length=10,
        validators=[RegexValidator(r'^\d{10}$', 'Enter a valid 10-digit number')],
        error_messages={'unique': "Phone number already exists."}
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['FirstName', 'LastName'],
                name='unique_name',
                violation_error_message="A contact with this first and last name already exists."
            )
        ]

    def clean(self):
        if self.FirstName.lower() == 'rahul' and self.EmailId.lower().endswith('gmail.com'):
            raise ValidationError("Email ending with 'gmail.com' is not allowed for first name Rahul.")