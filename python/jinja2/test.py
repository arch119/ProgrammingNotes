#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader
import os
tpl_vars={
    'user':{
        'name' : 'shambhu',
    },
    'results':[
        { 'status': 100 },
        { 'status': 200 }
    ]
}
if __name__ == '__main__':
    dirname= os.path.dirname(os.path.abspath(__file__))
    env = Environment(loader=FileSystemLoader(os.path.join(dirname, 'templates')))
    template = env.get_template('config.json')
    print(template.render(tpl_vars))
    
