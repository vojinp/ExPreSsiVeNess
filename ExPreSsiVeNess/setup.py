from setuptools import setup, find_packages

setup(
    name="expressiveness-core",
    version="0.1",
    packages=find_packages(),
    install_requires=['Django>=1.10'],
    namespace_packages=['Core'],
    provides=['Core'],
    zip_safe=False
)

