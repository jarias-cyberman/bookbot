
def num_words(file_text):
	return len(file_text.split())

def count_characters(file_text):
	chars_dict = {}
	file_text = file_text.lower()
	for char in file_text:
		if char in chars_dict:    # is char in dictionary?
			chars_dict[char] += 1   # yes, increase count by one
		else:
			chars_dict[char] = 1    # Count starts with 1
	return chars_dict

def sort_on(dict):
    return dict["count"]

def sort_chars(char_counts):
    # Create a list of dictionaries using list comprehension
    chars_list = [{"char": char, "count": count} for char, count in char_counts.items()]
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list	
		
