# Citations Network #
<!-- [![License](https://img.shields.io/badge/License-MPL%202.0-green.svg)](https://github.com/slidewiki/nlp-service/blob/master/LICENSE) -->
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
<!--[![Coverage Status](https://coveralls.io/repos/github/slidewiki/microservice-template/badge.svg?branch=master)](https://coveralls.io/github/slidewiki/microservice-template?branch=master)-->

This repository contains a pipeline written in Python (Luigi) that performs the following steps:
- Crawls DBLP and downloads open access papers
- Extracts reference list from them and builds the citation network
- Computes citation count and pagerank based algorithms for ranking papers in the network
- Creates an analytic report for the most influential and trending papers found in the above network


### Install Python ###
---
Please visit the wiki at [**Install Python**](http://docs.python-guide.org/en/latest/starting/installation/).


### Where to start developing? ###
---

```
# install pip 
sudo apt-get install python-pip

# install requirements
pip install -r requirements.txt

# Run the application
PYTHONPATH='.' luigi --module crawler Crawler --local-scheduler
...
```