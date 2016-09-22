#30 ml	1 fluid oz.
#100 ml	3.4 fluid oz.


def convert(ml):

    fluid = round((float(ml) * 0.033814), 1)

    return fluid






print("This program is made to convert milliliter to fluid ounces.\n")

milliliter = raw_input("How many milliliters do you want to convert?\n")

measure = convert(milliliter)

print(milliliter + " millilter is equal to " + str(measure) + " fluid ounces")
