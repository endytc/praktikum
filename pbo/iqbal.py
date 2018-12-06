class Jam():
  def __init__(self, jam, menit, detik):
    """
    The parameters jam, menit and detik have to be
    integers and must satisfy the following equations:
    0 <= h <24
    0 <= m < 60
    0 <= s < 60
    """
    self.set_Jam(jam, menit, detik)
		
  def set_Jam(self,jam, menit, detik):
    if type(jam) == int and 0 <= jam and jam < 24:
      self._jam = jam
    else:
      raise TypeError("Jam have to be integers between 0 and 23!")
    if type(menit) == int and 0 <= menit and menit < 60:
      self.__menit = menit
    else:
      raise TypeError("Menit have to be integers between 0 and 59!")
    
    if type(detik) == int and 0 <= detik and detik < 24:
      self.__detik = detik
    else:
      raise TypeError("Detik have to be integers between 0 and 59!")
		
  def __str__(self):
    return "{0:02d}:{1:02d}:{2:02d}".format(self.__jam,
                        self.__menit,
                        self.__detik)
		
  def tick(self):
    """
    menambahkan 1 detik
    """
    if self.__detik == 59:
      self.__detik = 0
      if self.__menit == 59:
        self.__menit = 0
        if self.__jam == 23:
          self.__jam = 0
        else:
          self.__jam += 1
      else:
        self.__menit += 1
    else:
      self.__detik += 1
			
class Kalender(object):
	bulan = (31,28,31,20,31,30,31,31,30,31,30,31)
	@staticmethod
	def leaptahun(tahun):
		""" cek tahun kabisat bukan """
		if not tahun % 4 == 0:
			return False
		else:
			return True
			
	def __init__(self,d,m,y):
		"""
		d, m, y have to be integer values and tahun has to be
		a four digit tahun number
		"""
		self.set_Kalender(d,m,y)
		
	def set_Kalender(self,d,m,y):
		"""
		d, m, y have to be integer values and tahun has to be
		a four digit tahun number
		"""
	
		if type(d) == int and type(m) == int and type(y) == int:
			self.__hari = d
			self.__bulan = m
			self.__tahun = y
		else:
			raise TypeError("d,m,y have to be integers!")
			
	def __str__(self):
		return "{0:02d}/{1:02d}/{2:4d}".format(self.__bulan,
												self.__hari,
												self.__tahun)
	
	def nextDay(self):
		"""
		This method nextDays to the next date.
		"""
		max_hari = Kalender.bulan[self.__bulan-1]
		if self.__bulan == 2 and Kalender.leaptahun(self.__tahun):
			max_hari +=1
		if self.__hari == max_hari:
			self.__hari = 1
			if self.__bulan == 12:
				self.__bulan = 1
				self.__bulan = 1
				self.__tahun +=1
			else:
				self.__bulan +=1
		else:
			self.__hari += 1
			
class KalenderJam(Jam,Kalender):
	"""
		The class KalenderJam implements a clock with integrated
		calendar. It's a case of multiple inheritance, as it inherits
		both from Jam and Kalender
	"""
	def __init__(self,hari,bulan,tahun,jam,menit,detik):
		Jam.__init__(self,jam, menit, detik)
		Kalender.__init__(self,hari,bulan,tahun)
		
	def tick(self):
		"""
		menambahkan jam 1 detik
		"""
		previous_jam = self._jam
		Jam.tick(self)
		if(self._jam < previous_jam):
			self.nextDay()
	
	def __str__(self):
		return Kalender.__str__(self) + "," + Jam.__str__(self) 
	
x = KalenderJam(31,12,2013,23,59,59)
print("One tick from",x, end="")
x.tick()
print("to",x)

# x = KalenderJam(28,2,1900,23,59,59)
# print("One tick from",x, end="")
# x.tick()
# print("to",x)		
			
# x = KalenderJam(28,2,2000,23,59,59)
# print("One tick from",x, end="")
# x.tick()
# print("to",x)		
								
# x = KalenderJam(7,2,2013,13,55,40)
# print("One tick from",x, end="")
# x.tick()
# print("to",x)	
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
			
		
