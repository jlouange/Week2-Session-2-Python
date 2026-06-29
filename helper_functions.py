def validate_input(user_input):
  if isinstance(user_input, str) and user_input.strip():
    print("The input is validated. it is a string and non-empty")
  else:
    print("Invalid input!")

