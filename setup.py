from setuptools import setup

requirements = []
with open('requirements.txt') as f:
  requirements = f.read().splitlines()

readme = ''
with open('README.rst') as f:
    readme = f.read()

setup(name='SelfDiscord',
      author='RedBallG',
      url='https://github.com/RedBallG/SelfDiscord',
      project_urls={
        "Documentation": "https://github.com/RedBallG/SelfDiscord/tree/main/docs",
        "Issue tracker": "https://github.com/RedBallG/SelfDiscord/issues",
      },
      version=0.1,
      packages=['selfdiscord'],
      license='MIT',
      description='Discord API Wrapper for Self Bots',
      long_description=readme,
      long_description_content_type="text/x-rst",
      include_package_data=True,
      install_requires=requirements,
      python_requires='>=3.5.3',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
      ]
)