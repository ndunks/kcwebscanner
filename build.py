#!/usr/bin/env python3
import sys
import os.path

file="source.txt"
if len(sys.argv) >= 2:
	file = sys.argv[1]

if not os.path.exists(file):
	print("File not found: ", file)
	print("USAGE:\n %s [source.txt]\n" % sys.argv[0])
	exit(1)

replace_char = None
replace_with = None


with open(file) as f:
	while True:
		line = f.readline()

		if not line: 
			break

		line = line.strip()
		if len(line) == 0:
			continue

		if line.startswith('#:config '):
			# remove config
			line = line[9:]

			if line.startswith('replace '):
				# remove replace
				line = line[9:]
				(char, sep, wit) = line.partition(' with ')
				if not char or not sep or not wit:
					continue

				if len(char) > 1:
					char = char.strip('"').strip("'")
				replace_char = char
				replace_with = []
				for i in wit.split(','):
					if len(i) > 1:
						i = i.strip('"').strip("'")
					replace_with.append(i)


				print('Replace Char "%s"' % replace_char, file=sys.stderr)
				print('\tWith', replace_with, file=sys.stderr)
				continue
		elif line[0] == '#':
			continue

		# Adding list
		print(line)

		# Replace chars
		if replace_char and line.find(replace_char) >= 0:
			for char in replace_with:
				print( line.replace(replace_char, char) )


