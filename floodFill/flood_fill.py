def floodFill(image, sr, sc, color):
    initial_color = image[sr][sc]
    fill(image, sr, sc, color, initial_color)

    return image

def fill(image, sr, sc, color, initial_color):
    if sr < 0 or sr > len(image) -1 or sc < 0 or sc > len(image[0]) -1 or image[sr][sc] != initial_color or image[sr][sc] == color:
        return
    
    image[sr][sc] = color

    fill(image, sr + 1, sc, color, initial_color)
    fill(image, sr - 1, sc, color, initial_color)
    fill(image, sr, sc + 1 , color, initial_color)
    fill(image, sr, sc - 1, color, initial_color)


print(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))


