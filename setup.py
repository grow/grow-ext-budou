from setuptools import setup


setup(
    name='grow-ext-budou',
    license='MIT',
    author='Grow Authors',
    author_email='hello@grow.io',
    include_package_data=False,
    packages=[
        'budou_ext',
    ],
    install_requires=[
        'budou',
        'google-api-python-client',
    ],
)
