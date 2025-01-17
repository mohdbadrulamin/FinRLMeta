from __future__ import annotations

from setuptools import find_packages
from setuptools import setup

# Read requirements.txt, ignore comments
try:
    REQUIRES = list()
    f = open("requirements.txt", "rb")
    for line in f.read().decode("utf-8").split("\n"):
        line = line.strip()
        if "#" in line:
            line = line[: line.find("#")].strip()
        if line:
            REQUIRES.append(line)
except FileNotFoundError:
    print("'requirements.txt' not found!")
    REQUIRES = list()

setup(
    name="finrlmeta",
    version="0.3.6",
    author="Xiao-Yang Liu, Ming Zhu, Jingyang Rui, Hongyang Yang",
    author_email="hy2500@columbia.edu",
    url="https://github.com/mohdbadrulamin/FinRL-Meta.git",
    license="MIT",
    install_requires=REQUIRES,
    description="FinRL­-Meta: A Universe of ­ Market En­vironments for Data­-Driven Financial Reinforcement Learning",
    packages=find_packages(),
    long_description="FinRL­-Meta: A Universe of Near Real­ Market En­vironments for Data­-Driven Financial Reinforcement Learning",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    keywords="Reinforcment Learning",
    platform=["any"],
    python_requires=">=3.7",
)
