class Section(object):
    # section enemies spawn class (section number, starting x axis, ending x axis, y axis that enemies spawn,
    # earliest time enemy can spawn, latest enemy can spawn)
    def __init__(self, section, start_point, end_point, yaxis, earliestCD, latestCD, CD):
        self.section = section
        self.startPoint = start_point
        self.endPoint = end_point
        self.midPoint = (end_point + start_point) / 2
        self.xaxis = (start_point, end_point)
        self.yaxis = yaxis
        self.earliestCD = earliestCD
        self.latestCD = latestCD
        self.CD = CD