import logging
from src.core.application.crudContainer import create, delete
def createContainer(**kwargs):
    '''This is create container'''
    logging.debug("Create container callsed")
    for k,v in kwargs.items():
        logging.debug(k,"=", v)
    create(*kwargs)
def deleteContainer(**kwargs):
    '''This is delete container'''
    logging.debug("Delete container callsed")
    for k,v in kwargs.items():
        logging.debug(k,"=", v)        