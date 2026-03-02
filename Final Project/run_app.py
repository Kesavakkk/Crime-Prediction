#!/usr/bin/env python
import sys
import traceback
from dotenv import load_dotenv
import logging

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logger.info("Starting Flask app wrapper...")

logger.info("Importing application...")

try:
    from app import app, socketio
    logger.info("Application imported successfully")
except Exception as e:
    logger.error(f"Failed to import app: {e}")
    traceback.print_exc()
    sys.exit(1)

logger.info("Starting Flask server with WebSocket support on http://localhost:5000")

try:
    socketio.run(app, host="0.0.0.0", port=5000, debug=False, use_reloader=False, allow_unsafe_werkzeug=True)
except Exception as e:
    logger.error(f"Flask error: {e}")
    traceback.print_exc()
    sys.exit(1)
