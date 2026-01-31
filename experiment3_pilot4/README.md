# Experiment 3 Pilot 4: Absent vs Present - Balloon & Drum

## 📋 Overview
This experiment investigates how the victim's presence (absent vs present) affects causal reasoning and emotional attribution in two scenarios: balloon popping and drum breaking.

## 🗂️ Folder Structure

```
experiment3_pilot4/
├── experiment3_absent/         # Condition 1: Victim absent
│   └── images/
│       ├── instructions.png
│       ├── balloon_absent/
│       │   ├── balloon_absent.001.png - .013.png (13 story images)
│       │   ├── balloon_absent_q_pop.png
│       │   ├── balloon_absent_q_cause_pop.png
│       │   ├── balloon_absent_q_sad.png
│       │   └── balloon_absent_q_cause_sad.png
│       └── drum_absent/
│           ├── drum_absent.001.png - .013.png (13 story images)
│           ├── drum_absent_q_break.png
│           ├── drum_absent_q_cause_break.png
│           ├── drum_absent_q_anger.png
│           └── drum_absent_q_cause_anger.png
└── experiment3_present/        # Condition 2: Victim present
    └── images/
        ├── instructions.png
        ├── balloon_present/
        │   ├── balloon_present.001.png - .011.png (11 story images)
        │   ├── balloon_present_q_pop.png
        │   ├── balloon_present_q_cause_pop.png
        │   ├── balloon_present_q_sad.png
        │   └── balloon_present_q_cause_sad.png
        └── drum_present/
            ├── drum_present.001.png - .010.png (10 story images)
            ├── drum_present_q_break.png
            ├── drum_present_q_cause_break.png
            ├── drum_present_q_anger.png
            └── drum_present_q_cause_anger.png
```

## 🎯 Two Conditions

### Condition 1: Absent
- **Folder**: `experiment3_absent/`
- **Condition**: `absent`
- **Stories**: 
  - Balloon: 13 images (victim absent when balloon pops)
  - Drum: 13 images (victim absent when drum breaks)

### Condition 2: Present
- **Folder**: `experiment3_present/`
- **Condition**: `present`
- **Stories**: 
  - Balloon: 11 images (victim present when balloon pops)
  - Drum: 10 images (victim present when drum breaks)

## 📝 Experiment Flow

Each participant goes through:

1. **Consent Form**
2. **Instruction Page** (`instructions.png`)
3. **First Scenario** (balloon or drum, randomized):
   - Story images
   - 4 questions in randomized order
