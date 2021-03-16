import re

class ValidatePaymentDetails:
  def __init__(self, first_name=None, last_name=None, email=None, contact_number=None, course=None, credit_card_token=None, credit_card_cvn=None):
    self.first_name         = first_name
    self.last_name          = last_name
    self.email              = email
    self.contact_number     = contact_number
    self.course             = course
    self.credit_card_token  = credit_card_token
    self.credit_card_cvn    = credit_card_cvn

    self.errors = []

  def execute(self):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if not self.first_name:
      self.errors.append("first_name is required")

    if not self.last_name:
      self.errors.append("last_name is required")

    if not self.email:
      self.errors.append("email is required")
    elif not re.search(regex, self.email):
      self.errors.append("Invalid email format")

    if not self.contact_number:
      self.errors.append("contact_number is required")

    if not self.course:
      self.errors.append("course is required")

    if not self.credit_card_token:
      self.errors.append("credit_card_token is required")

    if not self.credit_card_cvn:
      self.errors.append("credit_card_cvn is required")

    return self.errors
