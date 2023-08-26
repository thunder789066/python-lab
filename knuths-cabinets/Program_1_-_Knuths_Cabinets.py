##CS 101
##Program 1
##Christina Gerstner
##clgdtf@mail.umkc.edu
##
##Problem: The Knuth Cabinet Company keeps track of labor for cutting, sanding and finishing their
##  different types of cabinets. They have 3 types of cabinets; upper, lower and corner.You’ve been
##  asked to write them a Python program that gets the number of upper, lower, and corner cabinets
##  from the user, then computes the cutting, sanding, finishing and total hours.
##
##ALGORITHM:
##      1. Get user input for Upper, Lower, & Corner cabinets.
##      2. Make Dictionary/List to store hour values specified to which cabinet to either cutting,
##          sanding, or finishing labor hours
##      3. Calculate equation muliplying user input to corresponding values from each cabinet dictionary
##      4. add & total up hours for each labor as well as grand total
##      5. print output for all hours -> cutting, sanding, finishing, & grand total
##
##ERROR HANDLING: Generate up to ten errors & explain why they happened.
##
##OTHER COMMENTS: Most errors were intentional. Equation used from pseudo code in comment
##  line above equation.
#####################################################################################################
upperCabinetNum = int(input('Enter the number of upper cabinets: '))
lowerCabinetNum = int(input('Enter the number of lower cabinets: '))
cornerCabinetNum = int(input('Enter the number of corner cabinets: '))

uppercabinet = {
        'Cutting Labor': 1.2,
        'Sanding Labor': 2.4,
        'Finishing Labor': 3.4
    }

lowercabinet = {
        'Cutting Labor': 1.5,
        'Sanding Labor': 1.8,
        'Finishing Labor': 2.5
    }

cornercabinet = {
        'Cutting Labor': 1.9,
        'Sanding Labor': 1.2,
        'Finishing Labor': 1.5
    }

# total cutting hrs = (upper[cutting]*userUpper) + (lower[cutting]*userLower) + (corner[cutting]*usercorner)
totalCuttingHrs = (uppercabinet['Cutting Labor'] * upperCabinetNum) + (lowercabinet['Cutting Labor'] * lowerCabinetNum) + (cornercabinet['Cutting Labor'] * cornerCabinetNum)

# total sanding hrs = (upper[sanding]*userUpper) + (lower[sanding]*userLower) + (corner[sanding]*usercorner)
totalSandingHrs = (uppercabinet['Sanding Labor'] * upperCabinetNum) + (lowercabinet['Sanding Labor'] * lowerCabinetNum) + (cornercabinet['Sanding Labor'] * cornerCabinetNum)

# total finishing hrs = (upper[corner]*userUpper) + (lower[corner]*userLower) + (corner[corner]*usercorner)
totalFinishingHrs = (uppercabinet['Finishing Labor'] * upperCabinetNum) + (lowercabinet['Finishing Labor'] * lowerCabinetNum) + (cornercabinet['Finishing Labor'] * cornerCabinetNum)

# total labor hrs = cutting + sanding + finishing
totalLaborHrs = totalCuttingHrs + totalSandingHrs + totalFinishingHrs

print('\nTotal cutting hours', totalCuttingHrs)
print('Total sanding hours', totalSandingHrs)
print('Total finishing hours', totalFinishingHrs)
print('Total labor hours', totalLaborHrs)
