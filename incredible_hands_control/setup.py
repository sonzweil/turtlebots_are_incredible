from setuptools import setup

package_name = 'incredible_hands_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sonz',
    maintainer_email='smartsonzweil@gmail.com',
    description='Turtlebot3 Hands Control with mediapipe and OpenCV<',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'incredible_hands_control_publisher = incredible_hands_control.hands_control_publisher:main',
        ],
    },
)
