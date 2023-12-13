
class Time:
    def __init__(self , hh, mm, ss):
        #properties
        self.hour = hh
        self.minute = mm
        self.second = ss
        self.fix()


        #method
    def show(self):
        print(self.hour ,":" , self.minute ,":", self.second)

    def sum(self , other):
        s_new = self.second + other.second
        m_new = self.minute + other.minute
        h_new = self.hour + other.hour


        result = Time(h_new , m_new , s_new)
        return result
    

    def sub(self , other):
        s_new = self.second - other.second
        m_new = self.minute - other.minute
        h_new = self.hour - other.hour
        result = Time(h_new , m_new , s_new)
        return result
    

    def second_to_time(self,second):
        Calculated_HOUR=second//3600
        b=second-3600*Calculated_HOUR
        Calculated_MINUTE=b//60
        Calculated_SECOND=b-60*Calculated_MINUTE
        result=Time(Calculated_HOUR,Calculated_MINUTE,Calculated_SECOND)
        return result
    
    def time_to_second(self, other):
        Calculated_SECOND= other.hour*3600 + other.minute*60 + other.second
        result=Calculated_SECOND
        return result

    def gmt_to_tehran(self):
        t=Time(3, 30, 0)
        tehran_time=self.sum(t)
        return tehran_time
    

    def fix(self):

        if self.second >= 60:
            self.second -= 60
            self.minute +=1

        if self.minute >= 60:
            self.minute -= 60
            self.hour +=1

        if self.minute < 0:
            self.minute += 60
            self.hour -= 1

        if self.second < 0:
            self.second += 60
            self.minute -= 1



t1 = Time(3, 45 , 17)
t1.show()        
t2 = Time(4, 23 , 2)
t2.show()
t3 = t1.sum(t2)
t3.show()

tehran_time=t1.gmt_to_tehran()
tehran_time.show()

seconds=tehran_time.time_to_second()
print("Seconds : ", seconds)

time=Time.seconds_to_time(5600) 
time.show()