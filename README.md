# Overfitted
## Visual explanation
![alt text is for plebs](https://github.com/corollari/overfitted/raw/master/overfitted.jpg)
## Pls xplain
Encoding images in neural nets 101:
1. Decode an image into a matrix of RGB values so that `image[x][y]={red:RR, green:GG, blue:BB}`.
2. Train a neural net to predict the pixel colors (`{red:RR, green:GG, blue:BB}`) when given the pixel location (`(x, y)`)
3. Overfit that neural network to the extreme
4. Encode and compress the weights of the trained nnet in a file
5. That file is your compressed image, now you can decompress it by building the nnet using the specified weights and making it predict all the pixel values
6. Enjoy your compressed image, now you're above those plebs who use jpeg to compress their image in seconds, it's way better take several hours to do it.

### B.. but this is useless as this algorithm takes a ton of time to compress a single picture
You're right.

### Then why did you create this?
It's art, it doesn't need a reason to exist.

jk, I'm just a masochist.
