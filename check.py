import os
from dotenv import load_dotenv
load_dotenv()
key = os.environ.get("ANTHROPIC_API_KEY", "없음")
print(f"키 앞부분: {key[:12]} / 길이: {len(key)}")