const floodFill = (image, sr, sc, newColor) => {
    const initialColor = image[sr][sc];
    dfs(image, sr, sc, newColor, initialColor);
    return image;
}


const dfs = (image, sr, sc, newColor, initialColor) => {
    if (sr < 0 || sr > image.length -1 || sc < 0 || sc > image[0].length -1 || image[sr][sc] != initialColor || image[sr][sc] == newColor) {
        return image;
    }

    image[sr][sc] = newColor;
    dfs(image, sr + 1, sc, newColor, initialColor);
    dfs(image, sr - 1, sc, newColor, initialColor);
    dfs(image, sr, sc + 1, newColor, initialColor);
    dfs(image, sr, sc - 1, newColor, initialColor);
}



console.log(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))