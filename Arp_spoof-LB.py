import os
import re
# Runs the arp -a command and assigns the output to the 'data' variable
with os.popen('arp -a') as arp:
    data = arp.read()

    arp_table = []
# From the 'data' variable extracts the lines containing the ip, & Mac addresses, along with their state
    for line in re.findall('([-.0-9]+)\s+([-0-9a-f]{17})\s+(\w+)',data):
        arp_table.append(list(line))

filtered_arp = {}

x = 0
#for each list in the arp_table: for each ip in the list: Assign the IP address to the corresponding MAC address in a dictionary type
for list in arp_table:
    for ip in list:
        filtered_arp[ip] = arp_table[x][1]
        x += 1
        break

arp_spoof_check = []

#For each dictionary pair: Check if the MAC address is in the new list. If its not in the list, it will add it to the list.
for pair in filtered_arp:
    x = filtered_arp.get(pair)
    if x not in arp_spoof_check:
        arp_spoof_check.append(x)
    elif x in arp_spoof_check:
        print(f'{x} is being spoofed')
    else: print('No spoofing detected')

#^^If a MAC appears in the list more than once, it will tell notify you of which MAC is being spoofed.(Not Including the Brodacast Domain (ff-ff-ff-ff)