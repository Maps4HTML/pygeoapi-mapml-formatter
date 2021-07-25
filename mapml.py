import logging
from xml.etree.ElementTree import Element, SubElement, tostring

from pygeoapi.formatter.base import BaseFormatter

LOGGER = logging.getLogger(__name__)


class MapMLFormatter(BaseFormatter):
    """MapML formatter"""

    def __init__(self, formatter_def):
        super().__init__({'name': 'mapml', 'geom': None})
        self.mimetype = 'text/mapml'

    def write(self, options={}, data=None):
        """
        Generate data in MapML format
        :returns: string representation of format
        """
        mapml = Element('mapml', {'xmlns':'http://www.w3.org/1999/xhtml'})
        head = SubElement(mapml, 'head')
        title = SubElement(head, 'title')

        body = SubElement(mapml, 'body')

        if data['type'] == 'FeatureCollection':
            for f in data['features']:
                body.append(self.__generateFeature(f))
        elif data['type'] == 'Feature':
            body.append(self.__generateFeature(data))
        
        return tostring(mapml)

    def __generateFeature(self, f):
        type = f['geometry']['type'].lower()
        featureElem = Element('feature')
        properties = SubElement(featureElem, 'properties')
        name = SubElement(properties, 'h1')

        name.text = f['properties']['name'] if 'name' in f['properties'] else f['properties']['stn_id']
        geometry = SubElement(featureElem, 'geometry')
                    
        geometrySubtype = SubElement(geometry, type)
        if type == 'multipolygon':
            for p in f['geometry']['coordinates']:
                polygon = SubElement(geometry, 'polygon')
                polygon.text = self.__coordToStringPair(p)
        else:
            geometrySubtype.text = self.__coordToStringPair(f['geometry']['coordinates'])

        return featureElem

    def __coordToStringPair(self, coords):
        if type(coords[0]) == list:
            cString = ''
            for pair in coords[0]:
                cString += str(pair[0]) + ' ' + str(pair[1]) + ' '
            return cString[:-1]
        else: 
            return str(coords[0]) + ' ' +  str(coords[1])
