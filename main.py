import json
from pprint import pprint

from loguru_scientist import logger
from loguru_scientist.scientist import configure_metrics_file_sink


if __name__ == "__main__":
    configure_metrics_file_sink(logger)
    logger = logger.bind(project_id=2656, stage="eval")
    logger.metric(
        "CV polygon detection start",
        accuracy=0.694648,
        edge_detected=125,
        polygon_detected=32,
    )
    logger.trace("This is a trace application logs")
    logger.debug("This is a debug application logs")
    logger.info("This is an info application logs")
    logger.warning("This is a warning application logs")
    logger.error("This is an error application logs")
    logger.exception("This is an exception application logs")
    logger.metric(
        "CV polygon detection end",
        **dict(accuracy=0.694648, edge_detected=500, polygon_detected=64),
    )
    logger.success("This is a success application logs")

    with open("../metric/metrics.log", "r") as f:
        pprint(json.loads(f.readlines()[-1]))
