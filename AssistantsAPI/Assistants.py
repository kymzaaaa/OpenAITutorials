import os
from openai import OpenAI

# APIキーの設定（環境変数から取得）
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

# アシスタントの作成
def create_assistant():
    assistant = client.beta.assistants.create(
        name="Math Tutor",
        instructions="You are a personal math tutor. Write and run code to answer math questions.",
        tools=[{"type": "code_interpreter"}],
        model="gpt-4o"
    )
    print(f"✅ Created Assistant: {assistant.id}")
    return assistant.id

# スレッドの作成
def create_thread():
    thread = client.beta.threads.create()
    print(f"✅ Created Thread: {thread.id}")
    return thread.id

# メッセージの追加
def add_message(thread_id, user_input):
    message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=user_input
    )
    print(f"✅ Added Message: {message.id}")

# アシスタントの実行
def run_assistant(thread_id, assistant_id):
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread_id,
        assistant_id=assistant_id
    )
    
    if run.status == "completed":
        messages = client.beta.threads.messages.list(thread_id=thread_id)
        for msg in messages.data[::-1]:  # 最新のメッセージを取得
            print(f"{msg.role} > {msg.content[0].text.value}")
    else:
        print(f"⚠️ Run Status: {run.status}")

# メニュー
def main():
    assistant_id = None
    thread_id = None

    while True:
        print("\n=== OpenAI Assistants API ===")
        print("1: Create Assistant")
        print("2: Create Thread")
        print("3: Add Message")
        print("4: Run Assistant")
        print("5: Exit")
        choice = input("Select an option: ")

        if choice == "1":
            assistant_id = create_assistant()
        elif choice == "2":
            thread_id = create_thread()
        elif choice == "3":
            if not thread_id:
                thread_id = input("Enter Thread ID: ")
            user_input = input("Enter your message: ")
            add_message(thread_id, user_input)
        elif choice == "4":
            if not thread_id:
                thread_id = input("Enter Thread ID: ")
            if not assistant_id:
                assistant_id = input("Enter Assistant ID: ")
            run_assistant(thread_id, assistant_id)
        elif choice == "5":
            print("🔄 Exiting program.")
            break
        else:
            print("⚠️ Invalid choice, try again.")

if __name__ == "__main__":
    main()
