import requests


class GoogleDisk:
	def __init__(self):
		self.translation_url = "https://drive.google.com/uc" \
		                       "?id=1qss90wEiuWHR-xYpcbaw7YzBa66WPY4i&authuser=0&export=download"
		self.program_url = "https://drive.google.com/uc" \
		                       "?id=1ADJEECLYXmf8yHxpSFHpf5ba5-mNLu6U&authuser=0&export=download"

	def download_file(self, url, dst_filename):
		response = requests.get(url, allow_redirects=True)
		with open(dst_filename, "wb") as f:
			f.write(response.content)

	def download_translation(self):
		self.download_file(self.translation_url, "trans.zip")

	def download_program(self):
		self.download_file(self.program_url, "setup.exe")
