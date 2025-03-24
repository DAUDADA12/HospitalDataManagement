# Terminal.py

import importlib

def main():
    while True:
        command = input("\nUniTerminal >> ").strip().lower()
        
        if command == "exit":
            print("Exiting the program...")
            break


        if command:
            try:
                # Dynamically import the module based on the command
                module = importlib.import_module(f"Command.{command.capitalize()}")
            
                # Call the `ByDefault` function
                if hasattr(module, "ByDefault"):
                    print(module.ByDefault())
                else:
                    print(f"'{command}' does not support default behavior.")
        
            except ModuleNotFoundError:
                print(f"Command '{command}' not found. Please try again.")
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
