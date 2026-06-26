"""
Code to AI — Week 1 Project
Interactive Calculator 🧮

Concepts used: input(), type casting (float), variables,
arithmetic operators, f-strings.
(Straight-line code — no if/loops, that's Week 3!)
"""

# --- Header ---
print("=" * 35)
print("   🧮  WELCOME TO MY CALCULATOR  🧮")
print("=" * 35)

# --- Take input from the user ---
# input() returns a string, so we cast to float to do math
num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number: "))

# --- Do the calculations using arithmetic operators ---
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2          # division
power = num1 ** num2       # power
remainder = num1 % num2    # modulus (remainder)

# --- Show the results with f-strings ---
print("\n--------- RESULTS ---------")
print(f"{num1} + {num2}  = {add}")
print(f"{num1} - {num2}  = {sub}")
print(f"{num1} * {num2}  = {mul}")
print(f"{num1} / {num2}  = {div:.2f}")
print(f"{num1} ** {num2} = {power}")
print(f"{num1} % {num2}  = {remainder}")
print("---------------------------")

# --- Friendly closing message ---
print("\nThanks for using my calculator! Made with Python 🐍")
print("— Code to AI")
