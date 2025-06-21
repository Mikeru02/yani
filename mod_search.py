import re

def search_symbols(text: "str") -> dict:
  question_symbol = r"\?"
  exclamation_symbol = r"\!"

  # Check for symbols 
  return {
    "is_question": bool(re.search(question_symbol, text)),
    "is_exclamation": bool(re.search(exclamation_symbol, text))
  }
