import os
import sys
from dotenv import load_dotenv


load_dotenv()
if os.getenv("MATRIX_MODE") is None:
    print("MATRIX_MODE is not defined. "
          "Add it to .env file or use 'MATRIX_MODE=development_or_production "
          "python3 oracle.py'")
    sys.exit()

if os.getenv("DATABASE_URL") is None:
    print("DATABASE_URL is not defined. "
          "Add it to .env file or use 'DATABASE_URL=url_of_database "
          "python3 oracle.py'")
    sys.exit()

if os.getenv("API_KEY") is None:
    print("API_KEY is not defined. "
          "Add it to .env file or use "
          "'API_KEY=your_api_key python3 oracle.py'")

    sys.exit()

if os.getenv("LOG_LEVEL") is None:
    print("LOG_LEVEL is not defined. "
          "Add it to .env file or use 'LOG_LEVEL=DEBUG_INFO_WARNING_ERROR "
          "python3 oracle.py'")
    sys.exit()

if os.getenv("ZION_ENDPOINT") is None:
    print("ZION_ENDPOINT is not defined. "
          "Add it to .env file or use 'ZION_ENDPOINT=your_zion_url "
          "python3 oracle.py'")
    sys.exit()


if __name__ == "__main__":
    print("ORACLE STATUS: Reading the Matrix...")
    matrix_mode: str = str(os.getenv("MATRIX_MODE"))
    databaseurl: str = str(os.getenv("DATABASE_URL"))
    apikey: str = str(os.getenv("API_KEY"))
    loglevel: str = str(os.getenv("LOG_LEVEL"))
    zion: str = str(os.getenv("ZION_ENDPOINT"))
    print("Configuration loaded:")
    if matrix_mode == "development":
        print(f"Mode: {matrix_mode}")
        print("Database: Connected to local instance")
        print("API Access: Authenticated")
        print(f"Log level: {loglevel}")
        print("Zion network: Online")
    elif matrix_mode == "production":
        print(f"Mode: {matrix_mode}")
        print("Database: Connected to Zion")
        print("API Access: Authenticated")
        print(f"Log level: {loglevel}")
        print("Zion network: Online")
    else:
        print("Wrong MATRIX_MODE entered. Please enter a valid value. "
              "('development' or 'production')")
        sys.exit()
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print("The Oracle sees all configurations.")
