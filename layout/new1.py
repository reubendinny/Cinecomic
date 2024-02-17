types = {
    '1' : {
        'x' : 1,
        'y' : 1 
    },
    '2' : {
        'x' : 1,
        'y' : 2 
    },
    '3' : {
        'x' : 3,
        'y' : 1 
    },
    '4' : {
        'x' : 2,
        'y' : 1
    }
    
}

rows = [1,1,1]
cols = [1,1,1,1]

inputs = '14124114'

c_r = 0
c_c = 0

for i in inputs:
    for x in rows:
        if(x>4):
            continue
        if x + types[i]['x'] < 5:
            y = cols.index(min(cols)) - 1
            if y + types[i]['y'] < 4 :
                place(i)
                
                rows[x] += types[i]['x']
                col[y] += types[i]['y']
                res = list(map(lambda x: x + types[i]['x'], rows[x:x+type]))
        

        

