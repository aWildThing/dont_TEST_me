continue_check = input("press 'C' to continue\n")
lower_continue_check = continue_check.lower()
if lower_continue_check == "c":
    print("Good job! You did it. All by yourself too!")
else:
    print(f"Excuse me? I said press C not {continue_check}")
input("")