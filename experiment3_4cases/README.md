# Experiment 3: Tower Breaking Study - 4 Conditions

## 📋 Overview
This experiment investigates how people understand causal chains in scenarios where a tower breaks and Bobby (present or absent) is affected. The study has 4 conditions based on:
- **Chain Type**: Mental vs Physical causation
- **Bobby's Presence**: Bobby present vs Bobby absent

## 🗂️ Folder Structure

```
experiment3_4cases/
├── warm_up/                        # Shared warm-up images (1 instruction + 14 story + 2 questions)
│   ├── instructions.png            # Shared instruction page (shown first)
│   ├── warm_up.001.png - .014.png  # Story images
│   ├── q_swtich.png                # Question 1: Switch understanding
│   └── q_crumble.png               # Question 2: Crumble understanding
├── exp3_mental_mental_absent/      # Condition 1 experiment code
│   └── images/
│       ├── mental_mental_absent.001.png - .012.png (12 story images)
│       ├── q_break.png
│       ├── q_break_cause.png
│       ├── q_anger.png
│       └── q_anger_cause.png
├── exp3_mental_mental_present/     # Condition 2 experiment code
│   └── images/ (10 story images + 4 question images)
├── exp3_physical_physical_absent/  # Condition 3 experiment code
│   └── images/ (12 story images + 4 question images)
└── exp3_physical_physical_present/ # Condition 4 experiment code
    └── images/ (9 story images + 4 question images)
```

## 🎯 Four Conditions

### Condition 1: Mental Chain + Bobby Absent
- **Folder**: `exp3_mental_mental_absent/`
- **Condition**: `mental_mental_absent`
- **Story**: Mental chain causes tower to break, Bobby is absent
- **Story Images**: 12 images

### Condition 2: Mental Chain + Bobby Present
- **Folder**: `exp3_mental_mental_present/`
- **Condition**: `mental_mental_present`
- **Story**: Mental chain causes tower to break, Bobby is present
- **Story Images**: 10 images

### Condition 3: Physical Chain + Bobby Absent
- **Folder**: `exp3_physical_physical_absent/`
- **Condition**: `physical_physical_absent`
- **Story**: Physical chain causes tower to break, Bobby is absent
- **Story Images**: 12 images

### Condition 4: Physical Chain + Bobby Present
- **Folder**: `exp3_physical_physical_present/`
- **Condition**: `physical_physical_present`
- **Story**: Physical chain causes tower to break, Bobby is present
- **Story Images**: 9 images

## 📝 Experiment Flow

Each participant goes through:

1. **Consent Form**
2. **Instruction Page** (`instructions.png` from `warm_up/` folder - shared for all conditions)
3. **Warm-up Story** (14 images from `warm_up/` folder - same for all conditions)
4. **Warm-up Questions** (2 questions):
   - **Switch question** (`q_swtich.png`)
   - **Crumble question** (`q_crumble.png`)
5. **Main Story** (condition-specific images: 9-12 images)
6. **Four Main Questions** (in randomized order, answered in text boxes):
   - **Break question** (`q_break.png`)
   - **Break cause question** (`q_break_cause.png`)
   - **Anger question** (`q_anger.png`)
   - **Anger cause question** (`q_anger_cause.png`)
7. **Demographics Survey**

## 🔀 Question Randomization (8 Possible Orders)

The 4 main questions are randomized following these rules:
1. **Break questions** (`break` and `break_cause`) are kept together but their order is randomized (2 possibilities)
2. **Anger questions** (`anger` and `anger_cause`) are kept together but their order is randomized (2 possibilities)
3. The **order of the two groups** (break vs anger) is also randomized (2 possibilities)

**Total**: 2 × 2 × 2 = **8 possible question orders**

### Example Question Orders:
1. `break, break_cause, anger, anger_cause`
2. `break_cause, break, anger, anger_cause`
3. `break, break_cause, anger_cause, anger`
4. `break_cause, break, anger_cause, anger`
5. `anger, anger_cause, break, break_cause`
6. `anger_cause, anger, break, break_cause`
7. `anger, anger_cause, break_cause, break`
8. `anger_cause, anger, break_cause, break`

