
# Cerberus v0.3 - Testing, Validation & Operationalization Simulation (Conceptual)
# This file demonstrates the interaction of Security Testing, Communication Blackout Protocols, and Autonomous Recovery.

import time
import random
import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

# Import the actual, corrected modules
from testing.security_testing_framework import SecurityTestingFramework, IMSICatcherScenario, ProtocolDowngradeScenario
from protocols.communication_blackout_protocols import CommunicationBlackoutDetector, MockCommManager as MockCommManagerForBlackout, MockEmergencyBeacon
from protocols.autonomous_recovery_protocols import AutonomousRecoveryManager, MockFlightController, MockNetworkManager, MockSensorProvider

# --- Mock System for Security Testing ---
# This mock system is created specifically for this simulation to be tested by the framework.
class MockSystemForTesting:
    def __init__(self):
        self.modules = {"g5_detector": self, "5g": self}
        self.threat_level = "LOW"
        self.last_response = None

    def get_module(self, name): return self.modules.get(name)
    def get_threat_level(self): return self.threat_level
    def get_last_response(self): return self.last_response
    
    # Simulation methods that the adversarial scenarios can call
    def simulate_imsi_catcher(self):
        print("  - [MockSystem] Simulating high density of base stations.")
        self.threat_level = "HIGH"
        
    def simulate_downgrade(self):
        print("  - [MockSystem] Simulating encryption downgrade.")
        self.last_response = "FORCE_STRONGEST_ENCRYPTION"

# --- Simulation Setup ---
if __name__ == "__main__":
    print("Starting Cerberus v0.3 Testing, Validation & Operationalization Simulation...")

    # Initialize components for Scenario 1
    mock_system_to_test = MockSystemForTesting()
    security_tester = SecurityTestingFramework(mock_system_to_test)

    # Initialize components for Scenario 2
    comm_manager_for_blackout = MockCommManagerForBlackout()
    mock_beacon_for_blackout = MockEmergencyBeacon()
    blackout_detector = CommunicationBlackoutDetector(comm_manager_for_blackout, mock_beacon_for_blackout)
    
    flight_controller = MockFlightController()
    network_manager = MockNetworkManager()
    sensor_provider = MockSensorProvider()
    autonomous_recovery = AutonomousRecoveryManager(flight_controller, network_manager, sensor_provider)


    # --- Scenario 1: Security Testing ---
    print("\n--- Scenario 1: Adversarial Security Testing ---")
    security_tester.run_all_tests()
    

    # --- Scenario 2: Communication Blackout and Autonomous Recovery ---
    print("\n--- Scenario 2: Communication Blackout and Autonomous Recovery ---")
    print("Simulating total communication loss...")
    # Force all channels to appear inactive for the blackout simulation
    for module in comm_manager_for_blackout.get_all_modules().values():
        module._is_active = False

    # Run simulation loop for 12 seconds to trigger blackout
    for i in range(12):
        print(f"\n----- Blackout Simulation Cycle {i+1} -----")
        blackout_detector.run_check()
        # If a blackout is officially detected, the autonomous systems take over
        if blackout_detector.state == blackout_detector.state.BLACKOUT:
            sensor_provider.comm_blackout = True # Update the sensor provider with blackout status
            autonomous_recovery.run_recovery_check()
        time.sleep(1)

    print("\nSimulating communication restoration...")
    for module in comm_manager_for_blackout.get_all_modules().values():
        module._is_active = True
    blackout_detector.run_check()
    
    # Check recovery decision now that comms are back
    print("\n----- Post-Restoration Recovery Check -----")
    sensor_provider.comm_blackout = False
    autonomous_recovery.run_recovery_check()


    print("\nTesting, Validation & Operationalization conceptual simulation complete.")