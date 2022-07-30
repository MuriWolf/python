quest_one = print("What color are bananas?")
answer_one = str(input("(a) Blue\n(b) Wellow\n(c) Red\n\nAnswer: "))

quest_two = print("\nWhich is the largest country?")
answer_two = str(input("(a) Canada\n(b) USA\n(c) Russia\n\nAnswer: "))

quest_three = print("\nWhat color are strawbarries?")
answer_three = str(input("(a) Purple\n(b) Blue\n(c) Red\n\nAnswer: "))


score = 0
if answer_one == 'b':
    score = score + 1

if answer_two == 'c':
    score = score + 1

if answer_three == 'c':
    score = score + 1

print(f"\nYou got {score}/3 correct.")