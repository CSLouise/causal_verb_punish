# Experiment 2 V2: Accidental vs Intentional - 2 Conditions

## 📋 Overview
This is version 2 of Experiment 2, investigating how people understand causal chains in accidental vs intentional scenarios using bike and mirror stories.

## 🗂️ Folder Structure

```
experiment2_accidental_v2/
└── images/
    ├── instructions.png (shared instruction page)
    ├── bike/
    │   ├── bike_adults_accident.001.png - .008.png (8 story images)
    │   ├── bike_adults_accident_q_cause.png
    │   ├── bike_adults_accident_q_simple.png
    │   ├── bike_adults_accident_q_fault.png
    │   └── bike_adults_accident_q_punish.png
    └── mirror/
        ├── mirror_adults_accident.001.png - .009.png (9 story images)
        ├── mirror_adults_accident_q_cause.png
        ├── mirror_adults_accident_q_simple.png
        ├── mirror_adults_accident_q_fault.png
        └── mirror_adults_accident_q_punish.png

experiment2_intentional_v2/
└── images/
    ├── instructions.png (shared instruction page)
    ├── bike/
    │   ├── bike_adults_intent.001.png - .010.png (10 story images)
    │   ├── bike_adults_intent_q_cause.png
    │   ├── bike_adults_intent_q_simple.png
    │   ├── bike_adults_intent_q_fault.png
    │   └── bike_adults_intent_q_punish.png
    └── mirror/
        ├── mirror_adults_intent.001.png - .009.png (9 story images)
        ├── mirror_adults_intent_q_cause.png
        ├── mirror_adults_intent_q_simple.png
        ├── mirror_adults_intent_q_fault.png
        └── mirror_adults_intent_q_punish.png
```

## 🎯 Two Conditions

### Condition 1: Accidental
- **Folder**: `experiment2_accidental_v2/`
- **Condition**: `accidental`
- **Stories**: 
  - Bike: 8 images
  - Mirror: 9 images

### Condition 2: Intentional
- **Folder**: `experiment2_intentional_v2/`
- **Condition**: `intentional`
- **Stories**: 
  - Bike: 10 images
  - Mirror: 9 images

## 📝 Experiment Flow

Each participant goes through:

1. **Consent Form**
2. **Instruction Page** (`instructions.png`)
3. **First Scenario** (bike or mirror, randomized):
   - Story images
   - 4 questions in controlled random order
4. **Second Scenario** (bike or mirror, whichever wasn't first):
   - Story images
   - 4 questions in controlled random order
5. **Demographics Survey**

## 🔀 Question Randomization (4 Possible Orders per Scenario)

The 4 questions follow a **controlled randomization**:
- **(cause, simple) pair** must appear **FIRST**
  - Within this pair, order is randomized (2 possibilities)
- **(fault, punish) pair** must appear **SECOND**
  - Within this pair, order is randomized (2 possibilities)

**Total per scenario**: 2 × 2 = **4 possible question orders**

### Example Question Orders:
1. `cause, simple, fault, punish`
2. `simple, cause, fault, punish`
3. `cause, simple, punish, fault`
4. `simple, cause, punish, fault`

### Rationale:
This ensures that causal attribution questions (cause, simple) are asked before responsibility/punishment questions (fault, punish), while still controlling for order effects within each pair.

## 📊 Data Collection

### JSON Structure
```json
{
  "participant_id": "P1737891234567_1234",
  "condition": "accidental",
  "scenario_order": ["bike", "mirror"],
  "question_orders": {
    "bike": ["cause", "simple", "fault", "punish"],
    "mirror": ["simple", "cause", "punish", "fault"]
  },
  "responses": {
    "bike_cause": "...",
    "bike_simple": "...",
    "bike_fault": "...",
    "bike_punish": "...",
    "mirror_cause": "...",
    "mirror_simple": "...",
    "mirror_fault": "...",
    "mirror_punish": "..."
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
- `condition`: Condition type (accidental or intentional)
- `scenario_order`: Order of scenarios (e.g., "bike,mirror")
- `bike_question_order`: Question order for bike scenario (e.g., "cause,simple,fault,punish")
- `mirror_question_order`: Question order for mirror scenario
- `bike_cause`, `bike_simple`, `bike_fault`, `bike_punish`: Bike scenario responses
- `mirror_cause`, `mirror_simple`, `mirror_fault`, `mirror_punish`: Mirror scenario responses
- `age`, `race`, `gender`, `ethnicity`: Demographic information

## 🔧 Converting Data

Each experiment folder has a `convert_data_to_csv.py` script. To convert data:

```bash
cd experiment2_accidental_v2  # or experiment2_intentional_v2
python convert_data_to_csv.py
```

This will read `data.json` and create `data.csv` with properly formatted columns.

## 🌐 Deploying to Proliferate

Set up 2 conditions in Proliferate:
1. **Condition 1**: Accidental → Link to `experiment2_accidental_v2/index.html`
2. **Condition 2**: Intentional → Link to `experiment2_intentional_v2/index.html`

Example URLs (adjust based on your GitHub Pages setup):
- Accidental: `https://cslouise.github.io/causal_verb_punish/experiment2_accidental_v2`
- Intentional: `https://cslouise.github.io/causal_verb_punish/experiment2_intentional_v2`

Each condition will automatically:
- Show the shared instruction page
- Display bike and mirror stories in randomized order
- Present 4 questions per story in controlled random order
- Record scenario order and question orders
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
1. Open `experiment2_[condition]_v2/index.html` in a browser
2. Check console logs for:
   - Scenario order
   - Question order for each scenario
3. Verify questions appear in correct controlled order
4. Confirm data is collected with all order information

## 📈 Data Analysis Tips

When analyzing data:
- Use `scenario_order` to control for scenario presentation order
- Use `bike_question_order` and `mirror_question_order` to control for question order effects
- Note: (cause, simple) questions always precede (fault, punish) questions
- Compare responses between accidental and intentional conditions
- Analyze within-pair order effects (cause vs simple, fault vs punish)

## 🔍 Key Features

✅ **Scenario randomization** - Bike and mirror order is randomized
✅ **Controlled question order** - Causal questions before responsibility questions
✅ **Within-pair randomization** - Order effects controlled within question pairs
✅ **Order tracking** - Both scenario and question orders recorded
✅ **Text-based responses** - All questions use open-ended text boxes
✅ **Condition tracking** - Each submission includes condition type
✅ **Clean data output** - Automated CSV conversion with all columns

## 🎯 Research Questions

This experiment can help answer:
- How do intentionality judgments affect causal attributions?
- Does question order within pairs affect responses?
- Are there differences in reasoning between bike and mirror scenarios?
- How do people reason about cause before considering fault/punishment?

## 📧 Questions?

Check that:
- All image files exist in correct locations
- Image paths in `trial.js` match actual file names
- Console logs show correct randomization
- Question orders follow the controlled pattern
- Data includes both scenario_order and question_orders
