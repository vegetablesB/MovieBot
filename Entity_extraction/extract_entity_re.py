import re
def find_name(message):
    name = None
    # Create a pattern for checking if the keywords occur
    name_keyword = re.compile("name|call")
    # Create a pattern for finding capitalized words
    name_pattern = re.compile("called [A-Z]\S*")
    if name_keyword.search(message):
        # Get the matching words in the string
        name_words = name_pattern.findall(message)
        if len(name_words) > 0:
            # Return the name if the keywords are present
            name = ' '.join(name_words)
    print(name)


# Send messages
find_name("show me the movie called TheGodfather in the 2222")
find_name("show me the movie called CatchMeIfYouCan")
find_name("people call me Cassandra ")