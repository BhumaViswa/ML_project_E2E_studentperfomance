import logging
import os
from datetime import datetime
import sys
from exceptions import CustomException

LOG_FILE=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
# print(datetime.now())
LOG_FILE_dir=os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_FILE_dir, exist_ok=True)
LOG_FILE_path=os.path.join(LOG_FILE_dir, LOG_FILE)



logging.basicConfig(
    filename=LOG_FILE_path,
    level=logging.INFO,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
)

if __name__=="__main__":
    logging.info("logging has started")
    try:
        a=1/0
    except Exception as e:
        logging.info("logging has stopped")
        logging.info(CustomException(e, sys))
        
