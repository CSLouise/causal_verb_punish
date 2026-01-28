# Experiment 3 Pilot 2: Absent vs Present - 2 Conditions

## 📋 Overview
This experiment investigates how Bobby's presence affects causal reasoning about a tower breaking. The study has 2 conditions:
- **Absent**: Bobby is absent when the tower breaks
- **Present**: Bobby is present when the tower breaks

## 🗂️ Folder Structure

```
experiment3_pilot2/
├── experiment3_absent/         # Condition 1: Bobby absent
│   └── images/
│       ├── instruction.png
│       ├── absent.001.png - .013.png (13 story images)
│       ├── q_break.png
│       ├── q_cause_break.png
│       ├── q_anger.png
│       └── q_cause_anger.png
└── experiment3_present/        # Condition 2: Bobby present
    └── images/
        ├── instruction.png
        ├── present.001.png - .010.png (10 story images)
        ├── q_break.png
        ├── q_cause_break.png
        ├── q_anger.png
        └── q_cause_anger.png
```

## 🎯 Two Conditions

### Condition 1: Absent
- **Folder**: `experiment3_absent/`
- **Condition**: `absent`
- **Story**: Bobby is absent when the tower breaks
- **Story Images**: 13 images

### Condition 2: Present
- **Folder**: `experiment3_present/`
- **Condition**: `present`
- **Story**: Bobby is present when the tower breaks
- **Story Images**: 10 images

## 📝 Experiment Flow

Each participant goes through:

1. **Consent Form**
2. **Instruction Page** (`instruction.png`)
3. **Main Story** (condition-specific images: 10 or 13 images)
4. **Four Questions** (in randomized order, answered in text boxes):
   - **Break question** (`q_break.png`)
   - **Break cause question** (`q_cause_break.png`)
   - **Anger question** (`q_anger.png`)
   - **Anger cause question** (`q_cause_anger.png`)
5. **Demographics Survey**

## 🔀 Question Randomization (8 Possible Orders)

The 4 questions are randomized following these rules:
1. **Break pair** (`cause_break` and `break`) are kept together but their order is randomized (2 possibilities)
2. **Anger pair** (`cause_anger` and `anger`) are kept together but their order is randomized (2 possibilities)
3. The **order of the two pairs** (break vs anger) is also randomized (2 possibilities)

**Total**: 2 × 2 × 2 = **8 possible question orders**

### Example Question Orders:
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
  "question_order": ["cause_break", "break", "cause_anger", "anger"],
  "responses": {
    "break": "...",
    "cause_break": "...",
    "anger": "...",
    "cause_anger": "..."
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
- `question_order`: Order in which questions were presented (e.g., "cause_break,break,cause_anger,anger")
- `break`: Response to break question
- `cause_break`: Response to break cause question
- `anger`: Response to anger question
- `cause_anger`: Response to anger cause question
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
- Absent: `https://cslouise.github.io/causal_verb_punish/experiment3_pilot2/experiment3_absent`
- Present: `https://cslouise.github.io/causal_verb_punish/experiment3_pilot2/experiment3_present`

Each condition will automatically:
- Show the instruction page
- Display the condition-specific story
- Present 4 questions in one of 8 randomized orders
- Record the question order and all responses
- Submit to Proliferate

## ✅ Files in Each Condition Folder

- `index.html` - Main experiment page with randomization logic
- `js/trial.js` - Story images and questions configuration
- `js/consent.js` - Consent form
- `js/demographic_form.js` - Demographics survey
- `js/intro.js` - Introduction (if needed)
- `js/jquery.min.js` - jQuery library
- `js/jquery-ui.min.js` - jQuery UI library
- `convert_data_to_csv.py` - Data conversion script
- `images/` - Condition-specific images
  - `instruction.png`
  - Story images (10-13 images)
  - 4 question images

## 🎨 Image Organization

### Experiment 3 Absent (in `experiment3_absent/images/`):
- `instruction.png` - Instruction page
- `absent.001.png` to `.013.png` - Story (13 images)
- `q_break.png` - Break question
- `q_cause_break.png` - Break cause question
- `q_anger.png` - Anger question
- `q_cause_anger.png` - Anger cause question

### Experiment 3 Present (in `experiment3_present/images/`):
- `instruction.png` - Instruction page
- `present.001.png` to `.010.png` - Story (10 images)
- `q_break.png` - Break question
- `q_cause_break.png` - Break cause question
- `q_anger.png` - Anger question
- `q_cause_anger.png` - Anger cause question

## 🚀 Testing

Before deploying, test each condition locally:
1. Open `experiment3_[condition]/index.html` in a browser
2. Go through the entire flow
3. Check that instruction page shows
4. Verify questions appear in randomized order
5. Check console for question order logged
6. Verify data is collected correctly with question order

## 📈 Data Analysis Tips

When analyzing data:
- Use the `question_order` column to control for question order effects
- Compare responses between absent and present conditions
- Analyze break vs anger attributions
- Consider how Bobby's presence/absence affects responses

## 🔍 Key Features

✅ **Simple design** - Each condition has its own instruction and story
✅ **Question randomization** - 8 possible orders to control for order effects
✅ **Order tracking** - Question order is recorded for each participant
✅ **Text-based responses** - All questions use open-ended text boxes
✅ **Condition tracking** - Each submission includes the condition type (absent/present)
✅ **Clean data output** - Automated CSV conversion with all relevant columns

## 📊 Research Questions

This experiment can help answer:
- Does Bobby's presence affect causal attributions about the tower breaking?
- Does Bobby's presence affect judgments about who should feel angry?
- How do people reason about causation when the affected party is present vs absent?

## 📧 Questions?

Check that:
- All image files exist in the correct locations
- Image paths in `trial.js` match actual file names
- Proliferate connection is working
- Data is being submitted with question_order field
- Question randomization is working (check console log)

