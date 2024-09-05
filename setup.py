# -*- coding: utf-8 -*-
from setuptools import setup

long_description = "Pandas Technical Analysis, Pandas TA, is a free, Open Source, and easy to use Technical Analysis library with a Pandas DataFrame Extension. It has over 200 indicators, utility functions and TA Lib Candlestick Patterns. Beyond TA feature generation, it has a flat library structure, it's own DataFrame Extension (called 'ta'), Custom Indicator Studies and Independent Custom Directory."

setup(
    name="pandas_ta_dev",
    packages=[
        "pandas_ta",
        "pandas_ta.candles",
        "pandas_ta.cycles",
        "pandas_ta.momentum",
        "pandas_ta.overlap",
        "pandas_ta.performance",
        "pandas_ta.statistics",
        "pandas_ta.transform",
        "pandas_ta.trend",
        "pandas_ta.utils",
        "pandas_ta.volatility",
        "pandas_ta.volume"
    ],
    version=".".join(("0", "4", "19b")),
    description=long_description,
    long_description=long_description,
    author="Kevin Johnson",
    author_email="appliedmathkj@gmail.com",
    url="https://github.com/twopirllc/pandas-ta",
    maintainer="Kevin Johnson",
    maintainer_email="appliedmathkj@gmail.com",
    download_url="https://github.com/twopirllc/pandas-ta.git",
    keywords=[
        "technical analysis", "finance", "trading", "backtest", "trading bot",
        "features", "pandas", "numpy", "numba", "vectorbt", "yfinance",
        "polygon", "python3"
    ],
    license="The MIT License (MIT)",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Science/Research",
        "Topic :: Office/Business :: Financial",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    package_data={
        "pandas_ta": ["py.typed"],
        "data": ["data/*.csv"],
    },
    install_requires=[
        "numba>=0.59.0",
        "numpy==1.26.4",
        "pandas>=2.2.0",
        "pandas-datareader",
        "scipy>=1.12"
    ],
    # List additional groups of dependencies here (e.g. development dependencies).
    # You can install these using the following syntax, for example:
    # $ pip install -e .[full,test]     # locally
    # $ pip install -U pandas_ta[full]  # pip
    extras_require={
        "full": [
            "alphaVantage-api", "matplotlib", "mplfinance",
            "python-dotenv", "sklearn", "statsmodels", "stochastic",
            "TA-Lib>=0.4.28", "tqdm", "vectorbt", "yfinance>=0.2.36"
        ],
        "test": [
            "numba>=0.59.0",
            "numpy==1.26.4",
            "pandas>=2.2.0",
            "pandas_datareader>=0.10.0",
            "pytest==7.1.2",
            "TA-Lib>=0.4.28",
            "yfinance>=0.2.36"
        ],
    },
)
