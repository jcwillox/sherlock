from setuptools import setup

with open("requirements.txt", "r", encoding="UTF-8") as file:
    REQUIREMENTS = file.readlines()

setup(install_requires=REQUIREMENTS)
