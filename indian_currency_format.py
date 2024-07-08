def format_indian_currency(number):
    
    whole, fraction = str(number).split('.')
    

    if len(whole) > 3:

        last_three = whole[-3:]

        rest = whole[:-3]
 
        rest = rest[::-1]
        rest_with_commas = ','.join([rest[i:i+2] for i in range(0, len(rest), 2)])
        rest_with_commas = rest_with_commas[::-1]
     
        whole = rest_with_commas + ',' + last_three

    formatted_number = whole + '.' + fraction
    
    return formatted_number


number = 123456.7891
formatted_number = format_indian_currency(number)
print(formatted_number)  
