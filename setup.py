from setuptools import setup, find_packages

setup(
    name='tomo-axis',
    version='1.0',
    author='Maria Matveeva',
    author_email='matveeva.maria@gmail.com',
    license='LGPL',
    packages=find_packages(),
    scripts=['tomo-axis'],
    description="Computing axis of rotation",
    install_requires=['pyqtgraph',
                      'numpy',
                      'scipy'],
)
