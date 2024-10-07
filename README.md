# Welcome

Thank you for participating in our interview process for our Senior Frontend Developer position. We are excited to see your skills and creativity in action. This exercise is designed to evaluate your ability to build a functional and visually appealing dashboard using the [React](https://react.dev/) and [Typescript](https://www.typescriptlang.org/). You will have up to one week to complete this task and prepare a presentation of your project.

- You can also use any UI libraries or charting libraries (e.g., D3.js, Chart.js, Material-UI, Tailwind CSS).

# Table of Contents
- [Objective](#objective)
- [Duration](#duration)
- [JSON Data](#json-data)
- [Requirements](#requirements)
- [Deliverables](#deliverables)
- [Evaluation Criteria](#evaluation-criteria) 
- [Most important](#and-most-important-have-fun)

# Exercise Proposition

## Objective
Create a dynamic and interactive dashboard that visualizes data from a provided JSON file. The goal is to demonstrate your proficiency in frontend development using React and Typescript, including data handling, UI/UX design, and responsiveness.

## Duration
We respect your time and understand you have other commitments. Please do not feel obligated to spend more than 3 hours on this project. Focus on what you're comfortable with and can reasonably achieve within this timeframe.

## JSON Data
You will be provided with a JSON file containing a dataset. The dataset includes various fields that you will need to visualize in your dashboard. The structure of the JSON file is as follows and you can access the [`transactions.json`](./dataset/transactions.json):

```json
[
  {
    "transaction_id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
    "customer_name": "John Doe",
    "email": "johndoe@example.com",
    "age": 28,
    "purchase_date": "2023-08-25T12:34:56Z",
    "products": [
      {
        "product_id": 101,
        "product_name": "Wireless Mouse",
        "category": "Electronics",
        "quantity": 1,
        "price": 29.99
      },
      {
        "product_id": 102,
        "product_name": "Keyboard",
        "category": "Electronics",
        "quantity": 1,
        "price": 49.99
      }
    ],
    "payment_method": "Credit Card",
    "total_amount": 79.98,
    "currency": "USD",
    "status": "Completed"
  },
]
```

## Requirements

1. **Data Visualization**: The dashboard should include at least 2 different types of visualizations (e.g., bar chart, line chart, pie chart) to represent the data effectively.
2. **Filtering and Sorting**: Implement functionality to filter and sort the data based on different criteria (e.g., category, price range, date added).
3. **Responsive Design**: Ensure the dashboard is fully responsive and works well on various screen sizes, including desktops, tablets, and mobile devices.
4. **User Interaction**: Provide interactive elements such as tooltips, hover effects, and clickable elements to enhance the user experience.
5. **Code Quality**: Write clean, maintainable, and well-documented code. Use best practices for frontend development, including state management, component architecture, and performance optimization.
6. **Testing**: Write unit tests for critical components (e.g.: using [vitest](https://vitest.dev/)) or functions to ensure the reliability of the dashboard.
7. **Deployment (optional)**: Upload your webapp to Github Pages. This is optional. If you can serve it on localhost, it will be ok too.

## Deliverables

1. **Source Code**: Create a pull request to this repository with your source code changes to the [solution](./solution/) folder.
1. **Github Pages (optional)**: your application deployed to [Github Pages](https://pages.github.com/).
1. **Documentation**: A README file in the GitHub repository with instructions on how to set up and run the project locally, as well as any other relevant information.
1. **Presentation**: Prepare a presentation (≈ 30 minutes) to walk us through your project. The presentation should cover:
   - The overall architecture and design of the dashboard.
   - The technologies and libraries used.
   - Key features and functionalities implemented.
   - **Challenges faced and how you overcame them.**
   - Decisions you had to make given the exercise's time constraints.
   - Any additional improvements or features you would add given more time.

## Evaluation Criteria

Your submission will be evaluated based on the following criteria:
1. **Functionality**: How well does the dashboard meet the requirements and handle the provided data?
2. **UI/UX Design**: Is the dashboard visually appealing and easy to use?
3. **Code Quality**: Is the code clean, well-organized, and maintainable?
4. **Responsiveness**: Does the dashboard work well on different devices and screen sizes?
5. **Presentation**: How effectively do you communicate your approach, decisions, and the overall project during the presentation?

We look forward to seeing your work and hearing about your process. Good luck!

## And most important: Have fun!

![have-fun](https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGE5aDdtbHBuaHBmM3FkcWt1NTlnYWc4bmNuZzIzemk4azE2MnlsNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/kafM1F9H8IqUQISoFm/giphy.gif)