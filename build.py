import shutil
import os

#Delete SelfDiscord.egg-info
shutil.rmtree("SelfDiscord.egg-info/")

#Delete dist
shutil.rmtree("dist/")

#Delete build
shutil.rmtree("build/")

#Run Setup
os.system("python setup.py sdist bdist_wheel")

#Upload to pypi
os.system("python -m twine upload --repository pypi dist/*")