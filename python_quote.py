import random

# quotes for the code
quotes = ("It's just a flesh wound.",
          "He's not the Messiah. He's a very naughty boy!",
          "THIS IS AN EX-PARROT!!")

# picks a quote from list above randomly
def random_python_quote():
    rand_index = random.randint(0, len(quotes) - 1)
    return quotes[rand_index]

#runs the code
if __name__ == '__main__':
    quote = random_python_quote()
    print (quote)