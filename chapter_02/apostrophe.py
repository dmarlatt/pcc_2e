message = " One of Python's strengths is its\n\t\"diverse\"\ncommunity. "
# message = 'One of Pythons strengths is its diverse community.'
print(f"{message}")
# print(f"{message.strip()}")
print()

# Talk about numbers...
CONST = 1_000
print(f"{CONST}\t{type(CONST)}")
print(f"{CONST / 100}\t{type(CONST/100)}")
print(f"{int(CONST / 100)}\t\t{type(int(CONST/100))}")
