# FitJoe

FitJoe is a fitness chatbot powered by the GPT API. It provides personalized food suggestions based on users' goals and nutritional requirements. Whether you want to gain muscle, lose weight, or follow a specific dietary plan, FitJoe has got you covered. With its intuitive interface and expert guidance, FitJoe helps you make healthier food choices and supports you in achieving your fitness goals.

## Getting Started

To get FitJoe up and running on your local machine, follow the steps below:

### Installation

1. Clone the repository:

```shell
git clone https://github.com/HarshKakran/FitJoe.git
```
2. Navigate to the project directory:
```shell
cd fitjoe
```
3. Create a Python virtual environment:
```shell
python3 -m venv env
```
4. Activate the virtual environment:
```shell
source env/bin/activate
````

5. Install the backend dependencies:
```shell
pip install -r requirements.txt
```
6. Install the frontend dependencies:
```shell
cd frontend
npm install
```
### Configuration
Before running FitJoe, you need to configure the API credentials for GPT. Follow these steps:

- Sign up for the GPT API and obtain your API key.
- Create a file named .env in the root directory of the project. The structure of the env file could be found in the example_env present in the root folder.
- Replace <YOUR_API_KEY> with your actual API key:
```makefile
GPT_API_KEY= <YOUR_API_KEY>
```
### Usage
1. Start the Flask backend server:
```shell
python app.py
```
2. In a separate terminal, navigate to the frontend directory:
```shell
cd frontend
```
3. Start the React frontend development server:
```shell
npm start
```
4. Open your web browser and visit http://localhost:3000 to access FitJoe.

### How FitJoe Works
FitJoe leverages the power of the GPT API to generate personalized food suggestions based on user input. It analyzes the user's goals, dietary preferences, and nutritional requirements to provide tailored recommendations. The GPT API understands natural language and can engage in meaningful conversations with users, allowing for an interactive and user-friendly experience.

FitJoe's backend is built with Flask, a lightweight Python web framework. It handles the API requests, processes user input, and communicates with the GPT API to generate responses. The frontend is developed using React, a popular JavaScript library for building user interfaces, providing an intuitive and responsive chatbot interface.

### Customization

FitJoe is designed to be customizable, allowing you to adapt it to different types of chatbot applications. To customize FitJoe according to your specific needs, follow the steps below:

1. Understand the System Context: The system message, defined in the conversation flow, sets the behavior and tone of FitJoe. You can modify the system message in the conversation flow to align with the personality and purpose of your chatbot.

2. Adjust Conversation Flow: FitJoe's conversation flow determines how it interacts with users. You can modify the conversation flow to include or exclude specific prompts, add branching logic, or introduce new features based on your requirements.

3. Extend Functionality: FitJoe's functionality can be expanded by adding new features or integrating with external APIs. You can enhance FitJoe by incorporating additional capabilities like user authentication, database integration, or integrating with other fitness-related services.

4. Customize User Interface: The user interface of FitJoe can be tailored to match your branding or application design. You can modify the colors, fonts, layout, or add custom components to create a unique user experience.
