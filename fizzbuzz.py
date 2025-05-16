def fizzbuzz_printer():
  """
  Prints numbers from 1 to 100.
  - For numbers divisible by 3, it prints "fizz" in addition to the number.
  - For numbers divisible by 5, it prints "buzz" in addition to the number.
  - For numbers divisible by both 3 and 5, it prints "fizzbuzz" in addition to the number.
  """
  for i in range(1, 101):  # Loop from 1 to 100 (inclusive)
    output = str(i)  # Start with the number itself

    if i % 3 == 0 and i % 5 == 0:
      output += " fizzbuzz"
    elif i % 3 == 0:
      output += " fizz"
    elif i % 5 == 0:
      output += " buzz"
    
    print(output)

# Call the method to execute the FizzBuzz sequence
fizzbuzz_printer()
