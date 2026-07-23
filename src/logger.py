import logging
from pathlib import Path
from datetime import datetime
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)
logger= logging.getLogger(__name__)

LOG_FILE = LOG_DIR / f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.log"
logging.basicConfig(level=logging.INFO,format='%(asctime)s |  %(levelname)s |%(name)s |%(message)s',datefmt="%m/%d/%Y %I:%M:%S",
                    handlers=[
                        logging.FileHandler(LOG_FILE, encoding="utf-8"), 
                        logging.StreamHandler(), 
                        ])
logger.info(" should this be logged in a file?")
