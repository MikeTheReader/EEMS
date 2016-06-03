from setuptools import setup

setup(
    name='EEMS',
    version='2.0.2',
    description='Environmental Evaluation Modeling System',
    url='https://github.com/consbio/EEMS',
    author='Tim Sheehan, M.S.',
    author_email='tim@consbio.org',
    license='BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Logic Modeling :: Tools',
        'Programming Language :: Python :: 2.7'
    ],
    keywords='environment,modeling,eems',
    packages=['eems'],
    install_requires=['numpy'],
)
