class Colors:
	# red
	def red(self,number):
		return "\033[" +str(number)+ ";31m"
	# green
	def green(self,number):
		return "\033[" +str(number)+ ";32m"
	# yellow
	def yellow(self,number):
		return "\033[" +str(number)+ ";33m"
	# blue
	def blue(self,number):
		return "\033[" +str(number)+ ";34m"
	# purple
	def purple(self,number):
		return "\033[" +str(number)+ ";35m"
	# cyan
	def cyan(self,number):
		return "\033[" +str(number)+ ";36m"
	# white
	def white(self,number):
		return "\033[" +str(number)+ ";38m"
	# end
	def end(self):
		return "\033[0m"
