from setuptools import setup, find_packages

setup(
    name="jsonapi",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    description="An extended JSON API for Python",
    author="June Feng",
)
