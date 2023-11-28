
# What Sticks 10 Library

![What Sticks Logo](/docs/images/wsLogo_200px.png)

## Description
What Sticks 10 Library is a collection of custom Python packages designed to support the functionality of the What Sticks platform.

## Installation Instructions
To install the What Sticks 10 Library, clone the repository and install the required dependencies:
```
git clone [repository-url]
cd WhatSticks10Library
pip install -e .
```



## Usage
After installation, import the modules into your Python projects as needed:

```python
from ws_config import ConfigLocal, ConfigDev, ConfigProd
from ws_models import Base, create_engine, inspect, sess, engine, text, \
    Users,
    CommunityPosts, CommunityComments,NewsPosts, NewsComments, \
    UserLocationDay, Locations, WeatherHistory, \
    OuraToken, OuraSleepDescriptions
```

## Features

Data Processing: Modules for processing and analyzing data within the What Sticks ecosystem.
API Integration: Tools for seamless integration with the What Sticks API.
Analytics: Advanced analytics capabilities to derive insights from data.

## Contributing

We welcome contributions to the What Sticks 10 Library project. Please read our contributing guidelines for more information on how to contribute.


For any queries or suggestions, please contact us at nrodrig1@gmail.com.