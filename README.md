# echo_bott_Handler
Python Telegram Bot Homework
Updater & MessageHandler Basics
Prerequisites: You should be familiar with:
- Creating a bot using Updater
- Using MessageHandler with various filters
- Basic message handling in python-telegram-bot
Task 1: Echo Bot with Text Filters
Difficulty: Easy
Create a Telegram bot that:
- Responds to any text message by echoing it back to the user
- If the message contains the word "hello" (case-insensitive), respond with "Hello! How
can I help you today?"
- If the message contains the word "bye" (case-insensitive), respond with "Goodbye! Have
a great day!"
- For all other text messages, simply echo the message back
Requirements:
- Use Filters.text for the main handler
- Use Filters.regex() for detecting specific words
- Handle at least 3 different MessageHandlers
Example interaction:
User: hello there
Bot: Hello! How can I help you today?
User: How are you?
Bot: How are you?
User: bye for now
Bot: Goodbye! Have a great day!
Task 2: Photo & Sticker Counter
Difficulty: Easy-Medium
Create a bot that tracks and counts different types of media sent by users:
- Count how many photos a user has sent
- Count how many stickers a user has sent
- When user sends a photo, respond with: "Photo received! Total photos: X"
- When user sends a sticker, respond with: "Nice sticker! Total stickers: X"
- Add a command /stats that shows total counts for both media types
Requirements:
- Use Filters.photo for photo messages
- Use Filters.sticker for sticker messages
- Store counts in a dictionary (can be in-memory, doesn't need persistence)
- Use separate MessageHandlers for each media type
Task 3: Smart Text Processor
Difficulty: Medium
Create a bot that processes text in different ways based on user commands:
- If message starts with "UPPER:", convert the rest to uppercase
- If message starts with "LOWER:", convert the rest to lowercase
- If message starts with "COUNT:", count and return the number of words
- If message starts with "REVERSE:", reverse the text
- For any other message, respond with a help message explaining available commands
Requirements:
- Use Filters.regex() to detect command patterns
- Create separate handlers for each command type
- Handle edge cases (empty text after command)
Example interaction:
User: UPPER:hello world
Bot: HELLO WORLD
User: COUNT:The quick brown fox
Bot: Word count: 4
User: REVERSE:Python is awesome
Bot: emosewa si nohtyP
Task 4: Document & File Manager
Difficulty: Medium
Create a bot that handles different types of files:
- Accept document files (.pdf, .txt, .doc) and respond with file name and size
- Accept audio files and respond with duration (if available)
- Accept video files and respond with "Video received! Please wait for processing..." then
send back the video file ID
- Reject all other file types with appropriate message
Requirements:
- Use Filters.document for document handling
- Use Filters.audio for audio files
- Use Filters.video for video files
- Extract and display relevant metadata (file_name, file_size, duration)
- Use proper message formatting
Task 5: Mini Quiz Bot (Combined Project)
Difficulty: Medium-Hard
Create a quiz bot that combines multiple MessageHandler filters:
- Start quiz with a text message containing "start quiz"
- Ask 3 multiple-choice questions (use text messages)
- Accept text answers (A, B, C, or D)
- After each answer, confirm receipt and ask next question
- At the end, calculate and display the score
- If user sends a photo or sticker during quiz, respond: "Please focus on the quiz!"
- If user sends unrelated text during quiz, remind them to answer with A, B, C, or D
Requirements:
- Use Filters.text with Filters.regex() for answer validation
- Use Filters.photo and Filters.sticker to handle distractions
- Track quiz state (can use global variable or dictionary)
- Handle case-insensitive answers
- Provide feedback after quiz completion
Example Quiz Questions:
1. What is the capital of France? (A) London (B) Paris (C) Berlin (D) Madrid
2. Which planet is known as the Red Planet? (A) Venus (B) Mars (C) Jupiter (D) Saturn
3. What is 5 + 7? (A) 10 (B) 11 (C) 12 (D) 13
Bonus Challenge: Add a /reset command to restart the quiz at any time.
Submission Guidelines
For each task, ensure your code includes:
1. Proper bot token handling (use environment variables or config file)
2. Error handling for edge cases
3. Clear comments explaining your logic
4. The updater.idle() call to keep bot running
Grading Criteria
- Functionality (40%): Does the bot work as described?
- Code Quality (30%): Is the code clean, readable, and well-organized?
- Filter Usage (20%): Proper use of MessageHandler filters
- Error Handling (10%): Handles edge cases gracefully
Helpful Resources
- python-telegram-bot documentation: https://docs.python-telegram-bot.org/
- Filters documentation: Look up telegram.ext.Filters
- MessageHandler documentation: Check telegram.ext.MessageHandler
Good luck and happy coding! 🤖🐍