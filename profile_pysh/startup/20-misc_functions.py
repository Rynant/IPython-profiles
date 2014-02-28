import re, sys

if sys.version > '3.2':
	import urllib.request

	# Get current temperature
	def stj_current_temperature():
	    conditions_url = 'http://www.fairbanksmuseum.org/weatherwidget.php'
	    current_conditions = urllib.request.urlopen(conditions_url).read()
	    temp = re.findall(r'Temperature: \d+\.\d', str(current_conditions))[0]
	    return float(re.findall(r'\d+\.\d', temp)[0])

	ct = stj_current_temperature


def sunset(day=0):
    import ephem, datetime
    # Get sunset time
    obs = ephem.Observer()
    obs.lat = '44.41033'
    obs.long = '-72.00497'
    sun = ephem.Sun()
    day = datetime.datetime.now() + datetime.timedelta(days=day)
    obs.date = day
    return ephem.localtime(obs.next_setting(sun)).strftime(
            '%a, %b %d %Y, %I:%M %p')

