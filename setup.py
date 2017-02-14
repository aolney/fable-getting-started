#!/usr/bin/env python

from subprocess import check_call, check_output
import json
import shutil

check_call('brew install npm', shell=True)
check_call('brew install yarn', shell=True)
check_call('npm install --global yarn', shell=True)
check_call('yarn install', shell=True)

# update GUID
new_guid = check_output('uuidgen').strip()
with open('src/Main.fsproj') as f:
    fsproj = f.read()
with open('src/Main.fsproj', 'w') as f:
    f.write(fsproj.replace('4057826A-1B4A-4553-832E-9570A3394346', new_guid))

package = json.loads(open('package.json').read())
package['name'] = raw_input('Project name: ')
package['description'] = raw_input('Project description: ')
package['repository'] = raw_input('Project repository: ')
with open('package.json', 'w') as f: 
    f.write(json.dumps(package, indent=4))
    

shutil.move('GettingStarted.sln', package['name'] + '.sln')

print 'Done! Now use "yarn" or "yarn watch" to compile.'
print 'The output file is in dist/index.html'