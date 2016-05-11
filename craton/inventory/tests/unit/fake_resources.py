"""
Provides some fake resources - region, cell, host and other related
objects for test.
"""

class Cell(object):
    def __init__(self, name, status, region_id, project_id, variables):
        self.name = name
        self.status = status
        self.region_id = region_id
        self.project_id = project_id
        self.variables = variables

CELL1 = Cell("cell1", "active", "1", "abcd", {"key1": "value1", "key2": "value2"})
CELL2 = Cell("cell2", "active", "2", "abcd", {"key3": "value3", "key4": "value4"})

CELL_LIST =[CELL1, CELL2]


class Region(object):
    def __init__(self, name, project_id, variables):
        self.name = name
        self.project_id = project_id
        self.variables = variables

REGION1 = Region("region1", "abcd", {"key1": "value1", "key2": "value2"})
REGION2 = Region("region2", "abcd", {"key3": "value3", "key4": "value4"})

REGIONS_LIST = [REGION1, REGION2]
