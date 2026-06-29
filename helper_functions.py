def validate_input(user_input):
  if isinstance(user_input, str) and user_input.strip():
    return True
  else:
    return False

def create_message(name,age):
  print("Hello {}, you are {} years old!".format(name,age))


  