from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
import yaml
import json

dict = """
{
    "suite": {
        "base_url": "http://localhost:2345",
        "setup": "sample_setup",
        "teardown": "sample_teardown",
        "tests":[
            {
                "name": "test_1",
                "path": "/abc1",
                "method": "GET",
                "headers": {
                    "USEREMAIL": "sew@gmail.com"
                },
                "payload": {
                  "heading": "Heading 1",
                  "font": {
                    "name": "Times New Roman",
                    "size": "22",
                    "color_theme": "ACCENT_1"
                  }
                },
                "assert": {
                  "expression": "output.res",
                  "value": "Times New Roman"
                }
            },
            {
                "name": "test_2",
                "path": "/abc2",
                "method": "GET",
                "headers": {
                    "USEREMAIL": "sew@gmail.com"
                },
                "payload": {
                  "heading": "Heading 2",
                  "font": {
                    "name": "Times New Roman",
                    "size": "22",
                    "color_theme": "ACCENT_2"
                  }
                },
                "assert": {
                  "expression": "output.res",
                  "value": "Times New Roman"
                }
            }

        ]
    }
}
"""
print(yaml.dump(json.loads(dict)))
