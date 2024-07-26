# Author: Hamed Gharghi
# Date: 2024-07-26
# Description: An educational quiz game where the player answers multiple-choice questions and scores are tracked. The game provides feedback on each answer and shows the final score.

import random

def display_question(question, options):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

def get_answer():
    try:
        answer = int(input("Enter the number of your choice: "))
        return answer
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_answer()

def quiz_game():
    questions = [
        {"question": "What is the capital of France?", "options": ["Berlin", "Madrid", "Paris", "Rome"], "answer": 3},
        {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": 2},
        {"question": "What is the largest ocean on Earth?", "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "answer": 4},
        {"question": "Who wrote 'To Kill a Mockingbird'?", "options": ["Harper Lee", "Mark Twain", "Ernest Hemingway", "F. Scott Fitzgerald"], "answer": 1},
        {"question": "What is the chemical symbol for Gold?", "options": ["Au", "Ag", "Pb", "Fe"], "answer": 1},
        {"question": "How many continents are there on Earth?", "options": ["5", "6", "7", "8"], "answer": 3},
        {"question": "What is the speed of light in a vacuum?", "options": ["300,000 km/s", "150,000 km/s", "100,000 km/s", "200,000 km/s"], "answer": 1},
        {"question": "Who painted the Mona Lisa?", "options": ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Claude Monet"], "answer": 1},
        {"question": "What is the hardest natural substance on Earth?", "options": ["Gold", "Iron", "Diamond", "Platinum"], "answer": 3},
        {"question": "What is the smallest prime number?", "options": ["1", "2", "3", "5"], "answer": 2},
        {"question": "In which year did the Titanic sink?", "options": ["1900", "1912", "1920", "1930"], "answer": 2},
        {"question": "What is the largest mammal in the world?", "options": ["Elephant", "Blue Whale", "Giraffe", "Shark"], "answer": 2},
        {"question": "Which element has the atomic number 1?", "options": ["Helium", "Hydrogen", "Lithium", "Beryllium"], "answer": 2},
        {"question": "What is the capital of Japan?", "options": ["Beijing", "Seoul", "Tokyo", "Bangkok"], "answer": 3},
        {"question": "Which planet is closest to the Sun?", "options": ["Venus", "Earth", "Mercury", "Mars"], "answer": 3},
        {"question": "What is the largest desert in the world?", "options": ["Sahara", "Gobi", "Kalahari", "Antarctic"], "answer": 4},
        {"question": "What is the chemical formula for water?", "options": ["H2O", "CO2", "NaCl", "O2"], "answer": 1},
        {"question": "Who is known as the 'Father of Computers'?", "options": ["Charles Babbage", "Alan Turing", "Ada Lovelace", "John von Neumann"], "answer": 1},
        {"question": "What is the largest organ in the human body?", "options": ["Heart", "Liver", "Skin", "Lungs"], "answer": 3},
        {"question": "Which country is known as the Land of the Rising Sun?", "options": ["China", "Japan", "South Korea", "Thailand"], "answer": 2},
        {"question": "What is the smallest country in the world by land area?", "options": ["Monaco", "San Marino", "Vatican City", "Liechtenstein"], "answer": 3},
        {"question": "What is the name of the longest river in the world?", "options": ["Amazon", "Nile", "Yangtze", "Mississippi"], "answer": 2},
        {"question": "What is the chemical symbol for Silver?", "options": ["Au", "Ag", "Pb", "Fe"], "answer": 2},
        {"question": "What year did World War I begin?", "options": ["1912", "1914", "1916", "1918"], "answer": 2},
        {"question": "Who discovered penicillin?", "options": ["Marie Curie", "Alexander Fleming", "Louis Pasteur", "Isaac Newton"], "answer": 2},
        {"question": "What is the main ingredient in guacamole?", "options": ["Tomato", "Avocado", "Onion", "Pepper"], "answer": 2},
        {"question": "Which planet is known for its rings?", "options": ["Earth", "Mars", "Saturn", "Uranus"], "answer": 3},
        {"question": "What is the largest island in the world?", "options": ["New Guinea", "Greenland", "Borneo", "Madagascar"], "answer": 2},
        {"question": "What is the name of the galaxy that contains our solar system?", "options": ["Andromeda", "Milky Way", "Triangulum", "Sombrero"], "answer": 2},
        {"question": "Who wrote 'Pride and Prejudice'?", "options": ["Jane Austen", "Emily Brontë", "Charlotte Brontë", "Mary Shelley"], "answer": 1},
        {"question": "What is the tallest mountain in the world?", "options": ["K2", "Kangchenjunga", "Everest", "Makalu"], "answer": 3},
        {"question": "Which element has the chemical symbol 'O'?", "options": ["Oxygen", "Osmium", "Opium", "Oganesson"], "answer": 1},
        {"question": "What is the longest-running Broadway show?", "options": ["The Phantom of the Opera", "Cats", "Les Misérables", "Chicago"], "answer": 1},
        {"question": "In which year did the Berlin Wall fall?", "options": ["1987", "1988", "1989", "1990"], "answer": 3},
        {"question": "What is the largest species of shark?", "options": ["Great White Shark", "Hammerhead Shark", "Whale Shark", "Tiger Shark"], "answer": 3},
        {"question": "Which is the only U.S. state to begin with the letter 'A'?", "options": ["Alaska", "Arizona", "Arkansas", "Alabama"], "answer": 1},
        {"question": "Who was the first person to step on the moon?", "options": ["Buzz Aldrin", "Neil Armstrong", "Yuri Gagarin", "Michael Collins"], "answer": 2},
        {"question": "What is the hardest natural substance found on Earth?", "options": ["Gold", "Iron", "Diamond", "Quartz"], "answer": 3},
        {"question": "Which famous scientist developed the theory of relativity?", "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Niels Bohr"], "answer": 2},
        {"question": "What is the smallest planet in our solar system?", "options": ["Mercury", "Mars", "Venus", "Earth"], "answer": 1},
        {"question": "What is the primary language spoken in Brazil?", "options": ["Spanish", "Portuguese", "English", "French"], "answer": 2},
        {"question": "What type of animal is the largest living land carnivore?", "options": ["Lion", "Elephant", "Polar Bear", "Grizzly Bear"], "answer": 3},
        {"question": "What is the main function of red blood cells?", "options": ["Fight infection", "Carry oxygen", "Aid digestion", "Regulate temperature"], "answer": 2},
        {"question": "Who was the first female Prime Minister of the United Kingdom?", "options": ["Theresa May", "Margaret Thatcher", "Priti Patel", "Emily Thornberry"], "answer": 2},
        {"question": "Which famous physicist is known for his laws of motion?", "options": ["Galileo Galilei", "Isaac Newton", "Albert Einstein", "Nikola Tesla"], "answer": 2},
        {"question": "What is the primary ingredient in traditional Japanese sushi?", "options": ["Chicken", "Beef", "Fish", "Rice"], "answer": 4},
        {"question": "Which chemical element has the symbol 'Na'?", "options": ["Sodium", "Nickel", "Neon", "Nitrogen"], "answer": 1},
        {"question": "What is the capital city of Canada?", "options": ["Toronto", "Montreal", "Ottawa", "Vancouver"], "answer": 3},
        {"question": "What is the main source of energy for the Earth?", "options": ["Moon", "Sun", "Wind", "Water"], "answer": 2},
        {"question": "What is the process by which plants make their food?", "options": ["Photosynthesis", "Respiration", "Fermentation", "Germination"], "answer": 1},
        {"question": "Which continent is known as the Dark Continent?", "options": ["Asia", "Europe", "Africa", "Australia"], "answer": 3},
        {"question": "What is the most abundant gas in Earth's atmosphere?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": 3},
        {"question": "Which country is known as the Land of Fire and Ice?", "options": ["New Zealand", "Iceland", "Norway", "Sweden"], "answer": 2},
        {"question": "Who is the author of the 'Harry Potter' series?", "options": ["J.K. Rowling", "J.R.R. Tolkien", "Stephen King", "George R.R. Martin"], "answer": 1},
        {"question": "What is the tallest waterfall in the world?", "options": ["Niagara Falls", "Victoria Falls", "Angel Falls", "Iguazu Falls"], "answer": 3},
        {"question": "Which element is represented by the symbol 'Fe'?", "options": ["Iron", "Lead", "Francium", "Fermium"], "answer": 1},
        {"question": "Which planet is known as the Morning Star?", "options": ["Venus", "Mars", "Jupiter", "Mercury"], "answer": 1},
        {"question": "Which scientist is known for the theory of evolution by natural selection?", "options": ["Charles Darwin", "Gregor Mendel", "Louis Pasteur", "James Watson"], "answer": 1},
        {"question": "What is the main ingredient in a traditional Greek salad?", "options": ["Tomato", "Lettuce", "Cucumber", "Olive"], "answer": 4},
        {"question": "Which city is known as the Big Apple?", "options": ["Los Angeles", "Chicago", "New York", "San Francisco"], "answer": 3},
        {"question": "What is the freezing point of water in Celsius?", "options": ["0°C", "32°C", "100°C", "273°C"], "answer": 1},
        {"question": "What is the currency used in Japan?", "options": ["Yuan", "Won", "Yen", "Ringgit"], "answer": 3},
        {"question": "Which organ is responsible for pumping blood throughout the body?", "options": ["Brain", "Liver", "Lungs", "Heart"], "answer": 4},
        {"question": "What is the name of the famous clock tower in London?", "options": ["Big Ben", "London Eye", "Tower Bridge", "Buckingham Palace"], "answer": 1},
        {"question": "Which element has the atomic number 79?", "options": ["Gold", "Silver", "Platinum", "Copper"], "answer": 1},
        {"question": "What is the smallest bone in the human body?", "options": ["Stapes", "Incus", "Malleus", "Clavicle"], "answer": 1},
        {"question": "What is the name of the device used to measure temperature?", "options": ["Barometer", "Thermometer", "Altimeter", "Hygrometer"], "answer": 2},
        {"question": "Which famous scientist developed the polio vaccine?", "options": ["Jonas Salk", "Albert Sabin", "Louis Pasteur", "Robert Koch"], "answer": 1},
        {"question": "Which gas is most commonly used in light bulbs?", "options": ["Oxygen", "Hydrogen", "Argon", "Neon"], "answer": 3},
        {"question": "Which planet is known as the 'Giant Red Spot'?", "options": ["Jupiter", "Saturn", "Neptune", "Uranus"], "answer": 1},
        {"question": "Which country is the largest by land area?", "options": ["Canada", "United States", "China", "Russia"], "answer": 4},
        {"question": "What is the name of the famous river that flows through Egypt?", "options": ["Amazon", "Nile", "Yangtze", "Mississippi"], "answer": 2},
        {"question": "Who was the 16th President of the United States?", "options": ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "John Adams"], "answer": 1},
        {"question": "What is the main ingredient in traditional Italian pesto sauce?", "options": ["Tomato", "Basil", "Garlic", "Olive"], "answer": 2},
        {"question": "Which planet is known for its prominent ring system?", "options": ["Saturn", "Jupiter", "Uranus", "Neptune"], "answer": 1},
        {"question": "What is the chemical symbol for Carbon?", "options": ["C", "Ca", "Co", "Cl"], "answer": 1},
        {"question": "Which famous structure is located in Paris, France?", "options": ["Eiffel Tower", "Colosseum", "Great Wall", "Taj Mahal"], "answer": 1},
        {"question": "What is the most spoken language in the world?", "options": ["English", "Mandarin", "Spanish", "Hindi"], "answer": 2},
        {"question": "Who wrote 'The Catcher in the Rye'?", "options": ["J.D. Salinger", "F. Scott Fitzgerald", "Ernest Hemingway", "John Steinbeck"], "answer": 1},
        {"question": "What is the largest volcano in the world?", "options": ["Mount Fuji", "Mount Kilimanjaro", "Mauna Loa", "Mount St. Helens"], "answer": 3},
        {"question": "Which country is famous for the Taj Mahal?", "options": ["India", "Pakistan", "Bangladesh", "Nepal"], "answer": 1},
        {"question": "What is the main ingredient in traditional French ratatouille?", "options": ["Potato", "Tomato", "Eggplant", "Zucchini"], "answer": 3},
        {"question": "Which planet is known for its Great Red Spot?", "options": ["Jupiter", "Saturn", "Neptune", "Mars"], "answer": 1},
        {"question": "What is the primary color of the Sun as seen from Earth?", "options": ["Blue", "Yellow", "Red", "White"], "answer": 2},
        {"question": "Which animal is known for its black and white stripes?", "options": ["Tiger", "Zebra", "Panda", "Giraffe"], "answer": 2},
        {"question": "What is the largest continent by population?", "options": ["Africa", "Asia", "Europe", "North America"], "answer": 2},
        {"question": "What is the chemical symbol for Sodium?", "options": ["Na", "So", "S", "Sd"], "answer": 1},
        {"question": "Which element has the atomic number 2?", "options": ["Helium", "Hydrogen", "Oxygen", "Neon"], "answer": 1},
        {"question": "What is the process by which plants make their food using sunlight?", "options": ["Photosynthesis", "Respiration", "Fermentation", "Digestion"], "answer": 1},
        {"question": "What is the name of the famous tower in Pisa, Italy?", "options": ["Leaning Tower of Pisa", "Eiffel Tower", "Big Ben", "Colosseum"], "answer": 1},
        {"question": "Which ocean is the largest?", "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "answer": 4},
        {"question": "Which city is known as the 'City of Angels'?", "options": ["Los Angeles", "Paris", "Rome", "New York"], "answer": 1},
        {"question": "Who is known as the 'King of Pop'?", "options": ["Elvis Presley", "Michael Jackson", "Prince", "Madonna"], "answer": 2},
        {"question": "What is the hardest natural substance on Earth?", "options": ["Gold", "Diamond", "Iron", "Platinum"], "answer": 2},
        {"question": "Which famous playwright wrote 'Romeo and Juliet'?", "options": ["William Shakespeare", "George Bernard Shaw", "Tennessee Williams", "Arthur Miller"], "answer": 1},
        {"question": "What is the capital city of Italy?", "options": ["Venice", "Florence", "Rome", "Milan"], "answer": 3},
        {"question": "Which is the largest planet in our solar system?", "options": ["Earth", "Mars", "Saturn", "Jupiter"], "answer": 4},
        {"question": "What is the process by which a caterpillar becomes a butterfly?", "options": ["Metamorphosis", "Photosynthesis", "Germination", "Respiration"], "answer": 1},
        {"question": "Which country is famous for its kangaroos?", "options": ["Australia", "New Zealand", "South Africa", "India"], "answer": 1},
        {"question": "What is the chemical symbol for Gold?", "options": ["Au", "Ag", "Pb", "Fe"], "answer": 1},
        {"question": "Which human organ is responsible for detoxifying the blood?", "options": ["Liver", "Kidney", "Heart", "Lungs"], "answer": 1},
        {"question": "What is the capital city of Australia?", "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"], "answer": 4},
        {"question": "Which famous structure is found in India?", "options": ["Eiffel Tower", "Great Wall", "Taj Mahal", "Colosseum"], "answer": 3},
        {"question": "What is the name of the largest ocean on Earth?", "options": ["Atlantic", "Indian", "Arctic", "Pacific"], "answer": 4},
        {"question": "Which planet is known for its extensive ring system?", "options": ["Saturn", "Jupiter", "Uranus", "Neptune"], "answer": 1},
        {"question": "What is the largest organ in the human body?", "options": ["Liver", "Skin", "Lungs", "Heart"], "answer": 2},
        {"question": "What is the capital city of Brazil?", "options": ["Rio de Janeiro", "São Paulo", "Brasília", "Salvador"], "answer": 3},
        {"question": "What is the smallest planet in our solar system?", "options": ["Mercury", "Mars", "Venus", "Earth"], "answer": 1},
        {"question": "Which country is known for the Eiffel Tower?", "options": ["Germany", "France", "Italy", "Spain"], "answer": 2},
        {"question": "What is the chemical symbol for Helium?", "options": ["He", "H", "Hl", "Ho"], "answer": 1},
        {"question": "Which famous scientist developed the theory of relativity?", "options": ["Isaac Newton", "Albert Einstein", "Niels Bohr", "Michael Faraday"], "answer": 2},
        {"question": "Which country is famous for sushi?", "options": ["Japan", "China", "Thailand", "Vietnam"], "answer": 1},
        {"question": "Which ocean is the smallest?", "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"], "answer": 4},
        {"question": "What is the capital of South Korea?", "options": ["Seoul", "Busan", "Incheon", "Gwangju"], "answer": 1},
        {"question": "What is the chemical symbol for Oxygen?", "options": ["O", "Ox", "Oy", "Og"], "answer": 1},
        {"question": "Which country is known for its pyramids?", "options": ["Mexico", "Peru", "Egypt", "China"], "answer": 3},
        {"question": "What is the primary function of the human skeletal system?", "options": ["Protection", "Movement", "Support", "All of the above"], "answer": 4},
        {"question": "What is the largest desert in the world?", "options": ["Sahara", "Gobi", "Kalahari", "Antarctic Desert"], "answer": 4},
        {"question": "Which planet is known as the 'Red Planet'?", "options": ["Mars", "Jupiter", "Venus", "Saturn"], "answer": 1},
        {"question": "What is the capital city of Spain?", "options": ["Madrid", "Barcelona", "Valencia", "Seville"], "answer": 1},
        {"question": "What is the chemical symbol for Potassium?", "options": ["P", "Pt", "K", "Po"], "answer": 3},
        {"question": "Which is the longest river in the world?", "options": ["Nile", "Amazon", "Yangtze", "Mississippi"], "answer": 2},
        {"question": "Which planet is known for its Great Red Spot?", "options": ["Jupiter", "Mars", "Saturn", "Neptune"], "answer": 1},
        {"question": "What is the capital city of Canada?", "options": ["Toronto", "Montreal", "Ottawa", "Vancouver"], "answer": 3},
        {"question": "What is the primary source of energy for the Earth?", "options": ["Moon", "Sun", "Wind", "Water"], "answer": 2},
        {"question": "What is the process by which plants make their food using sunlight?", "options": ["Photosynthesis", "Respiration", "Fermentation", "Digestion"], "answer": 1},
        {"question": "What is the name of the famous tower in Pisa, Italy?", "options": ["Leaning Tower of Pisa", "Eiffel Tower", "Big Ben", "Colosseum"], "answer": 1},
        {"question": "Which ocean is the largest?", "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "answer": 4},
        {"question": "Which city is known as the 'City of Angels'?", "options": ["Los Angeles", "Paris", "Rome", "New York"], "answer": 1},
        {"question": "Who is known as the 'King of Pop'?", "options": ["Elvis Presley", "Michael Jackson", "Prince", "Madonna"], "answer": 2},
        {"question": "What is the hardest natural substance on Earth?", "options": ["Gold", "Diamond", "Iron", "Platinum"], "answer": 2},
        {"question": "Which famous playwright wrote 'Romeo and Juliet'?", "options": ["William Shakespeare", "George Bernard Shaw", "Tennessee Williams", "Arthur Miller"], "answer": 1},
        {"question": "What is the capital city of Italy?", "options": ["Venice", "Florence", "Rome", "Milan"], "answer": 3},
        {"question": "Which is the largest planet in our solar system?", "options": ["Earth", "Mars", "Saturn", "Jupiter"], "answer": 4},
        {"question": "What is the process by which a caterpillar becomes a butterfly?", "options": ["Metamorphosis", "Photosynthesis", "Germination", "Respiration"], "answer": 1},
        {"question": "Which country is famous for its kangaroos?", "options": ["Australia", "New Zealand", "South Africa", "India"], "answer": 1},
        {"question": "What is the chemical symbol for Gold?", "options": ["Au", "Ag", "Pb", "Fe"], "answer": 1},
        {"question": "Which human organ is responsible for detoxifying the blood?", "options": ["Liver", "Kidney", "Heart", "Lungs"], "answer": 1},
        {"question": "What is the capital city of Australia?", "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"], "answer": 4},
        {"question": "Which famous structure is found in India?", "options": ["Eiffel Tower", "Great Wall", "Taj Mahal", "Colosseum"], "answer": 3},
        {"question": "What is the name of the largest ocean on Earth?", "options": ["Atlantic", "Indian", "Arctic", "Pacific"], "answer": 4},
        {"question": "Which planet is known for its extensive ring system?", "options": ["Saturn", "Jupiter", "Uranus", "Neptune"], "answer": 1},
        {"question": "What is the largest organ in the human body?", "options": ["Liver", "Skin", "Lungs", "Heart"], "answer": 2},
        {"question": "What is the capital city of Brazil?", "options": ["Rio de Janeiro", "São Paulo", "Brasília", "Salvador"], "answer": 3},
        {"question": "What is the smallest planet in our solar system?", "options": ["Mercury", "Mars", "Venus", "Earth"], "answer": 1},
        {"question": "Which country is known for the Eiffel Tower?", "options": ["Germany", "France", "Italy", "Spain"], "answer": 2},
        {"question": "What is the chemical symbol for Helium?", "options": ["He", "H", "Hl", "Ho"], "answer": 1},
        {"question": "Which famous scientist developed the theory of relativity?", "options": ["Isaac Newton", "Albert Einstein", "Niels Bohr", "Michael Faraday"], "answer": 2},
        {"question": "Which country is famous for sushi?", "options": ["Japan", "China", "Thailand", "Vietnam"], "answer": 1},
        {"question": "Which ocean is the smallest?", "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"], "answer": 4},
        {"question": "What is the capital of South Korea?", "options": ["Seoul", "Busan", "Incheon", "Gwangju"], "answer": 1},
        {"question": "What is the chemical symbol for Oxygen?", "options": ["O", "Ox", "Oy", "Og"], "answer": 1},
        {"question": "Which country is known for its pyramids?", "options": ["Mexico", "Peru", "Egypt", "China"], "answer": 3},
        {"question": "What is the primary function of the human skeletal system?", "options": ["Protection", "Movement", "Support", "All of the above"], "answer": 4},
        {"question": "What is the largest desert in the world?", "options": ["Sahara", "Gobi", "Kalahari", "Antarctic Desert"], "answer": 4},
        {"question": "Which planet is known as the 'Red Planet'?", "options": ["Mars", "Jupiter", "Venus", "Saturn"], "answer": 1},
        {"question": "What is the capital city of Spain?", "options": ["Madrid", "Barcelona", "Valencia", "Seville"], "answer": 1},
        {"question": "What is the chemical symbol for Potassium?", "options": ["P", "Pt", "K", "Po"], "answer": 3},
        {"question": "Which is the longest river in the world?", "options": ["Nile", "Amazon", "Yangtze", "Mississippi"], "answer": 2}
    ]

    # Shuffle the questions
    random.shuffle(questions)

    # Select the first 5 questions
    questions = questions[:5]

    # Initialize the score
    score = 0

    # Iterate through the shuffled questions
    for q in questions:
        # Ask the question
        print(q["question"])
        for i, option in enumerate(q["options"], start=1):
            print(f"{i}. {option}")

        # Get the user's answer
        try:
            answer = int(input("Enter your answer (1-4): "))
            if 1 <= answer <= 4:
                if answer == q["answer"]:
                    score += 1
                    print("Correct!")
                else:
                    print("Incorrect!")
            else:
                print("Invalid answer. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

    # Print the final score
    print(f"Your final score is {score} out of {len(questions)}")

# Run the quiz
quiz_game()
