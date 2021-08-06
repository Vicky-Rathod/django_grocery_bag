import logging
from django.conf import settings
import datetime
import os

logger = logging.getLogger(__name__)

def rename_file():
    today = datetime.datetime.now()
    date_time = today.strftime("%H_%M_%S.txt")
    print("date and time:",date_time)
    file_path = settings.BASE_DIR /'test_folder/'
    os.chdir(file_path)
    print(os.getcwd())
    COUNT = 1
      
    # Function to increment count 
    # to make the files sorted.
    def increment():
        global COUNT
        COUNT = COUNT + 1
      
      
    for f in os.listdir():
        f_name, f_ext = os.path.splitext(f)
        f_name = date_time
        increment()
      
        new_name = '{} {}'.format(f_name, f_ext)
        os.rename(f, new_name)
    logger.info('Cron job was called')