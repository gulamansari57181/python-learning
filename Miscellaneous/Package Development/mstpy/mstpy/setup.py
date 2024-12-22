from setuptools import setup, find_packages

setup(
    name='mstpy',
    version='0.0',
    description='Calculate and visualize Gaussian, Binomial, and Normal distributions',
    long_description=open('README.txt').read(),  # Assuming you have a README.txt file
    long_description_content_type='text/plain',
    packages=find_packages(where='mstpy'),  # Pointing to the 'mstpy' subfolder where your code lives
    package_dir={'': 'mstpy'},  # Ensuring it looks in the right directory for packages
    author='Your Name',  # Optional: include your name
    author_email='gulamansari57181@gmail.com',
    zip_safe=False,
    classifiers=[  # Optional: Adds useful metadata about your package
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Optional: define the minimum required Python version
)
