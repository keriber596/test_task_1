from fastapi import FastAPI, Depends
import sqlalchemy as sql
import sqlalchemy.orm as orm
import datetime
from pydantic import BaseModel
from typing import Optional, Union
import redis
import logging
import os
import requests