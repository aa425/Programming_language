
import subprocess 
import time
def shell():
    while True:
        user_input = input(f"{Username}$ ")

        if user_input.lower() == "exit":
            break

        try:
            result = subprocess.check_output(user_input, shell=True, text=True)
            print(result)
        except subprocess.CalledProcessError as e:
            print(f"Command returned a non-zero exit status: {e.returncode}")
        except Exception as e:
            print(f"An error occurred: {e}")
Username = U1


U1 = input("Username: ")
shell()

