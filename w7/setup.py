import setuptools


setuptools.setup(
    name="my_mathematics", # Replace with your own username
    version="0.0.1",
    author="Inessa",
    author_email="author@example.com",
    description="My example package",
    long_description="My veeeeeery looooong description",
    long_description_content_type="text/markdown",
    url="https://github.com/Inessa-7/prog_mipt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['setuptools', 'wheel']
)
