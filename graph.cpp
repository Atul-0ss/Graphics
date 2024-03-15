#include <SFML/Graphics.hpp>

int main() {
    // Create a window
    sf::RenderWindow window(sf::VideoMode(800, 600), "SFML Rectangle");

    // Create a rectangle shape
    sf::RectangleShape rectangle(sf::Vector2f(200, 100));
    rectangle.setFillColor(sf::Color::Green); // Set rectangle color
    rectangle.setPosition(300, 200); // Set rectangle position

    // Main loop
    while (window.isOpen()) {
        // Handle events
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        // Clear the window
        window.clear();

        // Draw the rectangle
        window.draw(rectangle);

        // Display the window
        window.display();
    }

    return 0;
}
