# engine_simulation.py

import time
import random

class CarEngine:
    def __init__(self):
        self.is_running = False
        self.rpm = 0
        self.torque = 0
        self.horsepower = 0

    def start(self):
        """Start the car engine."""
        if not self.is_running:
            self.is_running = True
            print("Starting the engine...")
            time.sleep(1)
            print("\n─────────────── Engine Started ───────────────\n")
        else:
            print("Engine is already running.")

    def stop(self):
        """Stop the car engine."""
        if self.is_running:
            print("Stopping the engine...")
            time.sleep(1)
            self.is_running = False
            print("\n─────────────── Engine Stopped ───────────────\n")
        else:
            print("Engine is already stopped.")

    def simulate(self):
        """Simulate engine performance."""
        if not self.is_running:
            print("Cannot simulate. Engine is not running.")
            return
        
        # Simulate RPM, torque, and horsepower with random values
        self.rpm = random.randint(1000, 7000)
        self.torque = random.uniform(100, 500)
        self.horsepower = random.uniform(50, 300)

        # Display simulated engine metrics
        print("\n═════════════════════════════════════════════")
        print(f"  RPM: {self.rpm} | Torque: {self.torque:.2f} Nm | Horsepower: {self.horsepower:.2f} HP")
        print("═════════════════════════════════════════════\n")
        time.sleep(1)

if __name__ == "__main__":
    engine = CarEngine()

    # Main program loop
    while True:
        # ASCII art menu header
        print("\n╔══════════════════════════╗")
        print("║       Car Engine          ║")
        print("╠══════════════════════════╣")
        print("║ Menu:                    ║")
        print("║ 1. Start Engine          ║")
        print("║ 2. Stop Engine           ║")
        print("║ 3. Simulate Engine       ║")
        print("║ 4. Exit                  ║")
        print("╚══════════════════════════╝")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            engine.start()
        elif choice == '2':
            engine.stop()
        elif choice == '3':
            engine.simulate()
        elif choice == '4':
            print("\nExiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
