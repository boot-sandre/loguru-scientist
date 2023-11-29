# Loguru Scientist

Loguru logging extension dedicated to data scientists.

## Installation

```bash
pip install loguru-logging
```

## Features

### METRIC Logging Level

The `METRIC` logging level is a custom feature designed to enhance the logging
capabilities for data scientists. It allows for the segregation of application
logs from metric logs, making it easier to track and analyze performance metrics 
and data trends. This level integrates seamlessly with existing logging systems, 
providing a straightforward way to log and monitor key metrics without cluttering 
the application logs.

#### USE CASE

You can use directly with import logger instance from loguru_scientist

```python
from loguru_scientist import logger

logger.metric("CV polygon detection", dict(accuracy=0.694648, edge_detected=125, polygon_detected=32))
```

#### HOWTO

If you want export in a file structured json record

```python
from loguru_scientist import logger
from loguru_scientist.scientist import configure_metrics_file_sink

configure_metrics_file_sink("metric/metrics.yaml", rotation="1 day")
logger.metric("CV polygon detection", dict(accuracy=0.694648, edge_detected=125, polygon_detected=32))
```

### Logging Context

The Logging Context feature introduces the ability to include a contextual 
dictionary in all log messages. This context can contain essential information 
such as the identifier of a case being processed. It enhances log messages with 
relevant data, allowing for more precise and efficient debugging and tracking. 

This feature is particularly useful in scenarios where tracking the flow and state 
of data through various processes is crucial.

#### USE CASE

```python
from loguru_scientist import logger

logger = logger.bind(project_id=2656, stage="eval")
```

## Contributing

Contributions are always welcome and greatly appreciated! Here's how you can contribute to this project:

1. **Fork the Project**: Start by forking the repository to your own GitHub account. This creates a copy of the project where you can make your changes.

2. **Create Your Feature Branch**: From your forked repository, create a new branch for your feature by running `git checkout -b feature/AmazingFeature`. This ensures that your changes are kept separate from the main project, making it easier to manage and merge your contributions.

3. **Commit Your Changes**: Once you've made your changes, commit them to your branch using `git commit -m 'Add some AmazingFeature'`. Be sure to write clear and meaningful commit messages that explain what changes you've made and why.

4. **Push to the Branch**: Upload your changes to your branch with `git push origin feature/AmazingFeature`. This makes your changes available on your GitHub fork.

5. **Open a Pull Request**: Finally, open a pull request from your feature branch to the main repository. This is where your changes will be reviewed before they can be merged into the project. Be sure to provide a detailed description of your changes and the reasons behind them.

We look forward to reviewing your contributions!
