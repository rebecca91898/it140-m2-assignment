
 """To generate the user's name and birth year in a message."""

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
user_name = input("What is your name?")
user_age = int(input("How old are you?"))

    # Calculate user's approximate birth year.
birth_year = CURRENT_YEAR - user_age

    # Output personalized message with user's name and birth year.
print(f"Hello {user_name}! You were born in {birth_year}.")

# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===
# 2.7 String Formatting. Zybooks. (n.d.). https://learn.zybooks.com/zybook/IT-140-13393-M01_Introduction_to_Scripting_2026_C-6_(Oct_-_Dec)/chapter/2/section/7?lti_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3OTM5ODE0MTgsImlhdCI6MTc5Mzk4MTIzOCwianRpIjoiMDFhMWIxOWQtNGNjNS03MjBlLWIyMzYtNmI1NTcwNDg0ZWFiIiwidXNlcl9pZCI6MzA1MzI3Mn0.dK6RmEBOfIwBG1ny4_BJrJkeLqrzMCmBLA2-wKRvbAc    # Output personalized message with user's name and birth year.
    # TODO: Replace with code to output formatted results. zyBooks 1.3 & 2.7.
