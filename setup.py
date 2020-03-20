#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name="everviz",
    packages=find_packages(exclude=["tests", "test-data"]),
    package_data={"everviz": ["assets/axis_customization.css"]},
    description="",
    author="Equinor ASA",
    url="https://github.com/equinor/everviz",
    setup_requires=["pytest-runner", "setuptools_scm"],
    install_requires=[
        "pyyaml",
        "pandas",
        "numpy",
        "dash",
        "webviz-config",
        "plotly",
        "flask",
    ],
    test_suite="tests",
    use_scm_version={"write_to": "everviz/version.py"},
    classifiers=[
        "Programming language :: Python",
        "Programming language :: Python :: 3.6",
        "Programming language :: Python :: 3.7",
    ],
    entry_points={
        "webviz_config_plugins": [
            "Crossplot = everviz.plugins:Crossplot",
            "CrossplotIndexed = everviz.plugins:CrossplotIndexed",
            "SummaryPlot = everviz.plugins:SummaryPlot",
        ],
        "everest": ["everviz = everviz.everest_hooks",],
    },
)
