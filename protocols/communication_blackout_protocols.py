
# Defines criteria for detecting communication loss and triggers emergency procedures.

import time
import random
import threading
from enum import Enum

class BlackoutState(Enum):
    NORMAL = 1
    DEGRADED = 2
    BLACKOUT = 3

class HeartbeatMonitor:
    """Actively monitors the health of communication channels."""
    def __init__(self, comm_modules):
        self.comm_modules = comm_modules

    def check_all_channels(self):
        active_channels = []
        for name, module in self.comm_modules.items():
            if self._is_channel_alive(module):
                active_channels.append(name)
        return active_channels

    def _is_channel_alive(self, module):
        # Conceptual: In a real system, this would involve sending a small
        # heartbeat message and expecting a timely response.
        return module.get_status()["active"]

class CommunicationBlackoutDetector:
    """Detects communication blackouts and manages the state."""
    def __init__(self, comm_manager, emergency_beacon, blackout_threshold=10):
        self.comm_manager = comm_manager
        self.emergency_beacon = emergency_beacon
        self.heartbeat_monitor = HeartbeatMonitor(comm_manager.get_all_modules())
        
        self.state = BlackoutState.NORMAL
        self.last_contact_time = time.time()
        self.blackout_threshold = blackout_threshold # seconds

    def run_check(self):
        print("\n[BlackoutDetector] Running check...")
        active_channels = self.heartbeat_monitor.check_all_channels()

        if active_channels:
            self.last_contact_time = time.time()
            if self.state == BlackoutState.BLACKOUT:
                print("  - Communication RESTORED.")
                self.emergency_beacon.deactivate()
            self.state = BlackoutState.NORMAL
        else:
            time_since_contact = time.time() - self.last_contact_time
            print(f"  - No active channels. Time since last contact: {time_since_contact:.1f}s")
            if time_since_contact > self.blackout_threshold:
                if self.state != BlackoutState.BLACKOUT:
                    print("  - BLACKOUT DETECTED. Activating emergency beacon.")
                    self.state = BlackoutState.BLACKOUT
                    self.emergency_beacon.activate()
            else:
                self.state = BlackoutState.DEGRADED
        
        print(f"  - Current State: {self.state.name}")

# Mock classes for demonstration
class MockCommModule:
    def __init__(self, name, is_active=True):
        self.name = name
        self._is_active = is_active
    def get_status(self):
        # Simulate module randomly failing
        if random.random() < 0.1:
            self._is_active = False
        return {"active": self._is_active}

class MockCommManager:
    def __init__(self):
        self.modules = {
            "mesh": MockCommModule("mesh"),
            "5g": MockCommModule("5g"),
            "satellite": MockCommModule("satellite")
        }
    def get_all_modules(self):
        return self.modules

class MockEmergencyBeacon:
    def __init__(self, cooldown_period=60):
        self.last_activated_time = 0
        self.cooldown_period = cooldown_period
        self.is_active = False

    def activate(self):
        current_time = time.time()
        if self.is_active:
            return

        if current_time - self.last_activated_time < self.cooldown_period:
            print("[MockBeacon] Activation attempted during cooldown. Ignoring.")
            return

        print("[MockBeacon] Activated!")
        self.is_active = True
        self.last_activated_time = current_time

    def deactivate(self):
        if not self.is_active:
            return
        print("[MockBeacon] Deactivated.")
        self.is_active = False

if __name__ == "__main__":
    comm_manager = MockCommManager()
    beacon = MockEmergencyBeacon(cooldown_period=5)
    detector = CommunicationBlackoutDetector(comm_manager, beacon)

    # Simulate normal operations
    print("--- Simulating normal operations ---")
    for _ in range(3):
        detector.run_check()
        time.sleep(1)

    # Simulate a total blackout
    print("\n--- Simulating total blackout ---")
    for module in comm_manager.get_all_modules().values():
        module._is_active = False
    
    for _ in range(12):
        detector.run_check()
        time.sleep(1)


