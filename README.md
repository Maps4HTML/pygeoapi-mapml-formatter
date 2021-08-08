# pygeoapi-mapml-formatter

MapML Formatter Plugin for pygeoapi

## Installation

1. Install pygeoapi
2. Copy `mapml.py` into pygeoapi/pygeoapi/formatter
3. Add `'mapml'` to the [`FORMATS` array](https://github.com/geopython/pygeoapi/blob/master/pygeoapi/api.py#L79) on line 79.
4. Copy the below snipping into lines [1090](https://github.com/geopython/pygeoapi/blob/master/pygeoapi/api.py#L1110) and [1248](https://github.com/geopython/pygeoapi/blob/master/pygeoapi/api.py#L1263) of pygeoapi/api.py. Appending to the existing `if` `else if` blocks,

    ```python
    elif format_ == 'mapml':
      formatter = load_plugin('formatter', {'name': 'MapML', 'geom': True})
      content = formatter.write(
          data=content,
          options={}
      )

      headers_['Content-Type'] = '{}; charset={}'.format(
          formatter.mimetype, self.config['server']['encoding'])

      return headers_, 200, content
    ```

5. Add `'MapML': 'pygeoapi.formatter.mapml.MapMLFormatter'` to the formatters array on line [55](https://github.com/geopython/pygeoapi/blob/master/pygeoapi/plugin.py#L55) in the pygeoapi/plugin.py file
6. Build pygeoapi as you would before, now you can use `?f=mapml` to serve mapml features.
