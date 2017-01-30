import logging, sys
logging.basicConfig(stream=sys.stderr)

sys.path.insert(0, '/var/www/html/elections_us')

from launch_app import app

application=app