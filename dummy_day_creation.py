import datetime
import logging
import warnings

from daily_dummy_ingest.commands.run_model_command import RunModel

# set up parameters
FORMAT = '%(asctime)s: %(message)s'
logging.getLogger('boto').setLevel(logging.CRITICAL)

# Create a directory for logging
logging.basicConfig(format=FORMAT, level=logging.DEBUG)
                    # filename=f'daily_dummy_ingest/logging/DUMMY_LOAD: '
                    #          f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}.log')
warnings.filterwarnings("ignore")

startTime = datetime.datetime.now()
RunModel().run_model()

logging.info(f'Run time {datetime.datetime.now() - startTime}.')