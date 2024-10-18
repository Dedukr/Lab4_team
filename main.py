import os
from dotenv import load_dotenv, dotenv_values


load_dotenv()
TEXT=os.getenv("TEXT")

def ruslankonoz():
	print(TEXT)


if __name__ == '__main__':
	ruslankonoz()
