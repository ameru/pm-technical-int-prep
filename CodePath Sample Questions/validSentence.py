# Implement a solution that checks if a sentence is valid.
# For a sentence to be valid, it must meet the following two criteria:
# Does the sentence end with
# Return true if the sentence is valid and false if the sentence is not valid.

def isValid(sentence):
  if (sentence[0].isupper()) and (sentence.endswith(".") or sentence.endswith("!") or sentence.endswith("?")):
      return True
  else:
      return False
