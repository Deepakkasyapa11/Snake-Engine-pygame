# Modular Snake Engine (Pygame)

A robust, decoupled implementation of the classic Snake game logic using Python and Pygame. This project serves as a demonstration of **Model-View-Controller (MVC)** principles in a real-time game loop environment.
<img width="607" height="364" alt="Screenshot (141)" src="https://github.com/user-attachments/assets/4be52258-460f-44f1-a7a7-1a52359ed5ce" />

# Architectural Design
Unlike monolithic game scripts, this engine is built with a strict separation of concerns:
* **Settings Layer (`settings.py`):** Centralized configuration for physics (FPS), grid dimensions, and standardized color palettes.
* **Game Logic Engine (`engine.py`):** A pure Python implementation of snake movement and collision physics, completely agnostic of the rendering library.
* **View/Controller (`main.py`):** Handles the Pygame event loop, user input validation, and hardware-accelerated rendering.

# Key Engineering Features
* **Vector-Based Movement:** Directions are calculated using 2D coordinate vectors to simplify spatial math.
* **Input Buffering Logic:** Implemented directional locks to prevent 180-degree self-collision bugs.
* **Deterministic Grid System:** Ensures frame-independent collision detection via a discrete coordinate mapping system.

# Tech Stack
* **Language:** Python 3.x
* **Graphics:** Pygame
* **Architecture:** Object-Oriented (OOP) / Modular

# Installation & Execution
1. **Initialize Environment:**
   python -m venv venv
   .\venv\Scripts\activate
   pip install pygame
