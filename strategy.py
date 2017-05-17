import main
cooldown = 2
athresh = 10
ainc = 2


def aggro(hist, ohist, o2hist):
    alevel = (ohist.count("d") + o2hist.count("d"))*ainc - cooldown*len(hist)
    return "d" if alevel >= athresh else "c"



def shubik(hist, ohist, o2hist):
    count = 0
    for i in range(len(ohist)):
        if hist[i] == "c" and (ohist[i] == "d" or o2hist[i] == "d"):
            count += 1
    count -= (len(hist) - ''.join(hist).rfind('c') - 1)
    return "d" if count > 0 else "c"

def envy(hist, ohist, o2hist):
    points, opoints, o2points = main.getscores(hist, ohist, o2hist)
    return "d" if ((sum(opoints) + sum(o2points))/(len(opoints) + len(o2points))) > (sum(points)/len(points)) else "c"
