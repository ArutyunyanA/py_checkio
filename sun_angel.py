"""
Every true traveler must know how to do 3 things: fix the fire, find the water and
extract useful information from the nature around him. Programming won't help you 
with the fire and water, but when it comes to the information extraction - it might 
be just the thing you need.

Your task is to find the angle of the sun above the horizon knowing the time of the 
day. Input data: the sun rises in the East at 6:00 AM, which corresponds to the angle 
of 0 degrees. At 12:00 PM the sun reaches its zenith, which means that the angle 
equals 90 degrees. 6:00 PM is the time of the sunset so the angle is 180 degrees. 
If the input will be the time of the night (before 6:00 AM or after 6:00 PM), 
your function should return - "I don't see the sun!".
"""

from typing import Union


def sun_angle(time: str) -> Union[float, str]:
    h, m = map(int, time.split(':'))
    angel = 15 * h + m * 0.25 - 90
    if 0 <= angel <= 180:
        return angel
    else:
        return "I don't see the sun"
    return None


print("Example:")
print(sun_angle("07:00"))

assert sun_angle("07:00") == 15
assert sun_angle("12:15") == 93.75

print("The mission is done! Click 'Check Solution' to earn rewards!")

