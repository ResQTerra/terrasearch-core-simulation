from cryptography.fernet import Fernet

class DoubleEncryption:
    """
    Implements a double encryption scheme using a VPN-like tunnel and E2E encryption.
    """
    def __init__(self, vpn_key, e2e_key):
        self.vpn_cipher = Fernet(vpn_key)
        self.e2e_cipher = Fernet(e2e_key)

    def encrypt(self, data):
        """
        Apply two layers of encryption.
        """
        # Layer 1: End-to-end encryption
        e2e_encrypted = self.e2e_cipher.encrypt(data.encode())
        
        # Layer 2: VPN tunnel encryption
        vpn_encrypted = self.vpn_cipher.encrypt(e2e_encrypted)
        
        print("[DoubleEncryption] Data encrypted with E2E and VPN layers.")
        return vpn_encrypted

    def decrypt(self, encrypted_data):
        """
        Remove two layers of encryption.
        """
        # Layer 2: VPN tunnel decryption
        e2e_encrypted = self.vpn_cipher.decrypt(encrypted_data)
        
        # Layer 1: End-to-end decryption
        decrypted_data = self.e2e_cipher.decrypt(e2e_encrypted).decode()
        
        print("[DoubleEncryption] Data decrypted from VPN and E2E layers.")
        return decrypted_data

# Example Usage
if __name__ == "__main__":
    # In a real system, these keys would be securely managed (e.g., via a key exchange)
    vpn_key = Fernet.generate_key()
    e2e_key = Fernet.generate_key()

    encryptor = DoubleEncryption(vpn_key, e2e_key)

    original_message = "This is a top secret drone command."
    print(f"Original message: {original_message}")

    # Encrypt the message
    encrypted_message = encryptor.encrypt(original_message)
    print(f"Encrypted message (first 20 bytes): {encrypted_message[:20]}...")

    # Decrypt the message
    decrypted_message = encryptor.decrypt(encrypted_message)
    print(f"Decrypted message: {decrypted_message}")

    assert original_message == decrypted_message
    print("\nEncryption and decryption successful.")
