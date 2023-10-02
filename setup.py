from setuptools import setup, find_packages

setup(name = "diamond_price_prediction",
    version = "0.0.1",
    author = "mukul",
    author_email = "mukulvarshney420@gmail.com",
    packages = find_packages(),
    install_requires = ["pandas", "numpy", "flask"]
    )
