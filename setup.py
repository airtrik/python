import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="airtrik",
    version="0.1.3",
    author="Vishal Pandey",
    author_email="hello@airtrik.com",
    description="Connect IoT Devices to cloud and manage from anywhere.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/airtrik/python",
    packages=setuptools.find_packages(),
    install_requires=[
        'paho-mqtt',
        'requests',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)