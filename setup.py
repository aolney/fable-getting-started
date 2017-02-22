#!/usr/bin/env python

from subprocess import check_call, check_output
import json
import shutil

check_call('brew install yarn', shell=True)
check_call('yarn install', shell=True)

package = json.loads(open('package.json').read())
package['name'] = raw_input('Project name: ')
package['description'] = raw_input('Project description: ')
package['repository'] = raw_input('Project repository: ')
with open('package.json', 'w') as f: 
    f.write(json.dumps(package, indent=2))
    

shutil.move('GettingStarted.sln', package['name'] + '.sln')

print 'Done! The project is now built. Use "yarn watch" to live compile as you save.'
print 'You can open dist/index.html in your browser to run your code'