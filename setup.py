import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package])

if __name__ == "__main__":
    #pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
    install("google-api-python-client") 
    install("google-auth-httplib2")
    install("google-auth-oauthlib")