## 📊 Data Collection

### JSON Structure
```json
{
  "participant_id": "P1737891234567_1234",
  "condition": "mental_mental_absent",
  "question_order": ["break", "break_cause", "anger", "anger_cause"],
  "responses": {
    "warmup_switch": "...",
    "warmup_crumble": "...",
    "break": "...",
    "break_cause": "...",
    "anger": "...",
    "anger_cause": "..."
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
- `condition`: Condition type (mental_mental_absent, mental_mental_present, physical_physical_absent, physical_physical_present)
- `question_order`: Order in which questions were presented (e.g., "break,break_cause,anger,anger_cause")
- `warmup_switch`: Response to warm-up switch question
- `warmup_crumble`: Response to warm-up crumble question
- `break`: Response to break question
- `break_cause`: Response to break cause question
- `anger`: Response to anger question
- `anger_cause`: Response to anger cause question
- `age`, `race`, `gender`, `ethnicity`: Demographic information

## 🔧 Converting Data

Each experiment folder has a `convert_data_to_csv.py` script. To convert data:

```bash
cd exp3_mental_mental_absent  # or any other condition folder
python convert_data_to_csv.py
```

This will read `data.json` and create `data.csv` with properly formatted columns.

## 🌐 Deploying to Proliferate

Set up 4 conditions in Proliferate:
1. **Condition 1**: Mental-Absent → Link to `exp3_mental_mental_absent/index.html`
2. **Condition 2**: Mental-Present → Link to `exp3_mental_mental_present/index.html`
3. **Condition 3**: Physical-Absent → Link to `exp3_physical_physical_absent/index.html`
4. **Condition 4**: Physical-Present → Link to `exp3_physical_physical_present/index.html`

Each condition will automatically:
- Show the shared warm-up story with 2 comprehension questions
- Display the condition-specific instruction page
- Display its specific main story
- Present 4 main questions in one of 8 randomized orders
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
  - `instructions.png`
  - Story images (9-12 images)
  - 4 question images

## 🎨 Image Organization

### Shared Images (in `warm_up/` folder):
- `instructions.png` - **Shared instruction page (shown first before warm-up)**
- `warm_up.001.png` to `.014.png` - Warm-up story (14 images)
- `q_swtich.png` - Switch question
- `q_crumble.png` - Crumble question

### Condition-Specific Images (in each `exp3_*/images/` folder):
- `[condition_name].001.png` to `.0XX.png` - Main story images (9-12 images depending on condition)
- `q_break.png` - Break question
- `q_break_cause.png` - Break cause question
- `q_anger.png` - Anger question
- `q_anger_cause.png` - Anger cause question

## 🚀 Testing

Before deploying, test each condition locally:
1. Open `exp3_[condition_name]/index.html` in a browser
2. Go through the entire flow
3. Check that warm-up questions appear
4. Verify instruction page shows
5. Check that questions appear in randomized order
6. Check console for question order logged
7. Verify data is collected correctly with question order

## 📈 Data Analysis Tips

When analyzing data:
- Use the `question_order` column to control for question order effects
- Compare responses across the 4 conditions
- Check if warm-up questions show good understanding
- Analyze break vs anger attributions
- Consider the role of Bobby's presence/absence

## 🔍 Key Features

✅ **Shared instruction** - All conditions use the same instruction page (shown first)
✅ **Shared warm-up** - All conditions use the same warm-up to ensure consistent understanding
✅ **Comprehension check** - Two warm-up questions test participant understanding
✅ **Question randomization** - 8 possible orders to control for order effects
✅ **Order tracking** - Question order is recorded for each participant
✅ **Text-based responses** - All questions use open-ended text boxes
✅ **Condition tracking** - Each submission includes the condition type
✅ **Clean data output** - Automated CSV conversion with all relevant columns

## 📧 Questions?

Check that:
- All image files exist in the correct locations
- Image paths in `trial.js` match actual file names
- Warm-up images are accessible from each condition folder
- Proliferate connection is working
- Data is being submitted with question_order field
- Question randomization is working (check console log)
