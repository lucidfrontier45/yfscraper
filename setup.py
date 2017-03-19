from setuptools import setup

deps = [
    "bs4",
    "requests"
]

setup(
    name="yfscraper",
    version="0.1",
    description="yahoo finance japan parser",
    author="Shiqiao Du",
    author_email="lucidfrontier.45@gmail.com",
    packages=["yfscraper"],
    install_requires=deps
)
