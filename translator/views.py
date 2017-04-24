from django.shortcuts import render

from .forms import InputForm


def index(request):

    form = InputForm(request.POST or None)
    output_text = ""

    if request.method == 'POST':

        output_text = process(request.POST['input'])

    return render(request, 'translator/index.html', {'form': form, 'output_text': output_text})


def process(original_text):

    new_words = []
    diftongit_capital = []
    add_start = ""
    add_end = ""

    words = original_text.split()

    vokaalit = "aeiouyäö"
    vokaalit += vokaalit.upper()

    konsonantit = "bcdfghjklmnpqrstvxyz"
    konsonantit += konsonantit.upper()

    diftongit = ["ai", "ei", "oi", "äi", "öi", "ey", "äy", "öy", "au", "eu", "ou", "ui", "iy", "iu", "iy", "ie", "uo",
                 "yö"]

    for diftongi in diftongit:
        dif = diftongi.capitalize()
        diftongit_capital.append(dif)
    diftongit += diftongit_capital

    for index, word in enumerate(words):

        for i, letter in enumerate(word):
            if letter not in vokaalit and letter not in konsonantit:
                add_start += letter
            else:
                word = word[i:]
                break

        if len(word) > 2 and word != add_start:

            for i, letter in enumerate(word):
                if letter not in vokaalit and letter not in konsonantit:
                    add_end += letter

            if len(add_end) <= len(word):
                word = word[:len(word)-len(add_end)]

            if word[1] == "n" or word[:2] in diftongit:
                begin = "ko" + word[1:]
                end = word[:1] + "ntti"
            elif word[0] == word[1] and word[0] in vokaalit:
                begin = "koo" + word[2:]
                end = word[:1] + "ntti"
            elif word[1] == word[2] and word[1] in vokaalit:
                begin = "koo" + word[3:]
                end = word[:2] + "ntti"
            elif word[1] == word[2] and word[1] in konsonantit:
                begin = "ko" + word[1:]
                end = word[:1] + "ntti"
            elif word[0] in vokaalit and word[1] in konsonantit and word[2] in vokaalit:
                begin = "ko" + word[1:]
                end = word[:1] + "ntti"

            else:
                begin = "ko" + word[2:]
                end = word[:2] + "ntti"

            if end.istitle():
                begin = begin.capitalize()
                end = end.lower()

            new_word = begin + " " + end

        elif add_start == word:
            add_start = ""
            new_word = word

        else:
            new_word = word

        if add_end != "":
            new_word += add_end
            add_end = ""

        if add_start != "":
            new_word = add_start + new_word
            add_start = ""

        if new_word == "":
            new_word = word

        new_words.append(new_word)

    output = " ".join(new_words)

    return output



