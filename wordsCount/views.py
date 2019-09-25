from django.shortcuts import render
import operator


def home(request):
    """Funtion to return home page."""

    return render(request, 'home.html')


def count(request):
    """Function to process the count page.

    Get the text to be processed and return count page.
    """

    # Get user text into variable text
    text = request.GET['user_text']

    # Clean text
    bad_chars = [';', '.', '-', ',', '#', '_', ':', '(', ')']
    clean_text = ''.join(i for i in text if not i in bad_chars)

    # Create list with lower case and remove blank space
    word_list = clean_text.lower().split()

    # Loop into the list to count each words
    word_dict = {}

    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    sorted_list = sorted(
        word_dict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'tag_text': text, 'count': len(word_list), 'each_word': sorted_list})
