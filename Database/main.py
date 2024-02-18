import schedule
from datetime import time, timedelta, datetime
import subprocess

def job():
    subprocess.call(['python', 'Database\Internshala\IBD.py'])
    subprocess.call(['python', 'Database\Internshala\ICC.py'])
    subprocess.call(['python', 'Database\Internshala\IFD.py'])
    subprocess.call(['python', 'Database\Internshala\IGD.py'])
    subprocess.call(['python', 'Database\Internshala\IID.py'])
    subprocess.call(['python', 'Database\Internshala\ISMM.py'])
    subprocess.call(['python', 'Database\Internshala\IUIUX.py'])
    subprocess.call(['python', 'Database\Internshala\IWD.py'])

    subprocess.call(['python', 'Database\Shine\SBD.py'])
    subprocess.call(['python', 'Database\Shine\SCC.py'])
    subprocess.call(['python', 'Database\Shine\SFD.py'])
    subprocess.call(['python', 'Database\Shine\SGD.py'])
    subprocess.call(['python', 'Database\Shine\SID.py'])
    subprocess.call(['python', 'Database\Shine\SSMM.py'])
    subprocess.call(['python', 'Database\Shine\SUIUX.py'])
    subprocess.call(['python', 'Database\Shine\SWD.py'])
    

schedule.every(1).minutes.do(job)

while True: 
    schedule.run_pending()
tm.sleep(1)
