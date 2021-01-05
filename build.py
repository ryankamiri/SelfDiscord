import shutil
import os

#Delete SelfDiscord.egg-info
try:
    shutil.rmtree("SelfDiscord.egg-info/")
except:
    pass

#Delete dist
try:
    shutil.rmtree("dist/")
except:
    pass

#Delete build
try:
    shutil.rmtree("build/")
except:
    pass

#Run Setup
os.system("python setup.py sdist bdist_wheel")

#Upload to pypi
os.system("python -m twine upload --repository pypi dist/*")