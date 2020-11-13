#!/usr/bin/python3
##
print('Your settings can be retrieved from Utility -> System Setting -> System Status\n')

scope_id = "xxxx-xxxx-xxxx-xxxx"
serial_no = "SDS2xxxxxxxxxx"
model_no = "SDS2104X+"
software_version = "1.3.7R5"
uboot_versio = "5.0"
fpga_version = "2020-04-26"
cpld_version = "03"
hardware_version = "02-00"
#
# EEVBLOG defaults
SCOPEID = '0000000000000000'
Model	= 'SDS2000X+' #  'SDS1000X-E', 'SDS2000X-E', 'SDS2000X+', 'SDS5000X', 'ZODIAC-'
#
import hashlib

SCOPEID = scope_id.replace("-", "").lower()

def gen(x):
	h = hashlib.md5((
		hashkey +
		(Model+'\n').ljust(32, '\x00') +
		x.ljust(5, '\x00') +
		2*((SCOPEID + '\n').ljust(32, '\x00')) +
		'\x00'*16).encode('ascii')
	).digest()
	key = ''
	for b in h:
		if (b <= 0x2F or b > 0x39) and (b <= 0x60 or b > 0x7A):
			m = b % 0x24
			b = m + (0x57 if m > 9 else 0x30)
		if b == 0x30: b = 0x32
		if b == 0x31: b = 0x33
		if b == 0x6c: b = 0x6d
		if b == 0x6f: b = 0x70
		key += chr(b)
	return key.lower()

bwopt = ('100M', '200M', '350M', '500M', '750M', '1000M')
swopt = ('MAX', 'AWG', 'WIFI', 'MSO', 'FLX', 'CFD', 'I2S', '1553', 'PWA', 'MANC', 'SENT')
hashkey = '5zao9lyua01pp7hjzm3orcq90mds63z6zi5kv7vmv3ih981vlwn06txnjdtas3u2wa8msx61i12ueh14t7kqwsfskg032nhyuy1d9vv2wm925rd18kih9xhkyilobbgy'

print("Don't forget to enter the bandwidth keys in this order:\n100M-> 200M ->350M ->500M\n")
print('<< NB, the 750 and 1k options are here for completeness, not because they work AFAIK >>\n')
print('Your hashkeys for scope id {} are as follows:\n'.format(SCOPEID))
for opt in bwopt:
	print('Option: {:5}   \nKey:    {}-{}-{}-{}\n'.format(opt, gen(opt)[:4], gen(opt)[4:8], gen(opt)[8:12], gen(opt)[12:16]))
print('And now for the software options to go with your shiny new bandwidth...\n')
for opt in swopt:
	print('Option: {:5}   \nKey:    {}-{}-{}-{}\n'.format(opt, gen(opt)[:4], gen(opt)[4:8], gen(opt)[8:12], gen(opt)[12:16]))