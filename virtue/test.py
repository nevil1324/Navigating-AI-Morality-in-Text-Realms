from googletrans import Translator
import time

def translate_text(text, target_language='hi'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

def translate_large_dataset(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        english_text = f.read().splitlines()

    translated_text = []
    translator = Translator()

    for i, text in enumerate(english_text):
        try:
            translation = translator.translate(text, dest='hi')
            translated_text.append(translation.text)
            print(f"Translated {i+1} out of {len(english_text)} lines.")
            # Sleep for a short duration to avoid rate limiting
            time.sleep(0.1)
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            continue

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(translated_text))

if __name__ == "__main__":
    input_file = "util_test_hard_hindi.csv"  # Provide the path to your English dataset file
    output_file = "output_dataset_hindi.txt"  # Output file path for the translated dataset
    translate_large_dataset(input_file, output_file)
