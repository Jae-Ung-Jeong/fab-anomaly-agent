import anthropic 
from dotenv import load_dotenv

load_dotenv()  # .env에서 ANTHROPIC_API_KEY를 읽어옴

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=500,
    messages=[
        {"role": "user", "content": "반도체 공정에서 이상 탐지가 왜 어려운지 한 문장으로 설명해줘."}
    ],
)

for block in message.content:
    if block.type == "text":
        print(block.text)