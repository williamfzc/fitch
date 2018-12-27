from setuptools import setup, find_packages


setup(
    name='fitch',
    version='0.1.0',
    description='UI automation based on opencv ',
    author='williamfzc',
    author_email='fengzc@vip.qq.com',
    url='https://github.com/williamfzc/fitch',
    packages=find_packages(),
    install_requires=[
        'pyminitouch',
        'findit',
        'fastcap',
        'pyatool',
    ]
)
