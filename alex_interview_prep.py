# # Generate a random 1000 digit number
import random

def generate_thousand_digit_number():

    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    final_number = random.choice(digits[:-1])

    for num in range(999):
        random_digit = random.choice(digits)
        final_number += random_digit

    return int(final_number)

print generate_thousand_digit_number()


number = 6683495648732003307321070455380786072989993695145558781983265053039336977235349604650292313757117111834259314068061730757935817731792472028709260862506293354287510525429959150627118410220567966040759068557186923710070924407262902919546058205804241147521232237975031605865540388135213482944664824959208962090654375658569787336020146963365912445190590267553078272838504799976956835615564399195029145520009702825167407941715742302307654111785835626802815052882381401612610728368857693150660818952267510072037408462720256416299491631026567515603440974708045421707512884950152198200272268114714693893943677328124508377506065013073784400143306510710412804833585359596341443499948005947904939493210183595211949022966067177393698791098287922837617352305129152357787620239291985062878705107890905523067995652318724307378010374159227331254519592844493413567180524581028065294651401450797154808442201332638600570962000520360333543206974244836575513988603367835416123317113107838367879302365159828676891178191882

# # Greatest product of four adjacent numbers in the given number

# # Define the function
# # Max product variable
# # Loop through the digits of the number
# # Check the product of the four adjacent digits against max number
# # If larger, replace max, otherwise continue
# # Return max_product

def find_greatest_product(num):
    max_product = 0
    num = str(num)

    for i in range(len(num)-3):
        product = int(num[i]) * int(num[i+1]) * int(num[i+2]) * int(num[i+3])
        if product > max_product:
            max_product = product

    return max_product

print find_greatest_product(number)


names = [[0, 'jim'], [1, 'zed'], [2, 'bob'], [3, 'nick'], [4, 'barb']]

# Make a list of the second items 
# Sort that list
# Make a new list of the sorted items 

def sort_array_of_arrays(lst):
    second_items_in_lists = []
    for a in lst:
        second_items_in_lists.append(a[1])

    second_items_in_lists.sort()

    sorted_array = []

    for item in second_items_in_lists:
        for array in lst:
            if item in array:
                sorted_array.append(array)

    return sorted_array

print sort_array_of_arrays(names)


