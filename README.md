echo "# API Automation Project - Contact List App

This project automates the testing of a Contact List web application's RESTful APIs hosted at https://thinking-tester-contact-list.herokuapp.com using **Python**, **Pytest**, and the **Requests** library.

## Project Structure

\`\`\`
selenium_project_1/
├── test_api.py               # Test cases for user & contact endpoints
├── utils/
│   └── apis.py               # API wrapper class (GET, POST, PATCH, etc.)
├── data/
│   └── contact_data.py       # Functions to generate dynamic user/contact data
├── requirements.txt          # List of required Python packages
\`\`\`

## Features Tested

- User Registration
- User Authentication (Login, Logout)
- Fetching Authenticated User Details
- Updating User Info
- Deleting a User
- Adding New Contacts
- Retrieving Contacts

##  Installation & Setup

### 1. Clone the Repository

\`\`\`bash
git clone https://github.com/kalyan2003/selenium_form_automation.git
cd selenium_project_1
\`\`\`

### 2. Create Virtual Environment (Optional but Recommended)

\`\`\`bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
\`\`\`

### 3. Install Dependencies

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 4. Run Tests

\`\`\`bash
pytest test_api.py -v
\`\`\`

##  Sample Test Flow

- \`test_register_user\`: Registers a new user.
- \`test_get_user\`: Fetches current user details.
- \`test_patch_user\`: Partially updates the user profile.
- \`test_add_contact\`: Adds a new contact.
- \`test_get_contact\`: Fetches all contacts for the user.

## Dependencies

Add these to your \`requirements.txt\` if not already present:

\`\`\`
pytest
requests
\`\`\`

