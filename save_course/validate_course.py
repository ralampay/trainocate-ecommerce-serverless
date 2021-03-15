class ValidateCourse:
  def __init__(self, code=None, name=None, description=None, price=None, num_days=None):
    self.code         = code
    self.name         = name
    self.description  = description
    self.price        = price
    self.num_days     = num_days

    self.errors = []

  def execute(self):
    if not self.code:
      self.errors.append("code is required")

    if not self.name:
      self.errors.append("name is required")

    if not self.description:
      self.errors.append("description is required")

    if not self.price:
      self.errors.append("price is required")
    elif float(self.price) <= 0.0
      self.errors.append("price should be positive")

    if not self.num_days:
      self.errors.append("num_days is required")
    elif int(self.num_days) < 1
      errors.append("num_days should be more than one")

    return errors
