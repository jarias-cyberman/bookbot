import sys
from stats import num_words
from stats import count_characters
from stats import sort_chars


if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

book_path = sys.argv[1]

def get_book_text(Path_to_book_and_file_name):
	with open(Path_to_book_and_file_name) as f:
		file_contents = f.read()
		return file_contents
		
def main():
	whole_text_file = get_book_text(book_path)
	word_count = num_words(whole_text_file)
	cc_dict = count_characters(whole_text_file)
	sc_dict = sort_chars(cc_dict)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")
	print("----------- Word Count ----------")
	print(f"Found {word_count} total words")
	print("--------- Character Count -------")

	for char_dict in sc_dict: # print and remove non alpha characters
		char = char_dict["char"]
		if char.isalpha():
			print(f"{char}: {char_dict['count']}")
	print("============= END ===============")

main()
