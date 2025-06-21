# Main module of Yani 
from mod_open import open_file
from mod_search import search_symbols 
import time

if __name__ == "__main__":
  running = True
  words = open_file("data.json")

  # Greet the user 
  print("Hello! I am \"Yani\", Your AI Navigator and Informant")
  time.sleep(1)
  print("What do you want to chat about?")

  # Run the continous loop
  while running:
    # User input
    user_input = input(">> ")
    data_symbol = search_symbols(user_input)
  
    if data_symbol['is_question']:
      # Do question logic here!
      pass
    elif data_symbol['is_exclamation']:
      # Do excalamation logic here!
      pass


