from datetime import datetime
import math

def test(t1, t2):
    tz1 = math.floor(int(t1[25:]) / 100) * 3600 + int(t1[25:]) % 100 * 60
    tz2 = math.floor(int(t2[25:]) / 100) * 3600 + int(t2[25:]) % 100 * 60
    date1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    date2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    delta = date1 - date2
    print(delta.total_seconds())

if __name__ == "__main__":
    test("Sat 02 May 2015 19:54:36 +0530", "Fri 01 May 2015 13:54:36 -0000")