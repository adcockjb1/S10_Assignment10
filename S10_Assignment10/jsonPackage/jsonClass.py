# File Name : json.py
# Student Name: Asfia Siddiqui
#               Joseph Adcock
#               Kengo Ishizuka
#               Nogaye Gueye
# email: siddiqaf@mail.uc.edu
#        adcockjb@mail.uc.edu
#        ishizuko@mail.uc.edu
#        gueyene@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 4/10/25
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Research an API on the web, use it to populate a Python data structure. Analyze the data and put it into a CSV file

# Brief Description of what this module does. Ingest a json from a web api and print out the top 10 results from the data.
# Citations: https://www.freepublicapis.com/api
#             https://stackoverflow.com/questions/68962029/error-reading-json-file-containing-square-brackets-in-python

# Anything else that's relevant:

import json
import requests

class JsonTool():
    """
    A class for using json APIs to parse data and move it to a CSV
    params: n/a
    returns: n/a
    """
