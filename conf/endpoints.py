#!/bin/bash
# coding: utf-8
# authors: Jerzy Wawro
# (C) Galicea 2021

from rest import api

from rest import  api_demo, api_my

def define():
  from . import cors
  api.add_namespace(api_my)
  api.add_namespace(api_demo)
