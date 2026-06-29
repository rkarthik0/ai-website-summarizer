from dotenv import load_dotenv
from openai import OpenAI
import os
import requests
from bs4 import BeautifulSoup

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


def summarize_website(url):

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception:
        return "Unable to access the website. Please check the URL."

    soup = BeautifulSoup(response.text, "html.parser")

    text = soup.get_text(separator=" ", strip=True)

    text = text[:6000]

    prompt = f"""
 You are an expert AI assistant.

Read the website content carefully.

Generate a professional summary.

Include:

# Website Summary

## Main Purpose

## Key Features

## Important Points

## Conclusion

Keep the summary short, clean and readable.

Website Content:

    {text}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


if __name__ == "__main__":

    website = input("Enter Website URL: ")

    summary = summarize_website(website)

    print("\n")

    print(summary)