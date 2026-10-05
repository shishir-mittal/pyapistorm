# PyAPIStorm: A Python alternative to JMeter for API testing and load testing

## Overview

PyAPIStorm is an asynchronous API performance testing utility, It reads a scenario file, separate user and payload input files, authenticates each selected user, reuses access tokens, invokes a target API at a global request rate, stores request outcomes in DuckDB, and writes a CSV or JSON report.