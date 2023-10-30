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
Username = 'aarohcharne'
password = 'Laddu@2010'

U1 = input("Username: ")
P1 = getpass("Password: ")

if U1 == Username and P1 == password:
    print("Access Granted")
    time.sleep(2)
    print("Please wait for kernal...")
    time.sleep(10)
    shell()
