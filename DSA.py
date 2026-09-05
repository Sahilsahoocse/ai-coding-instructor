from google import genai

API_KEY = "AQ.Ab8RN6IOGvNFIK6U7oLBG8V6Q0U6cUI2f_OZyfu_u_lJZlB6Ig"
client = genai.Client(api_key=API_KEY)

SYSTEM_PROMPT = """
You are a Data Structures and Algorithms Instructor.

Rules:
- Answer only DSA-related questions politely and simply.
- If the question is not related to DSA, reply rudely.
"""

print("="*50)
print("📘 DSA AI Tutor (Python)")
print("Type 'exit' to quit.")
print("="*50)

while True:
    query = input("tell me about  array ")
    if query.lower() == "exit":
        break

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=query,
        config={"system_instruction": SYSTEM_PROMPT},
    )

    print("\nTutor:", response.text)
