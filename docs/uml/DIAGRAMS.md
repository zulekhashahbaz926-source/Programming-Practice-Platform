# UML Diagrams for Programming Practice Platform

This folder contains professional UML diagrams for the Programming Practice Platform project.

## Diagrams

### 1. Class Diagram
**File:** `class_diagram.svg` / `class_diagram.png`

Shows the main classes and their relationships:
- **User:** Manages authentication and profile
- **Problem:** Represents coding problems with test cases
- **Attempt:** Records user submission attempts
- **Quiz:** Quiz management and grading
- **Progress:** Tracks user progress and statistics

**Relationships:**
- User has many Attempts (1:*)
- Problem has many Attempts (1:*)
- User tracks Progress (dependency)
- User takes Quiz (dependency)

### 2. Use Case Diagram
**File:** `use_case_diagram.svg` / `use_case_diagram.png`

Depicts two actors and their interactions:
- **Student Actor:** Browse problems, write/run code, submit solutions, take quizzes, view progress, earn badges
- **Admin Actor:** Manage problems, manage quizzes, view all statistics

**Relationships:**
- `<<include>>` Submit → Evaluate
- `<<extend>>` View Progress → Earn Badges

### 3. Sequence Diagram
**File:** `sequence_diagram.svg` / `sequence_diagram.png`

Shows the flow of a code submission and evaluation:
1. User logs in via Auth service
2. User opens problem from database
3. User writes and submits code
4. Server evaluates code against test cases
5. Results saved to database
6. Progress updated
7. Result displayed to user

**Key Participants:**
- User
- GUI (Frontend)
- Evaluator (Backend service)
- Database
- Auth Service

### 4. Activity Diagram
**File:** `activity_diagram.svg` / `activity_diagram.png`

Illustrates the workflow of code submission:
1. Start
2. Open Problem, Write Code, Submit
3. Server: Evaluate Code (Run Tests)
4. Save Attempt and Update Progress
5. Display Result and Feedback
6. End

## Regenerating Diagrams

To regenerate the SVG and PNG files:

```bash
# Convert SVG to PNG (requires cairosvg or similar tool)
python ../../scripts/convert_svgs_to_pngs.py

# Or capture screenshots from SVG files
python ../../scripts/svg_to_png_screenshot.py
```

## Usage Notes

- All diagrams follow UML 2.0 standards
- SVG files are scalable and vector-based (recommended for printing)
- PNG files are high-resolution (2400px width) for presentations
- Use in documentation, presentations, and reports
