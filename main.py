from subprocess import call
from shutil import copyfile as cp
import random
import string
import os

while True:
	folders = ['c', 'cpp', 'csharp', 'go', 'java', 'js', 'php', 'python', 'r', 'swift']
	extensions = ['.c', '.cpp', '.cs', '.go', '.java', '.js', '.php', '.py', '.r', '.swift']
	folder = random.randint(0,9)

	nfiles = len(os.listdir('scripts/' + folders[folder]))
	new_name = 'x' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=12)) + str(nfiles) + extensions[folder]

	file = open('scripts/' + folders[folder] + '/' + new_name, 'w+')
	file.close()

	cp('scripts/' + folders[folder] + '/example' + extensions[folder], 'scripts/' + folders[folder] + '/' + new_name)

	file = open('commits.txt', 'r+')
	commits = int(file.read())
	file.close()
	file = open('commits.txt', 'w+')
	file.write(str(commits+1))
	file.close()
	commit_name = 'Commit #' + str(commits) + ' - added ' + new_name

	call(['git', 'add', '-A'])
	call(['git', 'commit', '-m', commit_name])
	call(['git', 'push', '-u', 'origin', 'master'])