import pyttsx3


e = pyttsx3.init() # object creation


print(   e.getProperty('rate')   )
print(   e.getProperty('volume')   )
print(   e.getProperty('voices')   )  # return a list [ obj1, obj2 ]

voices_List = e.getProperty('voices')

e.setProperty('rate', 250)
e.setProperty( 'volume', 1 )  # min 0 or max 1
e.setProperty('voice', voices_List[ 0 ].id )   # min 0 or max 1


pyttsx3.speak("""

letting the words fly like smoke uncurling from our mouths
we lie in bed with dykes ten years our junior, make
pot heaps to share, sleep in the same flannel sheets,
plot colored artist collaborations underground and not top 40,
draw the constellations from our lovers to each other,
worry language and tease interstitials at our debuts
fighting dotage, we pledge hot-age and buy expensive Italian
boots from Russian women in the village, study our gray hairs

""")
