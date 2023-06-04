from app import server
import os

if __name__ == "__main__":
    server.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT"), debug=True)
