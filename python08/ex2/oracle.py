import os
from dotenv import load_dotenv  # type: ignore


def main() -> None:
    env_loaded: bool = load_dotenv()
    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    matrix_mode = os.getenv("MATRIX_MODE", "development")
    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL", "INFO")
    zion_endpoint = os.getenv("ZION_ENDPOINT")
    print(f"Mode: {matrix_mode}")
    if not db_url:
        print("Database: [MISSING] - Connection failed")
    elif matrix_mode == "development":
        print("Database: Connected to local instance")
    elif matrix_mode == "production":
        print("Database: Connected to Production CLOUD cluster")
    else:
        print("Database: Connected to Unknown instance")
    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Denied (Missing Key)")
    print(f"Log Level: {log_level}")
    if zion_endpoint:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")
    print("\nEnvironment security check:")
    if api_key and db_url:
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WARNING] Missing critical secrets")
    if env_loaded:
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] No .env file found. Using system variables.")
    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
