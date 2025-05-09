# Human Prompt for Intent Skeleton

ChatGPT-4o was asked to make a skeleton `intents.json` with many intents, used the `intents.json` given by professor as an example.

> I'm making a public-facing chatbot for a nurse's station, which is intended to help patients and visitors find information and resources. I need an LLM to generate a dataset to train the chatbot. I will give you an intents.json as an example of the format for the dataset. Help me construct a prompt, which will instruct the LLM to create to create single- and multi-step intents for this purpose.

A prompt was generated, which is not shown here, then I issued this follow-up prompt:

> We will approach this in steps. First, I need a prompt for a .json with "tag", "context", and "required_context" fields populated, but with "pattern" and "response" fields empty. (This means we need to add "required_context").

The long prompt below was generated, then fed to ChatGPT-o3.

Note that I add a `required_context` field, which we ultimately remove later.

# Generated Prompt

You are tasked with generating a **JSON skeleton dataset** for training a **public-facing hospital nurse’s station chatbot**.

This JSON should contain **intents** formatted with these fields:

- `tag`: a short, descriptive name for the intent
- `patterns`: an **empty list** (`[]`) for now
- `responses`: an **empty list** (`[]`) for now
- `context`: a label for the conversation context (string). If the intent is simple (single-turn), set `context` to an empty string (`""`).
- `required_context`: a list of required prior contexts that must be active for the intent to apply. If no context is required, set as an empty list (`[]`).

---

## 🩺 Intent Types to Create:
Generate both:
- **Single-Step Intents** (basic Q&A, no special context required)
- **Multi-Step Intents** (where a clarifying or follow-up question will be needed)

Multi-Step Intents **must**:
- Have a non-empty `context` label (e.g., `"scheduling_followup"`)
- Specify the `required_context` needed to trigger them (e.g., `["scheduling"]`)

---

## 🩺 Topic Categories to Cover:
- **Finding Departments and Services**: directions to ICU, cafeteria, radiology, etc.
- **Hospital Logistics**: visiting hours, parking, wheelchair access
- **Help Requests**: lost and found, interpreter services
- **Appointments and Scheduling**: follow-up scheduling, rescheduling
- **Contacting Staff**: paging nurses, speaking with doctors
- **Emergencies**: deferring to live staff or 911

---

## 🩺 Format Example:

```json
{
  "intents": [
    {
      "tag": "find_icu",
      "patterns": [],
      "responses": [],
      "context": "",
      "required_context": []
    },
    {
      "tag": "schedule_followup_start",
      "patterns": [],
      "responses": [],
      "context": "scheduling_followup",
      "required_context": []
    },
    {
      "tag": "provide_department_for_followup",
      "patterns": [],
      "responses": [],
      "context": "",
      "required_context": ["scheduling_followup"]
    }
  ]
}
```

---

## 🩺 Special Instructions:
- Use **clear, descriptive** `tag` names (e.g., `"find_cafeteria"`, `"lost_item_report"`, `"request_interpreter"`).
- Assign **context** and **required_context** thoughtfully:
  - **Single-turn intents**: empty `context`, empty `required_context`
  - **First step of a multi-turn flow**: non-empty `context`, empty `required_context`
  - **Follow-up intents**: empty `context`, `required_context` pointing to the previous context.
- Do **NOT** generate patterns or responses yet — leave those fields empty.