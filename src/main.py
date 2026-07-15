from nova import Nova
from startup import StartupManager


startup = StartupManager()
startup.banner()

nova = Nova()

while True:

    user_input = input("Kerry: ")

    if user_input.lower() in ["exit", "quit"]:
        print("\nNova: Goodbye, Kerry.")
        break

    response = nova.chat(user_input)

    print(f"\nNova: {response}\n")