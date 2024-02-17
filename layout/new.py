images = [{'name': 'frame_0010.png', 'rank': 3, 'span': 'column'}, {'name': 'frame_0011.png', 'rank': 1, 'span': 'column'}, {'name': 'frame_0012.png', 'rank': 3, 'span': 'column'}, {'name': 'frame_0013.png', 'rank': 2, 'span': 'row'}, {'name': 'frame_0014.png', 'rank': 1, 'span': 'row'}, {'name': 'frame_0015.png', 'rank': 3, 'span': 'column'}]


for image in images:
    print(f"{image['span']} : {image['rank']}")


grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

# for i in range(3):
#     if(images[i]['span'] == 'row'):
#         j=0
#         while(j<images[i]['rank'] ):
#             grid[i][j] = 1
#             j=j+1

#     if(images[i]['span'] == 'column'):
#         j=0
#         while(j<images[i]['rank'] ):
#             grid[j][i] = 1
#             j=j+1

i = 0
start = {'r': 0 , 'c': 0}

r=0
c=0



try:



    while(i<6):

        print(start)

        if(images[i]['span'] == 'column'):
            if(images[i]['rank'] + c  > 4):
                r = r + 1
                c=0
                if(r>2):
                    break

            j=0
            while(j<images[i]['rank'] ):
                grid[r][c] = images[i]['rank']
                c=c+1
                j=j+1
                
            start['r'] = r
            start['c'] = c




        if(images[i]['span'] == 'row'):
            if(images[i]['rank'] + r  > 3):
                r = r + 1
                c=0
                if(c>3):
                    break


            j=0
            while(j<images[i]['rank'] ):
                grid[r][c] = images[i]['rank']
                r=r+1
                j=j+1

            r = start['r']
            c= start['c']


        i=i+1

except:
    print(f"r : {r} c: {c}")
    print(grid)



for row in grid:
    print(*row, sep=" ")

