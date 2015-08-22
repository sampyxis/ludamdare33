# Note used yet


def createLevel():
    startx=80   # map width
    starty=60  # map height
    themap= dMap()
    themap.makeMap(startx,starty,11,50,60)
    for y in range(starty):
            line = ""
            for x in range(startx):
                    block = Block(BLUE)
                    block_black = Block(BLACK)
                    if themap.mapArr[y][x]==0:
                            line += "."
                            block_black.rect.x = x * 20
                            block_black.rect.y = y * 20
                            block_list.add(block_black)
                            all_sprites_list.add(block_black)
                    if themap.mapArr[y][x]==1:
                            line += " "
                    if themap.mapArr[y][x]==2:
                        #block.rect = themap.mapArr[y][x]
                        block.rect.x = x * 20
                        block.rect.y = y * 20
                        #print('x: ', x, 'y: ', y)
                        block_list.add(block)
                        all_sprites_list.add(block)
                        line += "#"
                    if themap.mapArr[y][x]==3 or themap.mapArr[y][x]==4 or themap.mapArr[y][x]==5:
                            line += "="


            #print('add in list')
            print(line)