4. **Second Scenario** (balloon or drum, whichever wasn't first):
   - Story images
   - 4 questions in randomized order
5. **Demographics Survey**

## 🔀 Question Randomization (8 Possible Orders per Scenario)

Each scenario has **4 questions** organized in **2 pairs**, with **8 possible orders**:

### Balloon Scenario Questions:
- **Pop pair**: (`cause_pop`, `pop`) - kept together but order randomized
- **Sad pair**: (`cause_sad`, `sad`) - kept together but order randomized
- **Pair order**: The order of these two pairs is also randomized

### Drum Scenario Questions:
- **Break pair**: (`cause_break`, `break`) - kept together but order randomized
- **Anger pair**: (`cause_anger`, `anger`) - kept together but order randomized
- **Pair order**: The order of these two pairs is also randomized

### Randomization Logic:
1. Within each pair, order is randomized (2 possibilities)
2. The order between pairs is randomized (2 possibilities)
3. **Total**: 2 × 2 × 2 = **8 possible question orders per scenario**

### Example Question Orders (Balloon):
1. `cause_pop, pop, cause_sad, sad`
2. `pop, cause_pop, cause_sad, sad`
3. `cause_pop, pop, sad, cause_sad`
4. `pop, cause_pop, sad, cause_sad`
5. `cause_sad, sad, cause_pop, pop`
6. `sad, cause_sad, cause_pop, pop`
7. `cause_sad, sad, pop, cause_pop`
8. `sad, cause_sad, pop, cause_pop`

### Example Question Orders (Drum):
1. `cause_break, break, cause_anger, anger`
2. `break, cause_break, cause_anger, anger`
3. `cause_break, break, anger, cause_anger`
4. `break, cause_break, anger, cause_anger`
5. `cause_anger, anger, cause_break, break`
6. `anger, cause_anger, cause_break, break`
7. `cause_anger, anger, break, cause_break`
8. `anger, cause_anger, break, cause_break`

## 📊 Data Collection

### JSON Structure
```json
{
  "participant_id": "P1737891234567_1234",
  "condition": "absent",
  "scenario_order": ["balloon", "drum"],
  "question_orders": {
    "balloon": ["cause_pop", "pop", "cause_sad", "sad"],
    "drum": ["cause_break", "break", "cause_anger", "anger"]
  },
  "responses": {
    "balloon_pop": "...",
    "balloon_cause_pop": "...",
    "balloon_sad": "...",
    "balloon_cause_sad": "...",
    "drum_break": "...",
    "drum_cause_break": "...",
    "drum_anger": "...",
    "drum_cause_anger": "..."
  },
  "participants": {
    "age": 25,
    "gender": "Female",
    "race": "White",
    "ethnicity": "Non-Hispanic"
  }
}
```

### CSV Columns
- `participant_id`: Unique participant ID
- `condition`: Condition type (absent or present)
- `scenario_order`: Order of scenarios (e.g., "balloon,drum")
- `balloon_question_order`: Question order for balloon scenario
- `drum_question_order`: Question order for drum scenario
- `balloon_pop`, `balloon_cause_pop`, `balloon_sad`, `balloon_cause_sad`: Balloon responses
- `drum_break`, `drum_cause_break`, `drum_anger`, `drum_cause_anger`: Drum responses
- `age`, `race`, `gender`, `ethnicity`: Demographic information

## 🔧 Converting Data

Each experiment folder has a `convert_data_to_csv.py` script. To convert data:

```bash
cd experiment3_absent  # or experiment3_present
python convert_data_to_csv.py
```

This will read `data.json` and create `data.csv` with properly formatted columns.

## 🌐 Deploying to Proliferate

Set up 2 conditions in Proliferate:
1. **Condition 1**: Absent → Link to `experiment3_absent/index.html`
2. **Condition 2**: Present → Link to `experiment3_present/index.html`

Example URLs (adjust based on your GitHub Pages setup):
- Absent: `https://cslouise.github.io/causal_verb_punish/experiment3_pilot4/experiment3_absent`
- Present: `https://cslouise.github.io/causal_verb_punish/experiment3_pilot4/experiment3_present`

Each condition will automatically:
- Show the shared instruction page
- Display balloon and drum stories in randomized order
- Present 4 questions per story in one of 8 randomized orders
- Record scenario order and question orders for both scenarios
- Submit all responses to Proliferate

## ✅ Files in Each Condition Folder

- `index.html` - Main experiment page with randomization logic
- `js/trial.js` - Story images and questions configuration
- `js/consent.js` - Consent form
- `js/demographic_form.js` - Demographics survey
- `js/intro.js` - Introduction (if needed)
- `js/jquery.min.js` - jQuery library
- `js/jquery-ui.min.js` - jQuery UI library
- `convert_data_to_csv.py` - Data conversion script
- `images/` - All images organized by scenario

## 🚀 Testing

Before deploying, test each condition locally:
1. Open `experiment3_[condition]/index.html` in a browser
2. Check console logs for:
   - Scenario order (balloon/drum)
   - Question order for each scenario
3. Verify questions appear in randomized order
4. Confirm data is collected with all order information

## 📈 Data Analysis Tips

When analyzing data:
- Use `scenario_order` to control for scenario presentation order
- Use `balloon_question_order` and `drum_question_order` to control for question order effects
- Compare responses between absent and present conditions
- Analyze:
  - How presence/absence affects causal attributions
  - How presence/absence affects emotional attributions
  - Differences between balloon (sad) and drum (anger) emotions
  - Within-pair order effects

## 🔍 Key Features

✅ **Scenario randomization** - Balloon and drum order is randomized
✅ **Question randomization** - 8 possible orders per scenario
✅ **Paired questions** - Causal and outcome questions kept together
✅ **Order tracking** - Both scenario and question orders recorded
✅ **Text-based responses** - All questions use open-ended text boxes
✅ **Condition tracking** - Each submission includes condition type
✅ **Clean data output** - Automated CSV conversion with all columns

## 🎯 Research Questions

This experiment can help answer:
- Does the victim's presence affect causal attributions?
- Does the victim's presence affect emotional attributions?
- Are there differences in reasoning between balloon (sad) and drum (anger) scenarios?
- How do people reason about who caused the event vs who should feel the emotion?
- Does question order within pairs affect responses?

## 📧 Questions?

Check that:
- All image files exist in correct locations
- Image paths in `trial.js` match actual file names
- Console logs show correct randomization
- Question orders follow the paired pattern
- Data includes both scenario_order and question_orders for both scenarios
