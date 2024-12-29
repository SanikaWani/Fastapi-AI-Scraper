import secrets

def generate_secret_key(length: int = 32) -> str:
    return secrets.token_hex(length // 2)

# Example usage
if __name__ == "__main__":
    secret_key = generate_secret_key()
    print(f"Your generated secret key: {secret_key}")
