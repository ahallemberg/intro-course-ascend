# Git & GitHub Hands-On Exercise

## Exercise Overview

This practical exercise will guide you through a complete Git workflow, from forking a repository to creating pull requests and handling merge conflicts.

---

## 📋 Part 1: Repository Setup

### Step 1.1: Fork the Repository
1. Navigate to the original repository on GitHub
2. Click the **Fork** button in the top-right corner
3. Select your GitHub account as the destination

### Step 1.2: Clone Your Fork
```bash
# Replace YOUR_USERNAME with your actual GitHub username
git clone https://github.com/YOUR_USERNAME/intro-course-ascend.git
cd intro-course-ascend
```

### Step 1.3: Configure Git (if not done already)
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Step 1.4: Explore the Repository
```bash
# List all files and folders
ls -la

# Check current branch
git branch

# View commit history
git log --oneline
```

**✅ Checkpoint:** You should see the main branch with initial files.

---

## 📋 Part 2: Creating Your Feature Branch 

### Step 2.1: Create a Feature Branch
```bash
# Create and switch to a new branch
git checkout -b add-multiplication

# Verify you're on the new branch
git branch
```

### Step 2.2: Understand the Current Code
1. Open `src/calculator.py` in VS Code
2. Run the calculator to see current functionality:
```bash
cd src
python calculator.py
```
3. Test the existing `add` and `subtract` functions

**✅ Checkpoint:** Calculator runs with addition and subtraction only.

---

## 📋 Part 3: Implementing New Features

### Step 3.1: Add Multiplication Function
Open `src/calculator.py` and add this function after the `subtract` function:

```python
def multiply(a, b):
    """
    Multiply two numbers together.
    
    Args:
        a (float): First number
        b (float): Second number
        
    Returns:
        float: Product of a and b
        
    Raises:
        TypeError: If inputs are not numbers
    """
    validate_numbers(a, b)
    result = a * b
    return format_result(result)
```

### Step 3.2: Update the Main Function
In the same file, update the `main()` function:

1. Change this line:
```python
print("Available operations: add, subtract")
```
to:
```python
print("Available operations: add, subtract, multiply")
```

2. Update the operation validation:
```python
if operation not in ['add', 'subtract', 'multiply']:
    print("Invalid operation. Please use 'add', 'subtract', or 'multiply'")
```

3. Add the multiplication case:
```python
elif operation == 'multiply':
    result = multiply(a, b)
    print(f"Result: {a} * {b} = {result}")
```

### Step 3.3: Test Your Changes
```bash
cd src
python calculator.py
# Test the multiply function
```

**✅ Checkpoint:** Calculator now includes working multiplication.

---

## 📋 Part 4: Committing Changes

### Step 4.1: Check What's Changed
```bash
# Return to root directory
cd ..

# See what files have been modified
git status

# See the actual changes
git diff src/calculator.py
```

### Step 4.2: Stage and Commit Changes
```bash
# Stage the modified file
git add src/calculator.py

# Check staging area
git status

# Commit with a proper message
git commit -m "feat: add multiplication function to calculator

- Add multiply() function with input validation
- Update main() to support multiplication operation
- Maintain consistent function documentation style"
```

### Step 4.3: View Your Commit
```bash
# See your commit in the log
git log --oneline -3
```

**✅ Checkpoint:** Your commit appears in the git log with proper formatting.

---

## 📋 Part 5: Updating Documentation 

### Step 5.1: Update README.md
Open the main `README.md` file and:

1. Find the "Current Features" section
2. Change:
```markdown
- Basic calculator with addition and subtraction
```
to:
```markdown
- Basic calculator with addition, subtraction, and multiplication
```

### Step 5.2: Commit Documentation Update
```bash
git add README.md
git commit -m "docs: update README to reflect multiplication feature"
```

**✅ Checkpoint:** Two commits now exist on your feature branch.

---

## 📋 Part 6: Pushing to GitHub

### Step 6.1: Push Your Branch
```bash
# Push your feature branch to your fork
git push origin add-multiplication
```

### Step 6.2: Create a Pull Request
1. Go to your fork on GitHub
2. You should see a banner suggesting to create a pull request
3. Click **"Compare & pull request"**
4. Fill in the PR details:
   - **Title:** `Add multiplication functionality`
   - **Description:**
   ```markdown
   ## Changes Made
   - Added multiply() function to calculator.py
   - Updated main() function to support multiplication
   - Updated README.md documentation
   
   ## Testing
   - Tested with various inputs including edge cases
   - Function follows existing code patterns and conventions
   ```
5. Click **"Create pull request"**

**✅ Checkpoint:** Pull request created and visible on GitHub.

---

## 📋 Part 7: Simulating Collaboration

### Step 7.1: Switch Back to Main Branch
```bash
git checkout main
```

### Step 7.2: Create Another Feature Branch
```bash
git checkout -b add-division
```

### Step 7.3: Add Division Function
Add this function to `src/calculator.py`:

```python
def divide(a, b):
    """
    Divide first number by second number.
    
    Args:
        a (float): Dividend
        b (float): Divisor
        
    Returns:
        float: Quotient of a divided by b
        
    Raises:
        TypeError: If inputs are not numbers
        ValueError: If divisor is zero
    """
    validate_numbers(a, b)
    if not is_safe_division(b):
        raise ValueError("Cannot divide by zero")
    result = a / b
    return format_result(result)
```

### Step 7.4: Update Main Function for Division
Follow the same pattern as multiplication to add division support.

### Step 7.5: Commit and Push Division Feature
```bash
git add src/calculator.py
git commit -m "feat: add division function with zero-check

- Add divide() function with zero division protection
- Update main() to support division operation
- Use existing is_safe_division() utility function"

git push origin add-division
```

**✅ Checkpoint:** Second feature branch pushed to GitHub.

---

## 🚨 Common Issues & Solutions

### Issue: "Permission denied (publickey)"
**Solution:** Set up SSH keys or use HTTPS URLs for cloning.

### Issue: "Author identity unknown"
**Solution:** Configure git user.name and user.email globally.


### Issue: Pushed to wrong branch
**Solution:** Create a new branch from the current state and push there.

---

## 📚 Additional Resources

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [VS Code Git Tutorial](https://code.visualstudio.com/docs/editor/versioncontrol)

