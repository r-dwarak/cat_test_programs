class WordShuffler:
    def __init__(self):
        pass

    def shuffle_words(self, sentence):
        """
        Shuffle the words in a sentence such that odd-positioned words appear first,
        followed by even-positioned words.

        Args:
        sentence (str): Input sentence

        Returns:
        str: Generated string with shuffled words
        """
        words = sentence.split()
        odd_words = [words[i] for i in range(len(words)) if i % 2 == 0]
        even_words = [words[i] for i in range(len(words)) if i % 2 != 0]
        generated_string = ' '.join(odd_words + even_words)
        return generated_string

    def run(self):
        try:
            while True:
                # Input: Read the input sentence or "exit" to quit
                sentence = input("Enter the input sentence (type 'exit' to quit): ")

                if sentence.lower() == 'exit':
                    print("Exiting the program...")
                    break

                # Call the shuffle_words method to generate the shuffled string
                output_sent = self.shuffle_words(sentence)

                # Output the generated string
                print("Generated String:", output_sent)
        except Exception as e:
            print("An error occurred:", str(e))


if __name__ == "__main__":
    # Create an instance of the WordShuffler class and run the program
    word_shuffler = WordShuffler()
    word_shuffler.run()
