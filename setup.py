from setuptools import setup

read_me_description = ""
with open("README.rst") as file:
    read_me_description = file.read()

requirements = []
with open('requirements.txt') as f:
  requirements = f.read().splitlines()

setup(
    name="SelfDiscord",
    version="0.1",
    author="RedBallG",
    author_email="studiosredmotion@gmail.com",
    description="Discord API Wrapper for Self Bots",
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RedBallG/SelfDiscord",
    packages=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)