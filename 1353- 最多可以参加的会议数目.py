def maxEvents(events):
    """
    :type events: List[List[int]]
    :rtype: int
    """
    events_length = len(events)
    return events + "1" + str(events_length)
print(maxEvents("hello"))
    
