import logging

from datetime import datetime

import os

Log_file=f"web_scrapper_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",Log_file)
os.makedirs(logs_path,exist_ok=True) 
log_file_path=os.path.join(logs_path,Log_file)

logging.basicConfig(
    filename=log_file_path,     
    level=logging.INFO,
    format='[%(asctime)s] %(lineno)d %(levelname)s - %(message)s', 
    datefmt='%Y-%m-%d %H:%M:%S'
)


if __name__ == "__main__":
    logging.info("Logging has been configured.")