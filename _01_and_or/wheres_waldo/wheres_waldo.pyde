"""

# =========== SOUND =================
# Some computers are unable to play sounds. 
# If you cannot play sound on this computer, set canPlaySounds to false.
# If you are not sure, ask your teacher 
can_play_sounds = False

def setup():
    # Find a Where's Waldo picture and drop it onto the sketch.
    
    # Change the line below to match your file name.
    waldo = loadImage("waldo2.png")
    
    # Use the size() function to set the width and height of your sketch
    size(500,500)
    # Resize your waldo picture to the same size as the sketch
    waldo.resize(500,500)
    # Use the background() function to make the waldo image your
    # sketch background
    background(waldo)
    
def draw():
   
    # If the user presses the mouse...
    # *Hint* use the mousePressed variable
    if mousePressed and mouseX == 430 and mouseY == 124:
        # Use this print statement to help you find the location
        # of Waldo to use in the code below
        text("Waldo found!", mouseX, mouseY)
        # Check if the location of the mouse is anywhere on the image of Waldo.
        # If it is, print “Waldo found!”  Use the text() command to write it
        # on the sketch.
          
            # Use the play_woohoo() method below.
        play_woohoo()
        # However, if the mouse is not on Waldo, print "Not here!" 
        # Use the text() command to write it on the sketch.
    elif mousePressed:
        text("Not here!", mouseX, mouseY)
            # Use the play_doh() method below.
        play_doh()

    pass    

# =================== This code is needed to play sounds. ===================
woohoo = None
doh = None

if can_play_sounds:
    add_library('sound')

def play_woohoo():
    global woohoo
    if can_play_sounds:
        if woohoo is None:
            woohoo = SoundFile(this, "homer-woohoo.wav")
        woohoo.stop()
        woohoo.play()

def play_doh():
    global doh
    if can_play_sounds:
        if doh is None:
            doh = SoundFile(this, "homer-doh.wav") 
        doh.stop()
        doh.play()
