  
# Python3 program to find  
# hamming distance b/w two  
# string  
  
# Function to calculate 
# Hamming distance  
def hammingDist(str1, str2): 
    i = 0
    count = 0
  
    while(i < len(str1)): 
        if(str1[i] != str2[i]): 
            count += 1
        i += 1
    return count


templates = ['444444','14124114','312341' , '4432111' , '21411241' , '324114' , '13411141' , '12411131' ,'132113', '131423' , 
 '142344' , '234241','2411413','3141214','42111131']

# templates = ['14124114' ,'24123114', '444444', '111111111111']

# input = '44444414442412311452121212124461654897897441651616516848948964'

input =  "141241142411413"

start = 0
end = 0

while(start<len(input)):
    print(f"strat: {start}")
    result = []
    print(input)
    for template in templates:

        temp = input[start:start + len(template)]
        print(f"start: {start} len:{len(template)} temp:{temp}" )
        result.append(hammingDist(temp,template))

    print(result)
    print(min(result))
    print(templates[result.index(min(result))])

    start = start + len(templates[result.index(min(result))]) 

    print("****************")

# print(result)

# # while(start<len(input)):

# result = []

# for template in templates:

#     i = 0
#     while(i<len(input)):
#         temp = input[start:i]
#         if(len(template) == len(temp)):
#             result.append(hammingDist(template,temp))


#     i=i+1        


# end = len(template)






















