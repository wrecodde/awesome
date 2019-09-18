from django.db import models

class User(models.Model):
  """A general user."""
  username = models.CharField(max_length=30)
  email = models.EmailField(max_length=45)
  passphrase = models.CharField(max_length=75)

  def __str__(self):
    """Return a string representation of the model."""
    return self.username