def add_time (*tempo):

    startTime = ""
    timeToAdd = ""
    startTimeHours = 0
    startTimeMin = 0
    timeToAddHours = 0
    timeToAddMin = 0
    sumMin = 0
    sumHours = 0
    apMeridiem = 0
    car = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    dayNum = 0
    day = 0
    ret = ""

    if len(tempo) >= 2 and len(tempo) < 4:
        tmp = tempo[0].split(" ")
        startTime = tmp[0]
        if tmp[1] == "PM":
            apMeridiem = 1
        timeToAdd = tempo[1]
        if len(tempo) == 3:
            for i in range(len(car)):
                if tempo[2].capitalize() == car[i]:
                    day = i
    else:
        return 
    tmp = startTime.split(":")
    startTimeHours = int(tmp[0])
    startTimeMin = int(tmp[1])
    tmp = timeToAdd.split(":")
    timeToAddHours = int(tmp[0])
    timeToAddMin = int(tmp[1])
    sumHours = timeToAddHours + startTimeHours
    sumMin = timeToAddMin + startTimeMin
    if sumMin >= 60 :
        sumHours += 1
        sumMin -= 60
    while sumHours >= 24 :
        dayNum += 1
        sumHours -=24
    if apMeridiem % 2 == 0 :
        if sumHours >= 12 and sumHours <= 13:
            apMeridiem += 1
        elif sumHours >= 13 :
            apMeridiem += 1
            sumHours -= 12
    else :
        if sumHours >= 12 and sumHours <= 13:
            dayNum += 1
            apMeridiem += 1
        elif sumHours >= 13 :
            dayNum += 1
            apMeridiem += 1
            sumHours -= 12
        
    ret = str(sumHours) + ":"
    if sumMin < 10:
        ret += "0"
    ret += str(sumMin)
    ret += " AM" if apMeridiem % 2 == 0 else " PM"
    if len(tempo) == 3 :
        ret += ", " + car[(dayNum + day) % 7]
    if dayNum >= 1:
        if dayNum == 1:
            ret += " (next day)"
        else:
            ret += " (" + str(dayNum) + " days later)"
    return (ret)


def main():
    print(add_time("11:55 AM", "3:12"))

if __name__ == "__main__":
    main()


        
        

