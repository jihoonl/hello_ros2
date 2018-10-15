from setuptools import setup
from setuptools import find_packages

package_name='my_python_pkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=[],
    py_modules=[
        'listener',
    ],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    author='Jihoon Lee',
    author_email='jihoon.lee@kakaobrain.com',
    maintainer='Jihoon Lee',
    maintainer_email='jihoon.lee@kakaobrain.com',
    license='proprietary',
    test_suite='test',
    entry_points={
        'console_scripts': [
            'listener = listener:main',
        ],
    },
)
