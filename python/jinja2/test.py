#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader
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
    env = Environment(loader=FileSystemLoader('./templates'))
    template = env.get_template('config.json')
    print(template.render(tpl_vars))
    
