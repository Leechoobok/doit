from calendar import c
import FourCal

class SafeFourCal(FourCal.FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
