Exercício: escreva uma função para testar se uma palavra do usuário é um palíndromo. 

As declarações de função são fornecidas para você.
"""

def isPalindrome(str):
  
 
  if str == str[::-1]:
    return str + " is a palindrome!"
  else:
    return str + " is NOT a palindrome!"


# Solicitar que o usuário digite a sentença
def main():
  userInput = input("Enter a WORD to be tested as a palindrome:")

  if (isPalindrome(userInput)):
    print(userInput + " is a palindrome!")
  else:
    print(userInput + " is NOT a palindrome!")

if __name__ == "__main__":
    main()
