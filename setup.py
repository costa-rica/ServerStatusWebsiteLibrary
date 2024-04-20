from setuptools import setup

setup (
    name="ss-library",
    version = "0.1",
    author="NickRodriguez",
    author_email="nick@dashanddata.com",
    description = "ss stands for Server Status (Webstite). This is a started modules kit",
    packages=['ss_config','ss_models'],
    python_requires=">=3.10",
    )