from setuptools import setup

package_name = 'retina_pkg'

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
    maintainer='romain',
    maintainer_email='67638224+NootNook@users.noreply.github.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'image_subscriber = retina_pkg.image_subscriber:main',
            'uav_location_subscriber = retina_pkg.uav_location_subscriber:main'
        ],
    },
)
