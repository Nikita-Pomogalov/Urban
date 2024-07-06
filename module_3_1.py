calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    count_calls()
    a = (len(string), string.upper(), string.lower())
    return a


def is_contains(string, list_to_search):
    count_calls()
    count = 0
    for word in list_to_search:
        if str(word.casefold()) == str(string.casefold()):
            count += 1
        else:
            count = count
    if count == 0:
        return False
    else:
        return True


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)