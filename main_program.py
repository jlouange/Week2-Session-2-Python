from helper_functions import validate_input,create_message
def get_user_info():

  while True:

    name = input("What is your name: ")
    if validate_input(name):
      break
  while True:

    age = input("What is your age: ")
    if validate_input(age):
      break

  return name,age
name, age = get_user_info()
create_message(name,age)

