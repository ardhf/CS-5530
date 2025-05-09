# Human Prompt for Intent Filling

The generated prompt in `prompt_skeleton.txt` was issued to ChatGPT-o3, and I received skeleton `intents.json` with `tag` and `(required_)context` fields populated, and with `pattern` and `response` fields empty.

I used python to break this apart into batches (using `itertools`).

I then issued the following to ChatGPT-4o to get a prompt to fill out each batch of intent data:

> Now I need a prompt that I can give to an LLM, along with a .json, that will generate patterns and responses. I will give this prompt repeatedly on batches of intents.

The long prompt below was generated, and then given repeatedly to ChatGPT-o3 along with each `intents_##.json` to generate some patterns and responses for each intent.

# Generated Prompt

You are provided a **JSON file** containing a **batch of chatbot intents**.  
Each intent includes:

- `tag`: the name of the intent
- `patterns`: an **empty list** (to be filled)
- `responses`: an **empty list** (to be filled)
- `context`: the conversational context (string; may be empty)
- `required_context`: a list of required prior contexts (may be empty)

---

## 🩺 Your Task:

For each intent:

- Populate the **`patterns`** field with **20 to 50** realistic user utterances.
- Populate the **`responses`** field with **6 to 10** natural, helpful chatbot replies.

**DO NOT modify** the `tag`, `context`, or `required_context` fields.

---

## 🩺 Style Guidelines:

### Patterns (User Utterances)
- Reflect **realistic**, **natural** variations in how users might express the intent.
- Include a mix of:
  - **Formal and informal phrasing**
  - **Native and non-native English speaker patterns**
  - **Varying literacy levels** (simple, polite, casual, slightly awkward)
- Cover different **ways of asking the same thing** (question forms, statements, requests).

### Responses (Chatbot Replies)
- Keep replies **professional, supportive, and clear**.
- **If the topic involves emergencies, medical advice, or urgent needs, politely defer** users to **hospital staff or 911** — do not offer advice.
- Acknowledge when the chatbot is providing **basic information** versus **suggesting human assistance**.
- Responses should match the **context** (for multi-step conversations).
- Vary slightly across responses to avoid sounding robotic.

---

## 🩺 Examples:

Given input:

```json
{
  "tag": "find_cafeteria",
  "patterns": [],
  "responses": [],
  "context": "",
  "required_context": []
}
```

Output:

```json
{
  "tag": "find_cafeteria",
  "patterns": [
    "Where is the cafeteria?",
    "How do I get to the cafeteria?",
    "Is there a place to eat here?",
    "Can you tell me where the cafeteria is located?",
    "Which floor is the cafeteria on?",
    "I'm looking for food. Where should I go?",
    "How far is the cafeteria from here?"
    // (20-50 total)
  ],
  "responses": [
    "The cafeteria is located on the first floor near the main entrance.",
    "You'll find the cafeteria on the first floor. Follow the green signs.",
    "The hospital cafeteria is just past the main lobby on the first floor.",
    "For a meal, head to the cafeteria by the front entrance. Staff can help if you need directions.",
    "You'll find dining options in the cafeteria on the first floor, close to reception."
    // (6-10 total)
  ],
  "context": "",
  "required_context": []
}
```

---

## 🩺 Special Instructions:
- If an intent has a non-empty `required_context`, assume the user is continuing a **multi-turn conversation**.
- For multi-step intents:
  - Patterns should reflect a **follow-up message**, not a brand new conversation.
  - Responses should **move the conversation forward or confirm understanding**.
- **Maintain strict JSON formatting** — no extra fields, no missing fields.