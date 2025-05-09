# Human Prompt for Intent Expansion

The generated prompt in `prompt_fill_batch.txt` was issued to ChatGPT-o3 with each batch of intents to generate some patterns and responses for each intent.

Then the following prompt was given to ChatGPT-4o:

> Now I need a third prompt to expand each batch to increase the number of patterns by 3x and responses by 1.5x

The following long prompt was generated and then given repeatedly to ChatGPT-o3 along with each `intents_##_filled.json` to further expand on the patterns and responses for each intent.

# Generated Prompt

You are provided with a **batch of chatbot intents**.  
Each intent already contains a **moderate number** of patterns (user utterances) and responses (chatbot replies).

---

## 🩺 Your Task:

For each intent:

- **Expand** the number of `patterns` (user utterances) by approximately **3×**.
- **Expand** the number of `responses` (chatbot replies) by approximately **1.5×**.

**DO NOT modify** the `tag`, `context`, or `required_context` fields.  
**DO NOT** remove any existing patterns or responses — **only add** new ones.

---

## 🩺 Style Guidelines:

### Patterns (User Utterances)
- Add **natural and believable variations** of how a visitor or patient might ask the same thing.
- Use a mix of:
  - **Short questions** and **longer full sentences**
  - **Formal** and **casual** phrasing
  - **Native** and **non-native English** styles
- Minor typos, slight awkwardness, and different grammatical structures are acceptable.

### Responses (Chatbot Replies)
- Add **polite, clear, professional** new replies.
- **Moderate variety is sufficient**:
  - Small differences in phrasing, tone, or formality are enough.
  - Full rewording is not required unless natural.
- **Emergency/medical-related intents** must always defer politely to **hospital staff or 911**.

---

## 🩺 Example:

Starting Input:

```json
{
  "tag": "find_pharmacy",
  "patterns": [
    "Where is the pharmacy?",
    "How do I get prescriptions filled?"
  ],
  "responses": [
    "Our hospital pharmacy is on the ground floor next to the atrium—follow the purple ‘Pharmacy’ signs."
  ],
  "context": "",
  "required_context": []
}
```

Expanded Output:

```json
{
  "tag": "find_pharmacy",
  "patterns": [
    "Where is the pharmacy?",
    "How do I get prescriptions filled?",
    "Can you show me where the pharmacy is?",
    "Is there a pharmacy inside the hospital?",
    "Where can I pick up my medicine?",
    "I need to find the hospital drugstore.",
    "Is the pharmacy open now?",
    "Which way is the pharmacy from the entrance?"
  ],
  "responses": [
    "Our hospital pharmacy is on the ground floor next to the atrium—follow the purple ‘Pharmacy’ signs.",
    "You’ll find the pharmacy on Level 0, just beyond the atrium area.",
    "The hospital pharmacy is located on the ground floor near the main elevators."
  ],
  "context": "",
  "required_context": []
}
```

---

## 🩺 Special Instructions:
- **Patterns**: Add **about 3×** more patterns. (Slightly exceeding is fine if natural.)
- **Responses**: Add **about 1.5×** more responses. (Round up if needed.)
- **Preserve** the strict JSON format — no extra or missing fields.
- Do **NOT** invent unrelated topics or new intents.