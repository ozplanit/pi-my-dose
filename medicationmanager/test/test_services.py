# Title     : TODO
# Objective : TODO
# Created by: dean.wright
# Created on: 25/10/2017

import datetime
import time
import asyncio

from medicationmanager.services.core import DoseAlarm


def test_alarm():
    notificationqueue = asyncio.Queue(10)
    alarmfor = "Dean"
    alarmdue = datetime.datetime.now() + datetime.timedelta(minutes=1)
    alarm = DoseAlarm(alarmfor, alarmdue, notificationqueue)
    alarm.start()
    queueisempty = True

    while notificationqueue.empty():
        print("Alarm notifciation queue is empty " + datetime.datetime.now().ctime() + " is the current time.")
        time.sleep(5)

    print("Alarm notification for " + notificationqueue.get())


test_alarm()



async def print_every_second():
    "Print seconds"
    while True:
        for i in range(60):
            print(i, 's')
            await asyncio.sleep(1)


async def print_every_minute():
    for i in range(1, 10):
        await asyncio.sleep(60)
        print(i, 'minute')


loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.gather(print_every_second(),
                   print_every_minute())
)
loop.close()
