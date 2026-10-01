import logging
import os
from datetime import datetime

# 1. Define the log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2. Define the directory where logs will be stored
LOGS_DIR = os.path.join(os.getcwd(), "logs")

# 3. Create the directory if it doesn't exist
os.makedirs(LOGS_DIR, exist_ok=True)

# 4. Define the full path to the log file
LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE)

# 5. Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has started")