import get_temp

inside_temp = get_temp.read_temp(get_temp.inside_device)
outside_temp = get_temp.read_temp(get_temp.outside_device)

print("Inside: " + str(inside_temp))
print("Outside: " + str(outside_temp))