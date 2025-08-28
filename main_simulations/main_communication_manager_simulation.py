
# Cerberus v0.3 - Communication Manager Simulation
# This file demonstrates the dynamic decision-making of the enhanced Communication Manager.

import time
import sys
import os

# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

print(f"Project Root: {project_root}")
print(f"sys.path: {sys.path}")

# Try importing a module from the communication package directly
try:
    from communication.secure_5g_module import Secure5GModule
    print("Successfully imported security.secure_5g_module")
except ImportError as e:
    print(f"Failed to import security.secure_5g_module: {e}")

from communication.communication_manager import CommunicationManager

if __name__ == "__main__":
    print("Starting Cerberus v0.3 Communication Manager Simulation...")

    # Initialize the Communication Manager
    # It now internally manages all its required modules.
    comm_manager = CommunicationManager()

    # Start the manager's internal decision loop
    comm_manager.start()

    print("\n--- Simulation is running for 20 seconds (Press Ctrl+C to stop early) ---")
    try:
        # The main thread just needs to wait while the manager runs in the background.
        time.sleep(20)
    except KeyboardInterrupt:
        print("\n[Simulation] Stopping simulation...")
    finally:
        # Stop the manager's decision loop
        comm_manager.stop()

    print("\nCommunication Manager simulation complete.")


