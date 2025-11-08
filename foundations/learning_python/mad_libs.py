# a mini-project: Mad Libs Game
def get_words():
    place = input("Enter place: ") #a place name
    adj = input("Enter adjective: ") #describing word like "funny" or "pink"
    noun = input("Enter noun: ") #a person, place or thing 
    verb = input("Enter verb: ") # action word like "run", "swim"
    adj2 = input("Enter another adjective: ") # another describing word
    emotion = input("Enter feelings: ") # a feeling like "happy", "blessed"
    verb2 = input("Enter another verb: ") # another action word
    fr = input("Enter persons name: ") # a persons name
    
    return place, adj, noun, verb, adj2, emotion, verb2, fr

def create_story(place, adj, noun, verb, adj2, emotion, verb2, fr):
    story = f"Today I went to the {place}. I saw {adj} {noun} {verb}ing happily. It was a very {adj2} day, and I felt {emotion}. Then, I decided to {verb2} with my friend {fr}. We had so much fun!"
    print(story)

#main Program
words = get_words()
create_story(*words)