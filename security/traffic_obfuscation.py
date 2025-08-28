
import random
import time
import threading

class TrafficObfuscation:
    """
    Obfuscates traffic patterns to prevent analysis.
    """
    def __init__(self, send_function):
        self.send_function = send_function
        self.is_active = False
        self.thread = None

    def start(self):
        """
        Start the traffic obfuscation thread.
        """
        if not self.is_active:
            self.is_active = True
            self.thread = threading.Thread(target=self._obfuscate_traffic, daemon=True)
            self.thread.start()
            print("[TrafficObfuscation] Started.")

    def stop(self):
        """
        Stop the traffic obfuscation thread.
        """
        if self.is_active:
            self.is_active = False
            if self.thread:
                self.thread.join()
            print("[TrafficObfuscation] Stopped.")

    def _obfuscate_traffic(self):
        """
        Send dummy packets at random intervals to obfuscate real traffic.
        """
        while self.is_active:
            try:
                time.sleep(random.uniform(0.1, 2.0))  # Random delay
                dummy_packet = self._generate_dummy_packet()
                self.send_function(dummy_packet)
                print(f"[TrafficObfuscation] Sent dummy packet of size {len(dummy_packet)}")
            except Exception as e:
                print(f"[TrafficObfuscation] Error: {e}")

    def _generate_dummy_packet(self):
        """
        Generate a dummy packet of random size.
        """
        size = random.randint(64, 1024)  # Realistic packet sizes
        return random.randbytes(size)

# Example Usage
if __name__ == "__main__":
    def mock_send(packet):
        # In a real system, this would send the packet over the network
        pass

    obfuscator = TrafficObfuscation(mock_send)

    print("Starting traffic obfuscation for 10 seconds...")
    obfuscator.start()
    time.sleep(10)
    obfuscator.stop()
    print("\nTraffic obfuscation example complete.")
