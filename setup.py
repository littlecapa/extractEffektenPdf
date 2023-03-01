from setuptools import find_packages, setup
setup(
    name='extractEffektenPdf',
    packages=find_packages(),
    version='0.1.0',
    description='Get recommendations from Effekten PDF',
    author='littlecapa@googlemail.com',
    license='MIT',
    install_requires=['PyPDF2'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)