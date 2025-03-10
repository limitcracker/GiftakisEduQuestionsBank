<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Roulette Game</title>
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/brython@3.10.7/brython.min.js"></script>
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/brython@3.10.7/brython_stdlib.js"></script>
</head>
<body>
    <div id="roulette-game" style="display: flex; gap: 20px;">
        <!-- Add IDE section -->
        <div class="code-editor">
            <h3>Write Your Betting Logic</h3>
            <textarea id="python-code" rows="15" cols="50">
def check_win(choice, result_number, result_color, bet):
    winnings = 0
    
    if str(choice).isdigit():
        choice = int(choice)
        if choice == result_number:
            winnings = bet * 35
    elif choice == result_color:
        winnings = bet * 2
    else:
        winnings = -bet
        
    return winnings
</textarea>
            <br>
            <button id="run-code">Update Logic</button>
            <div id="code-output"></div>
        </div>

        <!-- Existing game container -->
        <div class="container">
            <h1>Roulette Game</h1>
            <p>You have <span id="credits">100</span> credits.</p>
            <label for="bet">Bet Amount:</label>
            <input type="number" id="bet" min="1" value="10">
            <br>
            <label for="choice">Choose a number (0-36) or color (red/black):</label>
            <input type="text" id="choice" placeholder="Enter 0-36, red, or black" autocomplete="off">
            <br>
            <button id="spin">Spin the Wheel</button>
            <div class="wheel-container">
                <div class="pointer"></div>
                <div class="wheel" id="wheel"></div>
            </div>
            <div class="result" id="result"></div>
        </div>

        <style>
            #roulette-game {
                font-family: Arial, sans-serif;
                text-align: center;
                margin: 20px;
            }
            #roulette-game .container {
                display: inline-block;
                padding: 20px;
                border: 1px solid #ccc;
                border-radius: 10px;
                background-color: #f9f9f9;
                width: 500px;
                min-height: 700px;
            }
            #roulette-game input, 
            #roulette-game button {
                margin: 10px;
                padding: 5px;
            }
            #roulette-game .wheel-container {
                position: relative;
                width: 400px;
                height: 400px;
                margin: 40px auto 20px;
            }
            #roulette-game .wheel {
                width: 400px;
                height: 400px;
                border: 5px solid #333;
                border-radius: 50%;
                position: relative;
                background: linear-gradient(145deg, #1a1a1a, #3d3d3d);
                transition: transform 3s cubic-bezier(0.17, 0.67, 0.12, 0.99);
                overflow: visible;
            }
            #roulette-game .pointer {
                position: absolute;
                top: -25px;
                left: 50%;
                transform: translateX(-50%);
                width: 0;
                height: 0;
                border-left: 15px solid transparent;
                border-right: 15px solid transparent;
                border-top: 25px solid yellow;
                z-index: 2;
            }
            #roulette-game .number {
                position: absolute;
                width: 35px;
                height: 35px;
                line-height: 35px;
                text-align: center;
                color: white;
                font-weight: bold;
                font-size: 14px;
                border-radius: 50%;
                z-index: 10;
                box-shadow: 0 0 5px 2px rgba(255,255,255,0.3);
            }
            #roulette-game .red { background-color: #e74c3c; }
            #roulette-game .black { background-color: #000000; border: 1px solid #333; }
            #roulette-game .green { background-color: #27ae60; }
            #roulette-game .result {
                margin-top: 20px;
                font-weight: bold;
                min-height: 20px;
            }
            #roulette-game .number.winner {
                box-shadow: 0 0 15px 5px gold;
                z-index: 2;
                animation: pulse 1s infinite;
            }

            @keyframes pulse {
                0% { box-shadow: 0 0 15px 5px gold; }
                50% { box-shadow: 0 0 25px 8px gold; }
                100% { box-shadow: 0 0 15px 5px gold; }
            }

            #roulette-game button#spin {
                padding: 10px 20px;
                font-size: 16px;
                cursor: pointer;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                transition: background-color 0.3s;
                margin: 10px;
            }

            #roulette-game button#spin:disabled {
                background-color: #cccccc;
                cursor: not-allowed;
            }

            #roulette-game input {
                padding: 8px;
                margin: 5px;
            }

            #roulette-game .code-editor {
                padding: 20px;
                background: #f5f5f5;
                border-radius: 10px;
                border: 1px solid #ccc;
            }

            #roulette-game textarea#python-code {
                width: calc(100% - 20px);
                font-family: monospace;
                font-size: 14px;
                padding: 10px;
                background: #2d2d2d;
                color: #fff;
                border: 1px solid #666;
                border-radius: 5px;
                resize: vertical;
                margin: 0 10px;
            }

            #roulette-game #run-code {
                margin-top: 10px;
                padding: 8px 15px;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }

            #roulette-game #run-code:hover {
                background-color: #45a049;
            }

            #roulette-game #code-output {
                margin-top: 10px;
                padding: 10px;
                min-height: 50px;
                background: #fff;
                border: 1px solid #ddd;
                border-radius: 4px;
            }

            #roulette-game input#choice {
                padding: 8px;
                margin: 5px;
                width: 150px;
                border: 1px solid #ccc;
                border-radius: 4px;
                transition: background-color 0.3s;
            }

            #roulette-game input#choice:focus {
                outline: none;
                border-color: #4CAF50;
            }
        </style>

        <script>
            // Initialize Brython when this component loads
            window.addEventListener('load', function() {
                if (window.brython) {
                    brython();
                } else {
                    // Load Brython dynamically if not already loaded
                    const brythonScript = document.createElement('script');
                    brythonScript.src = 'https://cdn.jsdelivr.net/npm/brython@3.10.7/brython.min.js';
                    brythonScript.onload = function() {
                        const brythonStdlib = document.createElement('script');
                        brythonStdlib.src = 'https://cdn.jsdelivr.net/npm/brython@3.10.7/brython_stdlib.js';
                        brythonStdlib.onload = function() {
                            brython();
                        };
                        document.head.appendChild(brythonStdlib);
                    };
                    document.head.appendChild(brythonScript);
                }
            });
        </script>

        <script type="text/python">
            from browser import document, window, timer
            import random
            import math

            # Initialize default check_win function
            def check_win(choice, result_number, result_color, bet):
                winnings = 0
                if str(choice).isdigit():
                    choice = int(choice)
                    if choice == result_number:
                        winnings = bet * 35
                elif choice == result_color:
                    winnings = bet * 2
                else:
                    winnings = -bet
                return winnings

            def update_check_win_function(evt):
                global check_win
                try:
                    # Get code from textarea
                    new_code = document['python-code'].value
                    
                    # Create new namespace
                    namespace = {}
                    
                    # Execute the new code
                    exec(new_code, namespace)
                    
                    # Get the new check_win function
                    if 'check_win' in namespace:
                        check_win = namespace['check_win']
                        # Test the function
                        test_result = check_win('red', 1, 'red', 10)
                        document['code-output'].text = f"Logic updated successfully! Test result: {test_result}"
                        document['code-output'].style.color = 'green'
                    else:
                        document['code-output'].text = "Error: check_win function not found"
                        document['code-output'].style.color = 'red'
                except Exception as e:
                    document['code-output'].text = f"Error: {str(e)}"
                    document['code-output'].style.color = 'red'

            # Create wheel numbers
            wheel = document['wheel']
            numbers = [
                (0, 'green'), (32, 'red'), (15, 'black'), (19, 'red'), (4, 'black'),
                (21, 'red'), (2, 'black'), (25, 'red'), (17, 'black'), (34, 'red'),
                (6, 'black'), (27, 'red'), (13, 'black'), (36, 'red'), (11, 'black'),
                (30, 'red'), (8, 'black'), (23, 'red'), (10, 'black'), (5, 'red'),
                (24, 'black'), (16, 'red'), (33, 'black'), (1, 'red'), (20, 'black'),
                (14, 'red'), (31, 'black'), (9, 'red'), (22, 'black'), (18, 'red'),
                (29, 'black'), (7, 'red'), (28, 'black'), (12, 'red'), (35, 'black'),
                (3, 'red'), (26, 'black')
            ]

            # Track if wheel is currently spinning and total rotation
            is_spinning = False
            total_rotation = 0

            def validate_input(evt):
                value = evt.target.value
                if value.lower() in ['red', 'black'] or (value.isdigit() and 0 <= int(value) <= 36):
                    evt.target.style.backgroundColor = 'white'
                else:
                    evt.target.style.backgroundColor = '#ffebee'

            def spin(evt):
                global is_spinning
                if is_spinning:
                    return
                
                is_spinning = True
                document['spin'].disabled = True
                
                # Get bet amount and choice
                bet = int(document['bet'].value)
                choice = document['choice'].value.lower()
                credits = int(document['credits'].text)
                
                # Validate bet and choice
                if bet > credits:
                    document['result'].text = "Not enough credits!"
                    document['spin'].disabled = False
                    is_spinning = False
                    return
                
                if not (choice in ['red', 'black'] or (choice.isdigit() and 0 <= int(choice) <= 36)):
                    document['result'].text = "Invalid choice! Choose a number (0-36) or color (red/black)"
                    document['spin'].disabled = False
                    is_spinning = False
                    return
                
                # Remove previous winner class if exists
                winners = document.select('.winner')
                for winner in winners:
                    winner.classList.remove('winner')
                
                # Random spin result
                result_idx = random.randint(0, len(numbers) - 1)
                result_number, result_color = numbers[result_idx]
                
                # Calculate the target position
                angle_per_number = 360 / len(numbers)
                target_position = (360 - (result_idx * angle_per_number)) % 360
                
                # Reset wheel position instantly
                wheel.style.transition = 'none'
                wheel.style.transform = 'rotate(0deg)'
                
                # Force browser reflow
                wheel.offsetHeight
                
                # Spin to final position (reduced to 3 full rotations plus target)
                wheel.style.transition = 'transform 4s cubic-bezier(0.2, 0, 0.2, 1)'
                wheel.style.transform = f'rotate({360 * 3 + target_position}deg)'
                
                def end_spin():
                    global is_spinning
                    # Calculate winnings
                    winnings = check_win(choice, result_number, result_color, bet)
                    
                    # Update credits
                    new_credits = credits + winnings
                    document['credits'].text = str(new_credits)
                    
                    # Show result
                    win_text = "Won" if winnings > 0 else "Lost"
                    document['result'].text = f"{win_text}! Number: {result_number} ({result_color})"
                    
                    # Highlight winning number
                    numbers = document.select('.number')
                    numbers[result_idx].classList.add('winner')
                    
                    # Re-enable spin button
                    document['spin'].disabled = False
                    is_spinning = False
                
                # Wait for spin animation to complete (reduced to 4 seconds)
                timer.set_timeout(end_spin, 4000)

            # Position the numbers on the wheel
            for i, (number, color) in enumerate(numbers):
                num_div = document.createElement('div')
                num_div.className = f'number {color}'
                num_div.text = str(number)
                
                # Calculate angle for positioning (counterclockwise from top)
                angle = (i * 360 / len(numbers))
                radius = 165  # Distance from center of wheel
                
                # Calculate position using trigonometry
                # Start from top (90 degrees in standard position)
                radian_angle = math.radians(angle)
                x = 200 + radius * math.sin(radian_angle)
                y = 200 - radius * math.cos(radian_angle)
                
                # Center the number div and rotate to be readable
                # Rotate numbers to face outward
                num_div.style.transform = f'translate(-50%, -50%) rotate({angle}deg)'
                num_div.style.left = f"{x}px"
                num_div.style.top = f"{y}px"
                
                wheel <= num_div

            # Bind events
            document['run-code'].bind('click', update_check_win_function)
            document['choice'].bind('input', validate_input)
            document['spin'].bind('click', spin)
        </script>
    </div>
</body>
</html>
