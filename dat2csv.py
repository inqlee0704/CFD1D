import sys

plt_nd_file = str(sys.argv[1])

# read
with open(f'data_plt_nd/{plt_nd_file}','r') as f:
    lines = f.readlines()
f.close()

# get a new header
hdr = lines[0].strip()
hdr = hdr.replace("\"","")
hdr = hdr.replace("VARIABLES=","")
hdr = hdr.split(' ')
new_hdr = [x for x in hdr if x!='']
new_hdr = ','.join(new_hdr) + '\n'

# convert ' ' to ','
new_lines = []
new_lines.append(new_hdr)
for line in lines[3:]:
    new_line = line.strip()
    new_line = new_line.split(' ')
    new_line = [x for x in new_line if x!='']
    new_line = ','.join(new_line) + '\n'
    new_lines.append(new_line)

# save
with open(f"data_plt_nd_csv/{plt_nd_file.split('.')[0]}.csv", 'w') as f2:
    for line in new_lines:
        f2.write(str(line))
f2.close()