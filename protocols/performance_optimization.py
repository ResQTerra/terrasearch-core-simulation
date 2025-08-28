# Implements performance optimization techniques like bandwidth management and latency optimization.

import time
import random
from collections import deque

class BandwidthManager:
    """Dynamically allocates bandwidth and shapes traffic based on message priority."""
    def __init__(self, comm_manager):
        self.comm_manager = comm_manager
        self.message_queue = deque()

    def queue_message(self, message, priority):
        """Add a message to the queue with a given priority."""
        self.message_queue.append((priority, message))

    def process_queue(self):
        """Process the message queue, prioritizing high-priority messages."""
        # Sort queue by priority (higher number = higher priority)
        sorted_queue = sorted(list(self.message_queue), key=lambda x: x[0], reverse=True)
        self.message_queue = deque(sorted_queue)

        while self.message_queue:
            priority, message = self.message_queue.popleft()
            print(f"  - [BandwidthManager] Sending message with priority {priority}: {message}")
            self.comm_manager.send(message)

class LatencyOptimizer:
    """Optimizes for latency using techniques like multi-path transmission."""
    def __init__(self, comm_manager):
        self.comm_manager = comm_manager

    def send_critical_message(self, message):
        """Send a critical message over multiple paths simultaneously."""
        print(f"\n[LatencyOptimizer] Sending critical message over multiple paths: {message}")
        
        # Get the two best available communication channels
        best_channels = self._get_best_channels()
        
        if not best_channels:
            print("  - No active channels to send critical message.")
            return

        print(f"  - Using channels: {[ch.name for ch in best_channels]}")
        for channel in best_channels:
            channel.send(message)

    def _get_best_channels(self):
        # Conceptual: This would involve a more complex assessment of channel quality
        # For now, we'll just pick the first two active ones.
        active_modules = []
        for module in self.comm_manager.get_all_modules().values():
            if module.get_status()["active"]:
                active_modules.append(module)
        return active_modules[:2]

# Mock classes for demonstration
class MockCommManagerForPerf:
    def __init__(self):
        self.modules = {
            "mesh": MockCommManagerForPerf.MockCommModuleForPerf("mesh", is_active=True),
            "5g": MockCommManagerForPerf.MockCommModuleForPerf("5g", is_active=True),
            "satellite": MockCommManagerForPerf.MockCommModuleForPerf("satellite", is_active=False)
        }
    def send(self, message):
        # Simulate sending a message through the currently active comm mode
        pass
    def get_all_modules(self):
        return self.modules

class MockCommModuleForPerf:
    def __init__(self, name, is_active):
        self.name = name
        self._is_active = is_active
    def get_status(self):
        return {"active": self._is_active}
    def send(self, message):
        print(f"    - [{self.name}] Sent: {message}")

if __name__ == "__main__":
    comm_manager = MockCommManagerForPerf()

    # --- Bandwidth Management Demo ---
    print("--- Bandwidth Management Demo ---")
    bw_manager = BandwidthManager(comm_manager)
    bw_manager.queue_message("Low-priority telemetry data.", 1)
    bw_manager.queue_message("Critical flight command.", 10)
    bw_manager.queue_message("Medium-priority sensor reading.", 5)
    bw_manager.process_queue()

    # --- Latency Optimization Demo ---
    print("\n--- Latency Optimization Demo ---")
    lat_optimizer = LatencyOptimizer(comm_manager)
    lat_optimizer.send_critical_message("EMERGENCY: Abort mission!")

    print("\nPerformance Optimization simulation complete.")
