from transformers import pipeline

def summarize_text(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def main():
    print("Tiny AI Text Summarizer!")
    print("Paste any article or paragraph below :\n")

    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    text = " ".join(lines)

    print("\n Summarizing your text...\n")
    result = summarize_text(text)
    print("Summary:\n", result)

if __name__ == "__main__":
    main()