from setuptools import find_packages, setup

package_name = 'gui2ros'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Jake Bonney',
    maintainer_email='jakebonney10@uri.edu',
    description='ROS2 Package for interfacing with Howland ROV GUI',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'gui_listener = gui2ros.gui_listener:main'
        ],
    },
)
