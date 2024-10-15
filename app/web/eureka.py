"""
Eureka Module
"""

import logging

import py_eureka_client.eureka_client as eureka_client

from app.config import App as appConfig


def register_app():
    """
    Method to register with Eureka
    """
    eureka_client.init(
        eureka_server = appConfig.EUREKA_URL,
        app_name = appConfig.APP_NAME,
        instance_port = appConfig.PORT,
        on_error = on_error,
    )
    logging.info("Service registered with Eureka")

def on_error(err_type: str, err: Exception):
    """
    Method to handle Eureka register errors
    """
    #logging.error(err_type, err)
    logging.info("Eureka client thrown error type of %s", err_type)
