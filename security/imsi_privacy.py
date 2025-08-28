import time
import hashlib

# This mock class is now complete with all methods needed for the simulation.
class MockHSMService:
    def get_secret(self, key_id):
        return "a_very_secret_key"

    def verify_signature(self, public_key, data, signature):
        # This logic is taken from the other mock definition to make this one complete.
        return signature == f"SIGNED({data})_BY_{public_key}"

class IMSIPrivacy:
    """
    Manages IMSI privacy by generating and rotating pseudonymous identifiers.
    """
    def __init__(self, hsm_service):
        self.hsm_service = hsm_service
        self.current_pseudonym = None
        self.generation_time = 0
        self.rotation_interval = 3600  # seconds

    def get_pseudonym(self):
        """
        Get the current pseudonym, generating a new one if it's time to rotate.
        """
        if not self.current_pseudonym or self._is_rotation_due():
            self._generate_new_pseudonym()
        return self.current_pseudonym

    def _is_rotation_due(self):
        """
        Check if the pseudonym needs to be rotated.
        """
        return (time.time() - self.generation_time) > self.rotation_interval

    def _generate_new_pseudonym(self):
        """
        Generate a new pseudonym using a timestamp and a secret from the HSM.
        """
        timestamp = str(time.time())
        hsm_secret = self.hsm_service.get_secret("imsi_privacy_key")
        data_to_hash = timestamp + hsm_secret
        
        # Use a cryptographic hash to generate the pseudonym
        self.current_pseudonym = "pseudo_imsi_" + hashlib.sha256(data_to_hash.encode()).hexdigest()
        self.generation_time = time.time()
        print(f"[IMSIPrivacy] New pseudonym generated: {self.current_pseudonym}")

# Example Usage (requires a mock HSM service)
if __name__ == "__main__":
    hsm = MockHSMService()
    imsi_manager = IMSIPrivacy(hsm)
    
    print("First pseudonym:", imsi_manager.get_pseudonym())
    print("Second pseudonym (should be the same):", imsi_manager.get_pseudonym())
    
    # Simulate time passing for rotation
    imsi_manager.rotation_interval = 0
    time.sleep(1)
    
    print("Third pseudonym (should be different after rotation):", imsi_manager.get_pseudonym())