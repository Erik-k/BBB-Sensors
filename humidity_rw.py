# Read from HIH-6130 Honeywell Humidity/Temp sensor
# and store to a txt file. This program will run continuously.
# Make sure to have it run silently (no printing) when using crond.
# Also, "$ time python humidity_rw.py" says it takes about .530s to
# run when using cpufreq governor ondemand, 0.7s when using powersave,
# and about .34s when using performance (700MHz, no switching). So be
# sure to consider that if you want to schedule it at rates >1Hz.
import smbus
import time

b = smbus.SMBus(1)
d = []
addr = 0x27

b.write_byte(0x27, 0x00)
time.sleep(0.050)

d = b.read_i2c_block_data(addr, 0)
status = (d[0] & 0xc0) >> 6
humidity = (((d[0] & 0x3f) << 8) + d[1])*100/16383
tempC = ((d[2] << 6) + ((d[3] & 0xfc) >> 2))*165/16383 - 40
tempF = tempC*9/5 + 32

time_now = time.localtime()
f = open("/home/root/humidityAndTemp_readings/%s.txt" % time.strftime('%Y_%b_%d_%a'), 'a') 

# Allowing this output really fills up the journalctl when cron is running this at 1Hz
#print "Data:       ", "%02x "*len(d)%tuple(d)
#print "Status:     ", status
#print "Humidity:   ", humidity, "%"
#print "Temperature:", tempC, "C"

str_hum = str(humidity)
str_temp = str(tempC)
f.write('{0} {1} {2}\n'.format(time.strftime('%H:%M'), str_hum, str_temp))
