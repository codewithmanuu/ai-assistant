# Personal Assistant Chatbot

This Personal Assistant Chatbot is designed to recognize user intents and provide responses based on personalized data. It leverages a Naive Bayes classifier, integrated with the Rasa framework for natural language understanding and management. The current implementation uses a pre-trained machine learning model. Future updates will include the code for creating, training, and saving the AI model, along with the training dataset. This will allow users to update the dataset with their own information, enabling them to build a fully customized AI assistant.

## Features

- Intent recognition using Naive Bayes classification.
- Personalized responses based on user data.
- Real-time chat interface using Flask.
- Dockerized for easy deployment and scalability.

## Technologies Used

- **Backend**: Python, Rasa, Flask, Docker
- **Machine Learning**: Scikit-learn (Naive Bayes, k-fold cross-validation, parameter tuning)
- **Frontend**: HTML5, CSS, jQuery

## Installation


### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/codewithmanuu/ai-assistant.git
   cd chatbot-project

2. **Build and start the services using Docker Compose:**

   ```bash
   sudo docker-compose up --build

   ```windows
   docker-compose up --build

## Usage

- Access the application at http://127.0.0.1:5000
- Ask the chatbot questions such as "Who is Manu?" or "what is manu's academic?"
- The chatbot will predict the intent and provide a response based on the trained data.


## Development
 
1. **Use the following command to stop and remove containers:**

   ```bash
   sudo docker-compose down

   ```windows
   docker-compose down

2. **Use the following command to rebuild images and start services:**

   ```bash
   sudo docker-compose up --build

   ```windows
   docker-compose up --build

## Contributing

- Feel free to fork the repository and submit pull requests for new features or bug fixes.

## Contact

- For questions or comments, please reach out <mailto:manukrishna.s2001@gmail.com>

## Note

- Note: The AI model is currently trained on a limited dataset, which may result in occasional inaccurate responses.