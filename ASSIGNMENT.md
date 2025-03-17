# SSO Flask Application - Homework Assignment

This homework assignment will help you understand the single sign-on (SSO) implementation and protected routes in this Flask application.

## Task 1: Clone and Initialize the Project

Use the information from README.md to set up the development environment.

**Steps:**

1. Clone the repository to your local machine
2. Create and activate a virtual environment
3. Install required dependencies from requirements.txt
4. Configure any necessary environment variables
5. Run the application and verify it starts correctly

## Task 2: Create a Protected User Profile Page

Create a new protected endpoint that displays user data with conditional UI elements based on user role.

**Steps:**

1. Create a new route in the main blueprint (e.g., `/profile`)
2. Apply the `@login_required` decorator to protect the route
3. Create a new template to display user information from the session
4. Add logic to check if the user's role is "superadmin"
5. If the user is a superadmin, display an "Edit" button on the page
6. Test the route with different user roles to verify the conditional display

## Task 3: Create a Role-Based Protected Endpoint

Implement a protected endpoint that displays different content based on the user's role.

**Steps:**

1. Create a new route in the main blueprint (e.g., `/admin`)
2. Protect the route with the `@login_required` decorator
3. Create a template for this page
4. Add server-side logic to check if the user's role is "superadmin"
5. If the role is "superadmin", display the message: "Your role is superadmin, the force is strong with you"
6. If the role is not "superadmin", return a 403 response with the message: "403 - You don't have permission to access this page"
7. Test the endpoint with different user roles

## Task 4: Implement Automatic SSO Login on Authentication Failure

Create an endpoint that demonstrates automatic SSO login triggering when authentication fails.

**Steps:**

1. Create a new route that returns a 401 status code (e.g., `/api/protected-data`)
2. Create another route that returns a page with a "Get Data" button (e.g., `/data`)
3. In the template for the `/data` page, add a button that sends a GET request to the protected endpoint
4. Create a JavaScript file or add a script to the template that:
   - Creates a new instance of the SSO class
   - Handles the fetch response from the button click
   - Checks if the response status is 401
   - If status is 401, calls the `openLoginWindow()` method to trigger the SSO flow
5. Test the implementation by clicking the button when not authenticated
